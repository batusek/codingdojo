
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
    
