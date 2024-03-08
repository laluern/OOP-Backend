from .payment import Payment

class Transaction:
    __id = 1000000
    def __init__(self, booking, amount, payment_method: Payment): 
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__transaction_id = Transaction.__id
        self.__status = False
        Transaction.__id += 1
    
    def show_payment(self):
        return {
                "transaction_id": self.__transaction_id,
                "amount": self.__amount,
                "status" : True
                }