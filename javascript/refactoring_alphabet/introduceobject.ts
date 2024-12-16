// TODO: introduce an enclosing class for weight and distance

export class CostCalculator {
    calculateShippingCost(weight: number, distance: number): number {
      let baseCost;

      if (weight > 10) {
        baseCost = 10;
      } else {
        baseCost = 5;
      }
      const costPerMile = 0.1;
      const totalCost = baseCost + (distance * costPerMile);
      return totalCost;
    }
  }
  
