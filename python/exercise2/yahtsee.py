from enum import Enum

class Category(Enum):
    ONES = 1

class Yahtsee(object):
    def score(self,category,values):
        return True