from .flight import Flight
from .showseat import ShowSeat

class FlightInstance(Flight):
    flight_instance_number = 1
    def __init__(self, departure, destination, flight_no, departure_time, destination_time, airplane):
        super().__init__(departure, destination, flight_no)
        self.__flight_instance_no = f"FI{FlightInstance.flight_instance_number:05d}"
        self.__departure_time = departure_time
        self.__destination_time = destination_time
        self.__airplane = airplane
        self.__show_seat_list = []
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
    def show_seat_list(self):
        return self.__show_seat_list
    
    def set_seat_price(self, airplane, base_price):
        for seat in airplane.seat_list:
            if seat.seat_type == "hot_seat":
                self.__show_seat_list.append(ShowSeat(seat.row, seat.column, seat.seat_type, base_price * 1.5))
            else:
                if seat.column == "B" or seat.column == "E":
                    self.__show_seat_list.append(ShowSeat(seat.row, seat.column, seat.seat_type, base_price))
                else:
                    self.__show_seat_list.append(ShowSeat(seat.row, seat.column, seat.seat_type, base_price * 1.2))

    def search_seat_by_seat_no(self, seat_no):
        for show_seat in self.__show_seat_list:
            if (show_seat.row + show_seat.column) == seat_no:
                return show_seat