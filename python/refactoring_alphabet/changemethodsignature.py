from dataclasses import dataclass
from math import sqrt

# Task
# Change method signature to 
# def distance_from_beginning(point: Point) -> float:
# Do it in multiple steps in such a way that your tests NEVER fail

class CoordinateHelper:
    @staticmethod
    def distance_from_beginning(x: float, y: float) -> float:
        return sqrt(x*x + y*y)

@dataclass
class Point:
    x: float
    y: float
    
class CoordinateHelperAfter:
    @staticmethod
    def distance_from_beginning(point: Point) -> float:
        return sqrt(point.x*point.x + point.y*point.y)
    