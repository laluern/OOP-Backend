class Seat:
    def __init__(self, row, column, seat_type):
        self.__row = row
        self.__column = column
        self.__seat_type = seat_type
        self.__price = None

    @property
    def row(self):
        return self.__row
    @property
    def column(self):
        return self.__column

    @property
    def seat_type(self):
        return self.__seat_type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        self.__price = amount
    
