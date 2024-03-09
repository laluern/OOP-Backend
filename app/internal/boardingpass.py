class BoardingPass:
    def __init__(self, destination, departure, departure_time, destination_time, flight_instance_no):
        self.__flight_instance_no = flight_instance_no
        self.__destination = destination
        self.__departure = departure
        self.__departure_time = departure_time
        self.__destination_time = destination_time
        self.__luggage_list = []
        self.__gate = None
        self.__seat = None

    def add_luggage(self, luggage):
        self.__luggage_list.append(luggage)

    def add_seat(self, seat):
        self.__seat = seat
    
    @property
    def seat(self):
        return self.__seat
    
    @property
    def luggage_list(self):
        return self.__luggage_list