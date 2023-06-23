from person import Person
from typing import List

class Car:

    def __init__(self, name:str, year:int, seats:int, ps:int) -> None:
        self.name = name
        self.year = year
        self.seats = seats
        self.ps = ps
        # we could also use a dictionary here, so we could save a seat to person mapping
        self.passengers = []

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) - {self.ps} PS"
    
    def add_passenger(self, passenger:Person) -> None:
        if len(self.passengers) < self.seats:
            self.passengers.append(passenger)
            print(f"{passenger} is now registered for driving in {self.name}")
        else:
            print(f"List of passengers for {self.name} is full!")
    
    def remove_passenger(self, passenger:Person) -> None:
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger} is now unregistered for driving in {self.name}")
        elif len(self.passengers) == 0:
            print(f"List of passengers for {self.name} is empty!")
        else:
            print(f"{passenger} is not registered for driving in {self.name}")
    
    def get_passengers(self) -> List[str]:
        return [str(passenger) for passenger in self.passengers]
    
    def start_ride(self) -> None:
        if len(self.passengers) == self.seats:
            print(f"Starting ride with {self.get_passengers()}.")
        else:
            print(f"Can't start ride with {self.get_passengers()}, because car is not full.")
    
    def add_multiple_passengers(self, passengers:List[Person]) -> None:
        for passenger in passengers:
            self.add_passenger(passenger)
    
    def remove_multiple_passengers(self, passengers:List[Person]) -> None:
        for passenger in passengers:
            self.remove_passenger(passenger)