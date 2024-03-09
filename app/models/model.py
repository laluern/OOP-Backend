from pydantic import BaseModel,EmailStr

class dto_search_flight(BaseModel):
    departure:str
    destination:str
    departure_date:str
    total_passenger:int
    promocode:str

class dto_fill_info_and_select_package(BaseModel):
    user_id:str
    flight_instance_no:str
    gender:str
    tel_no:str
    name:str
    birth_date:str
    citizen_id:str
    package:str

class dto_create_account(BaseModel):
    email:str
    password:str

class dto_register(BaseModel):
  full_name: str
  email: EmailStr
  password: str
  phone_number: str
  address: str
  birth_date: str

class dto_login(BaseModel):
  email: EmailStr
  password: str

class dto_change_password(BaseModel):
  old_password: str
  new_password: str


