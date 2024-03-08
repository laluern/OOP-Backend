from datetime import datetime

from ..internal.controller import Controller
from ..internal.flight import Flight
from ..internal.airport import Airport
from ..internal.airplane import Airplane
from ..internal.promocode import Promocode

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

Promocode('A1000', 10, datetime(2029, 1, 1))
Promocode('A2000', 10, datetime(2029, 1, 1))
Promocode('A3000', 10, datetime(2029, 1, 1))
Promocode('B1000', 20, datetime(2029, 1, 1))
Promocode('B2000', 20, datetime(2029, 1, 1))
Promocode('B3000', 20, datetime(2029, 1, 1))
Promocode('C1000', 30, datetime(2029, 1, 1))
Promocode('C2000', 30, datetime(2029, 1, 1))
Promocode('C3000', 30, datetime(2029, 1, 1))

controller.add_flight_list(Flight("Suvarnabhumi", "Chiang Mai", "F00001"))
controller.add_flight_list(Flight("Chiang Mai", "Suvarnabhumi", "F00002"))
controller.add_flight_list(Flight("Suvarnabhumi", "Hat Yai", "F00003"))
controller.add_flight_list(Flight("Hat Yai", "Suvarnabhumi", "F00004"))
controller.add_flight_list(Flight("Suvarnabhumi", "Khon Kaen", "F00005"))
controller.add_flight_list(Flight("Khon Kaen", "Suvarnabhumi", "F00006"))

controller.add_flight_instance_list("F00001",datetime(2024, 4, 1, 9, 0, 0), datetime(2024, 4, 1, 10, 20, 0), "A00001", "1")
controller.set_seat_price("FI00001", 1000)
controller.add_flight_instance_list("F00002",datetime(2024, 4, 1, 11, 50, 0), datetime(2024, 4, 1, 13, 10, 0), "A00002", "1")
controller.set_seat_price("FI00002", 1200)
controller.add_flight_instance_list("F00001",datetime(2024, 4, 1, 14, 45, 0), datetime(2024, 4, 1, 16, 5, 0), "A00003", "1")
controller.set_seat_price("FI00003", 1200)
controller.add_flight_instance_list("F00002",datetime(2024, 4, 1, 17, 35, 0), datetime(2024, 4, 1, 18, 55, 0), "A00004", "1")
controller.set_seat_price("FI00004", 1400)
controller.add_flight_instance_list("F00001",datetime(2024, 4, 1, 19, 35, 0), datetime(2024, 4, 1, 20, 55, 0), "A00005", "1")
controller.set_seat_price("FI00005", 1100)
controller.add_flight_instance_list("F00002",datetime(2024, 4, 1, 22, 25, 0), datetime(2024, 4, 1, 23, 45, 0), "A00006", "1")
controller.set_seat_price("FI00006", 1300)