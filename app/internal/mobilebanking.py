from .payment import Payment

class MobileBanking(Payment):
    def __init__ (self):
        self.__account_no = None
        self.__status = False
    
    def pay(self, account_no):
        self.__account_no = account_no
        self.__status = True
        return True

    @property
    def status(self):
        return self.__status