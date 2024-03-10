class Payment:
    transaction_number = 1
    def __init__(self, booking_no, price_summary):
        self.__booking_no = booking_no
        self.__price_summary = price_summary
        self.__transaction_id = f"T{Payment.transaction_number:05d}"

    @property
    def price_summary(self):
        return self.__price_summary

    @property
    def booking_no(self):
        return self.__booking_no