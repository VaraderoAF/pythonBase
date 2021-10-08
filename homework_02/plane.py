"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base, exceptions


class Plane(base.Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        if (self.cargo + load) <= self.max_cargo:
            self.cargo = self.cargo + load
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_removed = self.cargo
        self.cargo = 0
        return cargo_removed
