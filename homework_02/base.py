from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    is_parent = True
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        if distance > 0:
            fuel_loss = self.fuel_consumption * distance
            if self.fuel < fuel_loss:
                raise exceptions.NotEnoughFuel
            else:
                self.fuel = self.fuel - fuel_loss
