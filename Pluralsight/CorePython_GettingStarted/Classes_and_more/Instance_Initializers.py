"""Model for aircraft flights"""

class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid rout number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
    
    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger,
        
        Args:
            seat: A seat designated such as '12C'or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1] # seat = whole string but the last character 21A -> 21
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")
        
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} alredy occupied")
        
        self._seating[row][letter] = passenger

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_rows = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJ"[:self._num_seats_per_rows])
    

from Instance_Initializers import *

# a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
# print(a.registration())
# print(a.model())
# print(a.seating_plan())

f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
print(f.aircraft_model())

# from pprint import pprint as pp

# pp(f._seating)

f.allocate_seat("12A", "Fulano Jack")
f.allocate_seat("12A", "Ciclano Jack")