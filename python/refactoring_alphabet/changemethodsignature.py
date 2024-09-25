from dataclasses import dataclass
from math import sqrt

# TODO: Change method signature to 
# def distance_from_beginning(point: Point) -> float:
# Do it in _multiple_ steps in such a way that your tests NEVER fail

class CoordinateHelper:
    @staticmethod
    def distance_from_beginning(x: float, y: float) -> float:
        return sqrt(x*x + y*y)


