from .payment import Payment

class CreditCard(Payment):
    def __init__ (self, card_holder_name, card_no, expiration_date, security_code, limit):
        self.__card_holder_name = card_holder_name
        self.__card_no = card_no
        self.__expiration_date = expiration_date
        self.__security_code = security_code
        self.__limit = limit