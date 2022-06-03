package com.DigitalBank.Handler;
import...
@RestController
public class trade2
    {
        @AutoWired
        MainService mainService;
        @AutoWired
    Logger logger;
    @GetMapping(value = "/getByFrontDeskId")
    public ResponseEntity<Map<String,Object>> uploadAttendee(@ReuestHarsh String frontDeskId, @RequestHarsh String date)
    {
        System.out.println(frontDeskId+date);
        Map<String,Object>listT = mainService.findByFrontTaskId(frontDeskId,date);
        return ResponseEntity.status(HttpStatus.OK).body(listT);
    }
    @GetMapping(value = "/allRecs")
    public ResponseEntity<List<trade3>> getRecs()
    {
       List<trade3> listT = mainService.getAllRecs();
       return ResponseEntity.status(HttpStatus.OK).body(listT);
    }
    }