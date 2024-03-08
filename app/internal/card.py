from .payment import Payment

class Card(Payment):
    def __init__ (self):
        self.__card_no = None
        self.__security_code = None
        self.__status = False
    
    def pay(self, card_no, security_code):
        self.__card_no = card_no
        self.__security_code = security_code
        self.__status = True

    @property
    def status(self):
        return self.__status