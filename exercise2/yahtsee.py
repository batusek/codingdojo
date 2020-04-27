from enum import Enum
import collections

class Category(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    PAIR = 7
    TWOPAIRS = 8
    THREEOFAKIND = 9
    FOUROFAKIND = 10
    SMALL = 11
    LARGE = 12
    YAHTSEE = 13

class Numbers(object):
    def __init__(self,num):
        self.num = num
    
    def score(self,values):
        sum = 0
        for v in values:
            if v==self.num:
                sum += self.num

        return sum

class Kind(object):
    def __init__(self,num):
        self.num = num
    
    def score(self,values):
        frequencies = collections.Counter(values)
        result = 0
        for key in frequencies:                
            if frequencies[key]>=self.num:
                result += self.num*key
        return result


class Sequence(object):
    def __init__(self,len,value):
        self.len = len
        self.value = value
    
    def score(self,values):
        values.sort()
        last = values[0]
        sequencelen = 1
        for v in values[1:]:
            if v==last+1:
                sequencelen += 1
            last = v

        return self.value if sequencelen>=self.len else 0



class Yahtsee(object):
    def score(self,category,values):
        def pair(values):
            values.sort(reverse=True)
            for v in zip(values[:-1],values[1:]):
                if v[0]==v[1]:
                    return 2*v[0]

            return 0

        def twopairs(values):
            frequencies = collections.Counter(values)
            result = 0
            pairs = 0
            for key in frequencies:
                if frequencies[key]>=2:
                    result += 2*key
                    pairs += 1
            return result if pairs==2 else 0

        def yahtsee(values):
            score = Kind(5).score(values)
            return 50 if score>0 else 0

        switcher={
            Category.ONES:Numbers(1).score,
            Category.TWOS:Numbers(2).score,
            Category.THREES:Numbers(3).score,
            Category.FOURS:Numbers(4).score,
            Category.FIVES:Numbers(5).score,
            Category.SIXES:Numbers(6).score,
            Category.PAIR:pair,
            Category.TWOPAIRS:twopairs,
            Category.THREEOFAKIND:Kind(3).score,
            Category.FOUROFAKIND:Kind(4).score,
            Category.SMALL:Sequence(4,30).score,            
            Category.LARGE:Sequence(5,40).score,            
            Category.YAHTSEE:yahtsee,
        }
        func = switcher.get(category,lambda values:None)
        return func(values)