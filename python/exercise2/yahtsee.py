from enum import Enum

class Category(Enum):
    ONES = 1

class Yahtsee(object):
    def ones(self,values):
        sum = 0
        for v in values:
            if v==1:
                sum += 1

        return sum

    def score(self,category,values):
        switcher={
            Category.ONES:self.ones
        }
        func = switcher.get(category,lambda:None)
        return func(values)