from .payment import Payment

class MobileBanking(Payment):
    type_of_payment = "mobilebanking"
    
    def processing_payment(self, price_summary, info):
        self.__owner_name = info.owner_name
        self.__tel_no = info.tel_no
        self.__account_id = info.account_no
        self.__password = info.password
        self.__balance = 10000
        
        if self.__balance >= price_summary:
            self.__balance - price_summary
            return "Payment successful"
        else:
            return "Not enough money"