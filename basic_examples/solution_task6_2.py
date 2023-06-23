from abc import ABC, abstractmethod
from typing import Tuple, List

# use class Car if you want to create instance of the Car object
class Car(ABC):

    def __init__(self, model:str, release:int, ps:int, company:str) -> None:
        self.model = model
        self.release = release
        self.ps = ps
        self.company = company
        self.started = False
        self.users: List[str] = []
    
    def __str__(self) -> str:
        return f"{self.company} {self.model} ({self.release}) - {self.ps} PS"
    
    def start(self) -> None:
        if not self.started:
            print(f"{self.model} started!")
            self.started = True
        else:
            print(f"{self.model} already started!")
    
    def stop(self) -> None:
        if self.started:
            print(f"{self.model} stopped!")
            self.started = False
        else:
            print(f"{self.model} already stopped!")
    
    def add_user(self, user:str) -> None:
        if len(self.users) < 3:
            self.users.append(user)
            print(f"{user} is now registered for driving {self.model}")
        else:
            print(f"List of users for {self.model} is full!")
    
    @abstractmethod
    def fuel(self):
        pass

class ElectricCar(Car):

    def __init__(self, model: str, release: int, ps: int, company: str, capacity:float, status:float) -> None:
        super().__init__(model, release, ps, company)
        self.capacity = capacity
        self.status = status
    
    # fuel = charge in our use case
    def fuel(self, volume:float) -> None:
        if self.status + volume <= self.capacity:
            self.status += volume
            print(f"{self.model} charged with {volume} kWh")
        else:
            print(f"{self.model} can't be charged with {volume} kWh")
    
    def drive(self, consumption:float) -> None:
        if self.started:
            if self.status - consumption >= 0:
                self.status -= consumption
                print(f"{self.model} drove {consumption} kWh")
            else:
                print(f"{self.model} can't drive {consumption} kWh")
        else:
            print(f"{self.model} must be started first!")
    
class HybridCar(Car): 

    def __init__(self, model: str, release: int, ps: int, company: str, capacity_elec:float, capacity_organic:float, status:Tuple[float, float]) -> None:
        super().__init__(model, release, ps, company)
        self.capacity_elec = capacity_elec
        self.capacity_organic = capacity_organic
        self.status = status
    
    def fuel(self, amount:Tuple[float, float]) -> None:
        if self.status[0] + amount[0] <= self.capacity_elec and self.status[1] + amount[1] <= self.capacity_organic:
            self.status = (self.status[0] + amount[0], self.status[1] + amount[1])
            print(f"{self.model} charged/fueled with {amount[0]} kWh and {amount[1]} l")
        else:
            print(f"{self.model} can't be charged/fueled with {amount[0]} kWh and {amount[1]} l")

    
    def drive(self, consumption:Tuple[float, float]) -> None:
        if self.started:
            if self.status[0] - consumption[0] >= 0 and self.status[1] - consumption[1] >= 0:
                self.status = (self.status[0] - consumption[0], self.status[1] - consumption[1])
                print(f"{self.model} drove {consumption[0]} kWh and {consumption[1]} l")
            else:
                print(f"{self.model} can't drive {consumption[0]} kWh and {consumption[1]} l")
        else:
            print(f"{self.model} must be started first!")


def main():
    electric_car = ElectricCar("Model X", 2022, 500, "Tesla", 1000, 100)
    hybrid_car = HybridCar("A3 hybrid", 2021, 150, "Audi", 100, 40, (10, 10))

    # fist test the print out of both cars:
    print(electric_car)
    print(hybrid_car)
    # try to fuel the cars with valid input:
    electric_car.fuel(100)
    hybrid_car.fuel((20, 20))
    # try to overfuel the cars:
    electric_car.fuel(1000)
    hybrid_car.fuel((100, 100))
    # start the cars:
    electric_car.start()
    hybrid_car.start()
    # drive the cars:
    electric_car.drive(100)
    hybrid_car.drive((10, 10))
    # stop the cars:
    electric_car.stop()
    hybrid_car.stop()
    # try to drive again:
    electric_car.drive(100)
    hybrid_car.drive((10, 10))
    # add users to the cars:
    electric_car.add_user("Max")
    electric_car.add_user("Leonie")
    hybrid_car.add_user("Jürgen")
    hybrid_car.add_user("Lisa")
    electric_car.add_user("Hans")
    hybrid_car.add_user("Klaus")
    # try to add more users:
    electric_car.add_user("Hans")
    hybrid_car.add_user("Klaus")


if __name__ == "__main__":
    main()
        
    

