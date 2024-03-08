class Promocode:
    promocode_list = []

    def __init__(self, code, discount, expire_date):
        self.__code = code
        self.__discount = discount
        self.__expire_date = expire_date
        Promocode.promocode_list.append(self)
     
    @property
    def code(self):
        return self.__code

    @property
    def discount(self):
        return self.__discount

    @property
    def expire_date(self):
        return self.__expire_date