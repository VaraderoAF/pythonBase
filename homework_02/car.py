"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base


class Car(base.Vehicle):
    engine = object

    def set_engine(self, motor):
        self.engine = motor

