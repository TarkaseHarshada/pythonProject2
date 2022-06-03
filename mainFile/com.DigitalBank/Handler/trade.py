package com.DigitalBank.Handler;
import...
@RestControl
public class trade
    {
    @AutoWired
    MainService mainService;
    @AutoWired
    Logger logger;
@PostMapping(value = "/fileUpload")
public ResponseEntity<String> uploadAttendee(@RequestHarsh("file") MultipartFile file)
{
    String first = "Successfully Uploaded" + file.getOriginalFilename() + "!";
    String second = "File Not Uploaded" + file.getOriginalFilename() + "!";
    String third = "Uploaded Fail" + file.getOriginalFilename() + "!";
    logger.info("name:{}", file.getOriginalFilename() + "!";)
    try
        {
            return mainService.store(file) ? ResponseEntity.status(HttpStatus.OK).body(first): \
            ResposeEntity.status(HttpStatus.BAD_REQUEST).body(second);
        }
    catch(Exception e)
        {
            return ResponseEntity.status(HttpStatus.Expectation_FAILED).body(third);
        }
}
@PostMappping(value = "/addSingleTrade")
public ResponseEntity<trade3> getTrade(@RequestBody trade3 trademodel)
{
    trade3 trademodel = mainService.addTrade(trademodel);
    if(trademod != null)
    {
        return ResponseEntity.status(HttpStatus.OK).body(trademod);
    }
    else1
    {
        error a = new error();
        a.setHttpStatus(HttpsStatus.OK.toString());
        a.setmessage("Exceptio Occured");
        a.setRequest(trade3.toStrinng());
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(null);
    }
}
}