class Luggage:
    luggage_number = 1
    def __init__(self, package, luggage_id, price):
        self.__owner = None
        self.__package = package
        self.__luggage_id = f"Luggage{Luggage.luggage_number:05d}"
        self.__price = price
        Luggage.luggage_number += 1


    def set_owner(self, owner):
        self.__owner = owner

    @property
    def luggage_id(self):
        return self.__luggage_id

    @property
    def price(self):
        return self.__price