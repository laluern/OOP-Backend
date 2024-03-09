from datetime import datetime

from .user import User
from .promocode import Promocode
from .booking import Booking
from .passenger import Passenger
from .boardingpass import BoardingPass
from .luggage import Luggage
from .seat import Seat
from .flightinstance import FlightInstance

class Controller:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__guest_list = []
        self.__flight_list = []
        self.__flight_instance_list = []
        self.__admin_list = []
        self.__airplane_list = []
        self.__airport_list = []

    def get_seat_data(self, flight_instance_no):
        flight_instance = self.search_flight_instance_by_flight_instance_no(flight_instance_no)
        airplane = self.search_airplane_by_airplane_id(flight_instance.airplane)
        seat_list = airplane.seat_list
        reserved_seat_list = flight_instance.reserved_seat_list
        seat_detail = {}
        available_seat = []
        for seat in seat_list:
            seat_detail[seat.row + seat.column] = [seat.seat_type, seat.price]
            available_seat.append(seat.row + seat.column)
            for reserved_seat in reserved_seat_list:
                if (seat.row + seat.column) == (reserved_seat.row + reserved_seat.column):
                    available_seat.remove(reserved_seat.row + reserved_seat.column)
        seat_data = {"seat_detail":seat_detail, "available_seat":available_seat}
        return seat_data
    
    def search_flight(self, departure_name, destination_name, departure_time, total_passenger, promocode = ""):
        flight_list = {}
        departure = self.search_airport_by_airport_name(departure_name)
        destination = self.search_airport_by_airport_name(destination_name)
        for flight_instance in self.__flight_instance_list:
            airplane = self.search_airplane_by_airplane_id(flight_instance.airplane)
            if flight_instance.departure == departure_name and flight_instance.destination == destination_name and str(flight_instance.departure_time.date()) == departure_time:
                available_seat = self.get_seat_data(flight_instance.flight_instance_no)["available_seat"]
                if len(available_seat) >= total_passenger:
                    lowest__price_seat = min(available_seat, key=lambda seat_no: airplane.search_seat_by_seat_no(seat_no).price)
                    lowest_price = airplane.search_seat_by_seat_no(lowest__price_seat).price
                   
                    flight_departure_time = flight_instance.departure_time
                    flight_destination_time = flight_instance.destination_time
                    duration = flight_destination_time - flight_departure_time
                    discount_price = lowest_price

                    if promocode != "":
                        for cur_promocode in Promocode.promocode_list:
                            if cur_promocode.code == promocode:
                                discount_price =  lowest_price - (lowest_price * (cur_promocode.discount/100))
                                break
                        flight_list[flight_instance.flight_instance_no] = [departure.airport_code, flight_departure_time, destination.airport_code, flight_destination_time, int(duration.total_seconds()), float(lowest_price), float(discount_price)]
                    else:
                        flight_list[flight_instance.flight_instance_no] = [departure.airport_code, flight_departure_time, destination.airport_code, flight_destination_time, int(duration.total_seconds()), float(lowest_price), float(discount_price)]
        return flight_list
    
    def sort_flight(self, flight_list, sort_by):
        if sort_by == "Cheapest":
            flight_order = dict(sorted(flight_list.items(), key = lambda item:item[1][6]))
            return self.show_flight_format(flight_order)
        elif sort_by == "Fastest":
            flight_order = dict(sorted(flight_list.items(), key = lambda item:item[1][4]))
            return self.show_flight_format(flight_order)
        elif sort_by == "Earliest":
            flight_order = dict(sorted(flight_list.items(), key = lambda item:item[1][1]))
            return self.show_flight_format(flight_order)

    def fill_info_and_select_luggage_weight(self, user_id, seat_no, flight_instance_no, gender, tel_no, name, birth_date, citizen_id, weight = ""):
        flight_instance = self.search_flight_instance_by_flight_instance_no(flight_instance_no)
        airplane = self.search_airplane_by_airplane_id(flight_instance.airplane)
        user = self.search_user_by_user_id(user_id)
        temporary_seat = self.search_seat_by_seat_no(seat_no, airplane)
        
        booking = Booking(Booking.booking_no, flight_instance.destination, flight_instance.departure, flight_instance.departure_time, flight_instance.destination_time)
        passenger = Passenger(gender, tel_no, name, birth_date, citizen_id)
        boardingpass = BoardingPass(flight_instance.destination, flight_instance.departure, flight_instance.departure_time, flight_instance.destination_time, flight_instance.flight_instance_no)
        
        if weight != "":
            boardingpass.add_luggage(Luggage(weight, Luggage.luggage_id))
            
        boardingpass.add_seat(temporary_seat)
        passenger.add_boardingpass(boardingpass)
        booking.add_passenger(passenger)
        user.add_booking(booking)
        return booking.booking_no
    
    def booking_details(self, user_id, booking_no):
        booking_details = {}
        user = self.search_user_by_user_id(user_id)
        booking = user.search_booking_by_number(booking_no)
        passengers = booking.passenger
        total_passenser = 0
        seat_price = 0
        total_luggages = 0
        luggage_price = 0
        price_summary = 0

        for passenger in passengers:    
            boarding_pass = passenger.boarding_pass
            luggages = boarding_pass.luggage_list

            for luggage in luggages:
                luggage_price += self.get_luggage_price(luggage.weight)
                total_luggages += 1

            seat = boarding_pass.seat
            seat_price += seat.price
            total_passenser += 1

        booking_details = {
            "departure" : booking.departure,
            "destination" : booking.destination,
            "departure_time" : booking.departure_time,
            "price" : {
                      f"seat price (x{total_passenser})" : seat_price,
                      f"luggages price (x{total_luggages})" : luggage_price,
                      f"Summary price" : seat_price + luggage_price
            }
        }
        return booking_details

    def register(self, full_name, email, password, phone_number, address, birth_date):
        if self.search_user_by_full_name(full_name) != None:
            return "Name already used"
        if self.search_user_by_email(email) != None:
            return "Email already used"
        if self.search_user_by_phone_number(phone_number) != None:
            return "Phone number already used"
        
        user = User(full_name, email, password, phone_number, address, birth_date)
        self.add_user(user)
        return "Done"

    def login(self, email, password):
        user = self.search_user_by_email(email)
        if user == None:
            return "Wrong username or password"
        if user.password != password:
            return "Wrong username or password"
        return user.user_id        
        
    def search_seat_by_seat_no(self, seat_no, airplane):
        
        for seat in airplane.seat_list:
            if (seat.row + seat.column) == seat_no:
                return seat

    def search_user_by_user_id(self, user_id):
        for user in self.__user_list:
            if user.user_id == user_id:
                return user

    def search_user_by_phone_number(self, phone_number):
        for user in self.__user_list:
            if user.phone_number == phone_number:
                return user 

    def search_user_by_full_name(self, full_name):
        for user in self.__user_list:
            if user.full_name == full_name:
                return user       
    
    def search_user_by_email(self, email):
        for user in self.__user_list:
            if user.email == email:
                return user

    def search_flight_instance_by_flight_instance_no(self, flight_instance_no):
        for flight_instance in self.__flight_instance_list:
            if flight_instance.flight_instance_no == flight_instance_no:
                return flight_instance
    
    def search_airport_by_airport_name(self, airport_name):
        for airport in self.__airport_list:
            if airport.airport_name == airport_name:
                return airport
    
    def search_airplane_by_airplane_id(self, airplane_id):
        for airplane in self.__airplane_list:
            if airplane.airplane_id == airplane_id:
                return airplane
    
    def search_flight_by_flight_no(self, flight_no):
        for flight in self.__flight_list:
            if flight.flight_no == flight_no:
                return flight
            
    def show_flight_format(self, flight_instance_list):
        format_flight_instance_list = {}
        for flight_instance_no in flight_instance_list.keys():
            format_flight_instance_list[flight_instance_no] = []
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][0])
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][1].strftime("%Y-%m-%d %H:%M"))
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][2])
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][3].strftime("%Y-%m-%d %H:%M"))
            hours, remainder = divmod(flight_instance_list[flight_instance_no][4], 3600)
            minutes, _ = divmod(remainder, 60)
            format_flight_instance_list[flight_instance_no].append(f"{hours}h {minutes}m")
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][5])
            format_flight_instance_list[flight_instance_no].append(flight_instance_list[flight_instance_no][6])
        return format_flight_instance_list

    def set_seat_price(self, flight_instance_no, base_price):
        flight_instance = self.search_flight_instance_by_flight_instance_no(flight_instance_no)
        airplane = self.search_airplane_by_airplane_id(flight_instance.airplane)
        airplane.set_seat_price(base_price)

    def get_luggage_price(self, weight):
        return int("".join(filter(str.isdigit, weight))) * 30
        
        
    def add_flight_list(self, flight):
        self.__flight_list.append(flight)

    def add_airplane(self, airplane):
        self.__airplane_list.append(airplane)

    def add_flight_instance_list(self, flight_no, departure_time, destination_time, airplane):
        flight = self.search_flight_by_flight_no(flight_no)
        self.__flight_instance_list.append(FlightInstance(flight.departure, flight.destination, flight.flight_no, departure_time, destination_time, airplane))
        
    def add_admin(self, admin):
        self.__admin_list.append(admin)

    def add_user(self, user):
        self.__user_list.append(user)

    def add_airport(self, airport):
        self.__airport_list.append(airport)

    def add_promocode(self, code):
        Promocode.promocode_list.append(code)
    
    @property
    def flight_instance_list(self):
        return self.__flight_instance_list

    @property
    def user_list(self):
        return self.__user_list

    @property
    def guest_list(self):
        return self.__guest_list