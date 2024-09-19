class CostCalculator:
    def calculate_shipping_cost(self,weight, distance) -> float:
        if weight > 10:
            base_cost = 10
        else:
            base_cost = 5
        cost_per_mile = 0.1
        total_cost = base_cost + (distance * cost_per_mile)
        return total_cost 
    
#After
class ShippingParams:
    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

        
class CostCalculatorA:
    def calculate_shipping_cost(params: ShippingParams) -> float:
        if params.weight > 10:
            base_cost = 10
        else:
            base_cost = 5
        cost_per_mile = 0.1
        total_cost = base_cost + (params.distance * cost_per_mile)
        return total_cost        
