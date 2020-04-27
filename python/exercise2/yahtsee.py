from enum import Enum

class Category(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    PAIR = 7

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
        def pair(values):
            values.sort(reverse=True)
            for v in zip(values[:-1],values[1:]):
                if v[0]==v[1]:
                    return 2*v[0]

            return 0

        switcher={
            Category.ONES:Numbers(1).score,
            Category.TWOS:Numbers(2).score,
            Category.THREES:Numbers(3).score,
            Category.FOURS:Numbers(4).score,
            Category.FIVES:Numbers(5).score,
            Category.SIXES:Numbers(6).score,
            Category.PAIR:pair
        }
        func = switcher.get(category,lambda values:None)
        return func(values)