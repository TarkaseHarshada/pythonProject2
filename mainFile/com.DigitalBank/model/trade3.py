@Entity
@Table
public class trade3
    {
        @Id @column @GenerateValue(strategy = GenerationType.IDENTITY)
        public Integer id;
        @column
        public Integer customerId;
        @column
        public String orderNum;
        @column
        public String shareName;
        @column public String shareId;
        @column public String quantity;
        @column public String buyorsell;
        @column public int pricepershare;
        @column public int account;
        @column public int frontDeskOffId;
        @column public String branchcode;
        @column public int tradingcharge;
        @column public String exchange;
        @column public Date tradeDataTime;
        public Integer getcustomerId()
        {
            return cusomerId;
        }
        public void setcustomerId(Integer customerId)
       {
           this.customerId = customerId;
       }
        public String getorderNum()
        {
            return orderNum;
        }
        public trade3(){}
        public trade3(Integer customerId, String orderNum, String shareName, shareId,
                        String quantity,String buyorsell, int pricepershare, int account,
                        int frontDeskOffId, String branchcode, int tradingcharge,
                        String exchange, Date tradeDataTime)
        {
            super ();
            this.customerId = customerId;
            this.orderNum = orderNum;
        }

    }