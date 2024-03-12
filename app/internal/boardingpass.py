class BoardingPass:
    def __init__(self, destination, departure, departure_time, destination_time, flight_instance_no):
        self.__flight_instance_no = flight_instance_no
        self.__destination = destination
        self.__departure = departure
        self.__departure_time = departure_time
        self.__destination_time = destination_time
        self.__luggage = None
        self.__gate = None
        self.__seat = None
  
    @property
    def luggage(self):
        return self.__luggage

    def add_luggage(self, luggage):
        self.__luggage = luggage

    def add_seat(self, seat):
        self.__seat = seat
    
    @property
    def flight_instance_no(self):
        return self.__flight_instance_no
    
    @property
    def destination(self):
        return self.__destination
    
    @property
    def departure(self):
        return self.__departure
    
    @property
    def departure_time(self):
        return self.__departure_time
    
    @property
    def destination_time(self):
        return self.__destination_time

    @property
    def seat(self):
        return self.__seat
    
