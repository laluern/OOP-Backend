from .seat import Seat

class ReservedSeat(Seat):
    def __init__(self, row, column, seat_type):
        super().__init__(row, column, seat_type , None)