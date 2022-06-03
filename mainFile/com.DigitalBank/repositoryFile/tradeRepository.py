package com.DigitalBank.repository;
import ...
@resipotory
public interfacetradeRepositiry extends crudRepository<trade3,Integer>
{
    @Query(value = "select * from trade_3",nativeQuery = true)
public List<trade3>getAllRecs();
@Query(value = "select * from trade_3 t where t.FRONT_DESK_OFF_ID=? and t.TRADE_DATE_TIME=?", natieQuery = true)
public List<trade3> findFrontTaskId(String frontDeskOfficerId,String date);
}