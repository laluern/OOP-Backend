from fastapi import FastAPI

from ..models.model import *
from ..database.database import controller
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/search_flight")
def search_flight(dto:dto_search_flight):
    global flight_list
    flight_list = controller.search_flight(dto.departure, dto.destination, dto.departure_date, dto.total_passenger, dto.promocode)
    return flight_list

@app.get("/select_flight")
def select_flight(sort_by:str):
    return controller.sort_flight(flight_list, sort_by)

@app.get("/select_seat")
def select_seat(flight_instance_no:str):
    return controller.get_seat_data(flight_instance_no)

@app.post("/{user_id}/{flight_instance_no}/fill_info_and_select_package")
def fill_info_and_select_package(user_id, flight_instance_no, dto:dto_fill_info_and_select_package):
    return controller.fill_info_and_select_package(user_id, flight_instance_no, dto.gender, dto.tel_no, dto.name, dto.birth_date, dto.citizen_id, dto.package)

@app.get("/{user_id}/{booking_no}/booking_details")
def booking_details(user_id, booking_no):
    global Booking_details
    Booking_details = controller.booking_details(user_id, booking_no)
    return Booking_details

@app.get("/{user_id}/view_account_details")
def view_account_details(user_id):
    user = controller.search_user_by_user_id(user_id)
    return user.view_account_details()

@app.post("/register")
def register(dto:dto_register):
    return controller.register(dto.full_name, dto.email, dto.password, dto.phone_number, dto.address, dto.birth_date)

@app.post("/login")
def login(dto:dto_login):
    return controller.login(dto.email, dto.password)

@app.put("/{user_id}/payment_method/creditcard")
def card_paid(user_id, booking_id, card_info:card_info):
    return controller.pay(user_id, booking_id, Booking_details, 0, card_info)

@app.put("/{user_id}/payment_method/mobilebanking")
def card_paid(user_id, booking_id, bank_account_info:bank_account_info):
    return controller.pay(user_id, booking_id, Booking_details, 1, bank_account_info)


