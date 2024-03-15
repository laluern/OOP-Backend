from datetime import datetime

from ..internal.controller import Controller
from ..internal.flight import Flight
from ..internal.airport import Airport
from ..internal.airplane import Airplane
from ..internal.promocode import PromoCode
from ..internal.creditcard import CreditCard
from ..internal.mobilebanking import MobileBanking
from ..internal.user import User


controller = Controller("MeltAsia")

controller.add_airport(Airport("Suvarnabhumi", "BKK"))
controller.add_airport(Airport("Chiang Mai", "CNX"))
controller.add_airport(Airport("Hat Yai", "HDY"))
controller.add_airport(Airport("Khon Kaen", "KKC"))

controller.add_airplane(Airplane(60)) #A00001
controller.add_airplane(Airplane(60)) #A00002
controller.add_airplane(Airplane(60)) #A00003
controller.add_airplane(Airplane(60)) #A00004
controller.add_airplane(Airplane(60)) #A00005
controller.add_airplane(Airplane(60)) #A00006
controller.add_airplane(Airplane(60)) #A00007
controller.add_airplane(Airplane(60)) #A00008
controller.add_airplane(Airplane(60)) #A00009
controller.add_airplane(Airplane(60)) #A00010
controller.add_airplane(Airplane(60)) #A00011
controller.add_airplane(Airplane(60)) #A00012

PromoCode('A1000', 10, datetime(2020, 1, 1))
PromoCode('A2000', 10, datetime(2029, 1, 1))
PromoCode('A3000', 10, datetime(2029, 1, 1))
PromoCode('B1000', 20, datetime(2029, 1, 1))
PromoCode('B2000', 20, datetime(2029, 1, 1))
PromoCode('C3000', 30, datetime(2029, 1, 1))

controller.add_flight_list(Flight("Suvarnabhumi", "Chiang Mai", "F00001"))
controller.add_flight_list(Flight("Chiang Mai", "Suvarnabhumi", "F00002"))
controller.add_flight_list(Flight("Suvarnabhumi", "Hat Yai", "F00003"))
controller.add_flight_list(Flight("Hat Yai", "Suvarnabhumi", "F00004"))
controller.add_flight_list(Flight("Suvarnabhumi", "Khon Kaen", "F00005"))
controller.add_flight_list(Flight("Khon Kaen", "Suvarnabhumi", "F00006"))
controller.add_flight_list(Flight("Chiang Mai", "Hat Yai", "F00007"))
controller.add_flight_list(Flight("Hat Yai", "Chiang Mai", "F00008"))
controller.add_flight_list(Flight("Chiang Mai", "Khon Kaen", "F00009"))
controller.add_flight_list(Flight("Khon Kaen", "Chiang Mai", "F00010"))
controller.add_flight_list(Flight("Hat Yai", "Khon Kaen", "F00011"))
controller.add_flight_list(Flight("Khon Kaen", "Hat Yai", "F00012"))

for number in range(1, 12, 2):
    for day in range(1,31):

        flight_no = f"F{number:05d}"
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 6, 40, 0), datetime(2024, 4, day, 8, 5, 0), "A00001")
        controller.set_seat_price(flight_instance_no, 1100)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 9, 0, 0), datetime(2024, 4, day, 10, 20, 0), "A00002")
        controller.set_seat_price(flight_instance_no, 1300)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 11, 35, 0), datetime(2024, 4, day, 12, 50, 0), "A00003")
        controller.set_seat_price(flight_instance_no, 1500)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 14, 45, 0), datetime(2024, 4, day, 16, 5, 0), "A00004")
        controller.set_seat_price(flight_instance_no, 1400)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 19, 35, 0), datetime(2024, 4, day, 21, 00, 0), "A00005")
        controller.set_seat_price(flight_instance_no, 1200)

        flight_no = f"F{number + 1 :05d}"

        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 9, 35, 0), datetime(2024, 4, day, 11, 0, 0), "A00001")
        controller.set_seat_price(flight_instance_no, 1100)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 11, 50, 0), datetime(2024, 4, day, 13, 10, 0), "A00002")
        controller.set_seat_price(flight_instance_no, 1300)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 14, 20, 0), datetime(2024, 4, day, 15, 35, 0), "A00003")
        controller.set_seat_price(flight_instance_no, 1500)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 17, 35, 0), datetime(2024, 4, day, 18, 55, 0), "A00004")
        controller.set_seat_price(flight_instance_no, 1400)
        flight_instance_no = controller.add_flight_instance_list(flight_no,datetime(2024, 4, day, 22, 30, 0), datetime(2024, 4, day, 23, 55, 0), "A00005")
        controller.set_seat_price(flight_instance_no, 1200)

# controller.register("Peerawat Ingkhasantatikul", "66011442@kmitl.ac.th", "123456789", "0812895077", "KMITL", "2004-08-12")

controller.add_user(User("Sataporn", "earn@gmail.com", controller.hash_password("yHh31t0!"), "0123456789", "KMITL", "2005-04-01")) #U00001
controller.add_user(User("Issaree", "little@gmail.com", controller.hash_password("1t+Mb880"), "0987612345", "KMITL", "2005-05-01")) #U00002
controller.add_user(User("Supakarn", "third@gmail.com", controller.hash_password("391CUhr="), "0543216789", "KMITL", "2004-12-01")) #U00003
controller.add_user(User("Peerawat", "mark@gmail.com", controller.hash_password("1234"), "0987654321", "KMITL", "2004-03-01")) #U00004

controller.create_booking("U00001", "FI00001")
controller.fill_info("U00001", "FI00001", "B00001", "4A", "30kg", "male", "0812895077", "Supakarn Tantichawa-ochanon", "2004-08-12", "123456")
controller.fill_info("U00001", "FI00001", "B00001", "4B", "30kg", "male", "0812895077", "Peerawat aaa", "2004-08-12", "123456")
controller.booking_details("U00001", "B00001")

# controller.create_booking("U00003", "FI00001")
# controller.fill_info("U00001", "FI00001", "B00001", "4A", "30kg", "male", "0812895077", "Supakarn Tantichawa-ochanon", "2004-08-12", "123456")
# controller.fill_info("U00001", "FI00001", "B00001", "4B", "30kg", "male", "0812895077", "Peerawat aaa", "2004-08-12", "123456")
# controller.booking_details("U00001", "B00001")

# info = {
#     "card_holder_name": "Supakarn",
#     "card_no": "191",
#     "expiration_date": "2032-10-10",
#     "security_code": "123"
# }
# controller.pay("U00001","B00001",controller.booking_details("U00001", "B00001"),0, info)
