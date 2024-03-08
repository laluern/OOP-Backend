from app.database.database import controller

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.router.router:app", host="127.0.0.1", port=8000, log_level="info")



#############################################################################################
    
# # TODO get seat data
# print(controller.get_seat_data("FI00003"))

# TODO seacrh flgiht
# print(controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1))
# print(controller.search_flight("Chiang Mai", "Suvarnabhumi", "2024-04-01", 1))
# print(controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1, "A1000"))

# TODO sort flight
# flight_list = controller.search_flight("Suvarnabhumi", "Chiang Mai", "2024-04-01", 1)
# print("Cheapest")
# print(controller.sort_flight(flight_list, "Cheapest"))
# print("Fastest")
# print(controller.sort_flight(flight_list, "Fastest"))
# print("Earliest")
# print(controller.sort_flight(flight_list, "Earliest"))
