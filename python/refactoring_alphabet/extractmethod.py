
from dataclasses import dataclass


@dataclass
class Item:
    price: float
    quantity: int
    is_taxable: bool
    

class PriceCalculator:
    def __init__(self, taxRate: float):
        self.taxRate = taxRate
    
    def calculate_total_price(self, items: list[Item]):
        # TODO: extract method for calculating tax
        total: float = 0
        for item in items:
            total += item.price * item.quantity
            if item.is_taxable:
                total += item.price * item.quantity * self.taxRate
        return total    
    
# After start
class PriceCalculatorAfter:
    def __init__(self, taxRate: float):
        self.taxRate = taxRate
    
    def calculate_total_price(self, items: list[Item]):
        total = 0
        for item in items:
            total += item.price * item.quantity
            total += self.calculate_tax(item)
        return total

    def calculate_tax(self, item: Item):
        if item.is_taxable:
            return item.price * item.quantity * self.taxRate
        else:
            return 0
# After end