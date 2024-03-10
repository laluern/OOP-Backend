from .booking import Booking

class User():
    user_number = 1
    def __init__(self, full_name, email, password, phone_number, address, birth_date):
        self.__full_name = full_name
        self.__email = email
        self.__user_id = f"U{User.user_number:05d}"
        self.__booking_list = []
        self.__password = password
        self.__phone_number = phone_number
        User.user_number += 1
        
    @property
    def email(self):
        return self.__email
    
    @property
    def full_name(self):
        return self.__full_name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def password(self):
        return self.__password

    @property
    def user_id(self):
        return self.__user_id


    def view_account_details(self):
        account_detail = []
        booking_info_list = []
        for that_booking in self.__booking_list:
            booking_info = []
            booking_info.append(that_booking.booking_no)
            booking_info.append(that_booking.departure)
            booking_info.append(that_booking.destination)
            booking_info.append(that_booking.departure_time)
            booking_info.append(that_booking.arriving_time)
            booking_info_list.append(booking_info)
        
        account_detail.append(self.__email)
        account_detail.append(self.__user_id)
        account_detail.append(booking_info_list)
        return account_detail
            
   

    def add_booking(self, booking):
        if isinstance(booking, Booking):
            self.__booking_list.append(booking)

    def search_booking_by_number(self, booking_number):
        for booking in self.__booking_list:
            if isinstance(booking, Booking) and booking_number == booking.booking_no:
                return booking