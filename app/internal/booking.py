class Booking:

    booking_number = 1
    
    def __init__(self, departure, destination, departure_time, arriving_time):
        self.__booking_no = f"B{Booking.booking_number:05d}"
        self.__passenger_list = []
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__arriving_time = arriving_time
        self.__booking_status = False
        self.__payment = None 
        Booking.booking_number += 1

    def update_booking_status(self):
        pass
    
    def update_payment(self):
        pass

    def add_passenger(self, passenger):
        self.__passenger_list.append(passenger)

    def add_payment(self, payment):
        self.__payment = payment

    def set_booking_status(self):
        self.__booking_status = True

    @property
    def payment(self):
        return self.__payment

    @property
    def booking_status(self):
        return self.__booking_status    

    @property
    def passenger(self):
        return self.__passenger_list

    @property
    def booking_no(self):
        return self.__booking_no

    @property
    def destination(self):
        return self.__destination

    @property
    def departure(self):
        return self.__departure
    
    @property
    def departure_date(self):
        return self.__departure_date

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def arriving_date(self):
        return self.__arriving_date
    
    @property
    def arriving_time(self):
        return self.__arriving_time