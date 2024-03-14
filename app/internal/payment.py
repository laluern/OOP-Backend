class Payment:
    def __init__(self, booking_no, price_summary):
        self.__booking_no = booking_no
        self.__price_summary = price_summary
        self.__transaction_payment_method = None

    @property
    def payment_method(self):
        return self.__transaction_payment_method

    @property
    def price_summary(self):
        return self.__price_summary

    @property
    def booking_no(self):
        return self.__booking_no

    def set_payment_method(self, method):
        if method == 0:
            self.__transaction_payment_method = "CreditCard"
        elif method == 1:
            self.__transaction_payment_method = "MobileBanking"