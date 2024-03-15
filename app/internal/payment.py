class Payment:
    def __init__(self):
        self.__owner_name = None
        if self.type_of_payment == "creditcard":
            self.__card_no = None
            self.__expiration_date = None
            self.__security_code = None
            self.__limit = None
        elif self.type_of_payment == "mobilebanking":
            self.__tel_no = None
            self.__account_id = None
            self.__password = None
            self.__balance = None