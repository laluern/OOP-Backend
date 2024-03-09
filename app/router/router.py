from fastapi import FastAPI

from ..models.model import *
from ..database.database import controller

app = FastAPI()

flight_list = []

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

@app.post("/fill_info_and_select_package")
def fill_info_and_select_package(dto:dto_fill_info_and_select_package):
    return controller.fill_info_and_select_package(dto.user_id, dto.flight_instance_no, dto.gender, dto.tel_no, dto.name, dto.birth_date, dto.citizen_id, dto.package)

@app.get("/booking_details")
def booking_details(user_id:str, booking_no:str):
    return controller.booking_details(user_id, booking_no)

@app.get("/view_account_details")
def view_account_details(user_id : str):
    user = controller.search_user_by_user_id(user_id)
    return user.view_account_details()

@app.post("/register")
def register(dto:dto_register):
    return controller.register(dto.full_name, dto.email, dto.password, dto.phone_number, dto.address, dto.birth_date)

@app.post("/login")
def login(dto:dto_login):
    return controller.login(dto.email, dto.password)



