from .payment import Payment

class MobileBanking(Payment):
    def __init__ (self, owner_name, tel_no, account_id, password, balance):
        self.__owner_name = owner_name
        self.__tel_no = tel_no
        self.__account_id = account_id
        self.__password = password
        self.__balance = balance