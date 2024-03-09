from .flight import Flight

class FlightInstance(Flight):
    flight_instance_number = 1
    def __init__(self, departure, destination, flight_no, departure_time, destination_time, airplane):
        super().__init__(departure, destination, flight_no)
        self.__flight_instance_no = f"FI{FlightInstance.flight_instance_number:05d}"
        self.__departure_time = departure_time
        self.__destination_time = destination_time
        self.__airplane = airplane
        self.__reserved_seat_list = []
        self.__gate = None
        FlightInstance.flight_instance_number += 1

    @property
    def flight_instance_no(self):
        return self.__flight_instance_no
        
    @property
    def departure_time(self):
        return self.__departure_time
    @property
    def destination_time(self):
        return self.__destination_time

    @property
    def airplane(self):
        return self.__airplane

    @property
    def gate(self):
        return self.__gate
    
    @gate.setter
    def gate(self, gate):
        self.__gate = gate

    @property
    def reserved_seat_list(self):
        return self.__reserved_seat_list

    def add_reserved_seat(self, reserved_seat):
        self.reserved_seat_list.append(reserved_seat)