from app.database.database import controller

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.router.router:app", host="127.0.0.1", port=8000, log_level="info")

############################################################################################

#TODO get_available_seat
# print(controller.get_available_seat("FI00001"))

# #TODO seacrh_flgiht
# print(controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1))
# print(controller.search_flight("Chiang Mai", "Suvarnabhumi", "2024-04-01", 1))
# print(controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1, "A1000"))

# #TODO sort_flight
# flight_list = controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1)
# print("Cheapest")
# print(controller.sort_flight(flight_list, "Cheapest"))
# print("Fastest")
# print(controller.sort_flight(flight_list, "Fastest"))
# print("Earliest")
# print(controller.sort_flight(flight_list, "Earliest"))

# #TODO get_seat_data
# print(controller.get_seat_data("FI00003"))


# #TODO create_booking
# print(controller.create_booking("U00001", "FI00001"))

# #TODO fill_info_and_select_luggage_weight
# print(controller.fill_info("U00001", "FI00001", "B00001", "1A", "15kg", "male", "0812895077", "Peerawat Ingkhasantatikul", "2004-08-12", "123456"))
# print(controller.fill_info("U00001", "FI00001", "B00001", "1A", "30kg", "male", "0812895077", "Supakarn Tantichawa-ochanon", "2004-08-12", "123456"))

# #TODO booking_details
# print(controller.booking_details("U00001", "B00001"))

# #TODO payment ถ้าจะเทสต้องไปเปลี่ยนวิธีดึงตัวแปลใน creditcard หรือ mobilebanking
info = {
    "card_holder_name": "Supakarn",
    "card_no": "191",
    "expiration_date": "2032-10-10",
    "security_code": "123"
}
print(controller.pay("U00001", "B00001", controller.booking_details("U00001", "B00001"),0,info))

# #TODO register 
# user_data_register = {
#     "full_name": "kwai",
#     "email": "kwai@gmail.com",
#     "password": "1111",
#     "phone_number": "1111",
#     "address": "1111",
#     "birth_date": "1111"
# }

# controller.register(user_data_register["full_name"], user_data_register["email"], controller.hash_password(user_data_register["password"]), user_data_register["phone_number"], user_data_register["address"], user_data_register["birth_date"])
# print(controller.register)

# #TODO login ถ้าจะเทสต้องไปเปลี่ยนวิธีดึงตัวแปลใน controller.verify_login
# user_data_login = {
#     "email": "kwai@gmail.com",
#     "password": "1111"
# }
# print(controller.verify_login(user_data_login))