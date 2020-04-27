from enum import Enum

class Category(Enum):
    ONES = 1
    TWOS = 2

class Numbers(object):
    def __init__(self,num):
        self.num = num
    
    def score(self,values):
        sum = 0
        for v in values:
            if v==self.num:
                sum += self.num

        return sum


class Yahtsee(object):
    def score(self,category,values):
        switcher={
            Category.ONES:Numbers(1).score,
            Category.TWOS:Numbers(2).score
        }
        func = switcher.get(category,lambda:None)
        return func(values)