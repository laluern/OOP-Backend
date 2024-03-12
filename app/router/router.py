from fastapi import FastAPI

from ..models.model import *
from ..database.database import controller
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173",
    "http://127.0.0.1:5173",
    "127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

flight_list = []
Booking_details = None


@app.get("/{user_id}/view_personal_info")
def view_personal_info(user_id):
    try:
        user = controller.search_user_by_user_id(user_id)
        if user:
            return user.view_personal_info()
    except:
        return "could not reach account details"

@app.get("/{user_id}/view_my_bookings")
def view_my_bookings(user_id):
    try:
        user = controller.search_user_by_user_id(user_id)
        if user:
            return user.view_my_bookings()
    except:
        return "could not reach booking details"     
    
@app.post("/search_flight")
def search_flight(dto:dto_search_flight):
    try:
        global flight_list
        flight_list = controller.search_flight(dto.departure, dto.destination, dto.departure_date, dto.total_passenger, dto.promocode)
        return flight_list
    except:
        return "could not matched a flight"

@app.get("/select_flight")
def select_flight(sort_by:str):
    try:
        sorted_flight = controller.sort_flight(flight_list, sort_by)
        if sorted_flight:
            return sorted_flight
    except:
        return "could not find a flight"

@app.get("/{flight_instance_no}/select_seat")
def select_seat(flight_instance_no):
    return controller.get_seat_data(flight_instance_no)

@app.post("/{user_id}/{flight_instance_no}/create_booking")
def create_booking(user_id, flight_instance_no):
    try:
        booking = controller.create_booking(user_id, flight_instance_no)
        if booking:
            return booking
    except:
        return "failed to create booking"

@app.post("/{user_id}/cancel_booking")
def cancel_booking(user_id, booking_no:str):
    try:
        controller.cancel_booking(user_id, booking_no)
        return "Cancel booking succesfully"
    except:
        return "failed to create booking"

@app.post("/{user_id}/{booking_no}/{flight_instance_no}/fill_info")
def fill_info_and_select_package(user_id, booking_no, flight_instance_no, dto:dto_fill_info):
    try:
        fill_infomation = controller.fill_info(user_id, flight_instance_no, booking_no, dto.seat_no, dto.package, dto.gender, dto.tel_no, dto.name, dto.birth_date, dto.citizen_id)
        if  fill_infomation:
            return fill_infomation
    except:
        return "failed to fill infomation"

@app.get("/{user_id}/{booking_no}/booking_details")
def booking_details(user_id, booking_no):
    try:
        Booking_details = controller.booking_details(user_id, booking_no)
        if Booking_details:
            return Booking_details
    except:
        return "could not reach booking details"

@app.put("/{user_id}/payment_method/creditcard")
def card_paid(user_id, booking_id, card_info:card_info):
    # try:
        Booking_details = controller.booking_details(user_id, booking_id)
        payment = controller.pay(user_id, booking_id, Booking_details, 0, card_info)
        if payment:
            return {f"message: {payment} is successfull"}      
    # except:
    #     return "card payment failed" 

@app.put("/{user_id}/payment_method/mobilebanking")
def mobilebanking_paid(user_id, booking_id, bank_account_info:bank_account_info):
    try:
        Booking_details = controller.booking_details(user_id, booking_id)
        payment = controller.pay(user_id, booking_id, Booking_details, 1, bank_account_info)
        if payment:
            return {f"message: {payment} is successfull"}
    except:
        return "mobilebanking payment failed" 

@app.post("/login")
def login(user_data: dto_login):
    try:
        user = controller.verify_login(user_data)
        if user:
            return {"message": "Logged in successfully", "user": user , "status": True}
        else:
            return {"message": "Failed to login"}
    except:
        return "please try again"  

@app.post("/register")
def create_user(user_data: dto_register):
    try :
        if controller.verify_username(user_data.email) == True:
            new_user = controller.register(user_data.full_name, user_data.email, controller.hash_password(user_data.password), user_data.phone_number, user_data.address, user_data.birth_date)
            if new_user != None:
                return {"message": f"{new_user.full_name} account created successfully", "status": True}
            else:
                return {"message": "Failed to create user"}
        else: return {"message": "Failed to create user"}
    except :
        return "please try again"

