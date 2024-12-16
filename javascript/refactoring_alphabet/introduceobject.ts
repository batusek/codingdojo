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
  
  // After start
  export class ShippingParams {
    constructor(public weight: number, public distance: number) {}
  }
  
  export class CostCalculatorAfter {
    calculateShippingCost(params: ShippingParams): number {
      let baseCost;

      if (params.weight > 10) {
        baseCost = 10;
      } else {
        baseCost = 5;
      }
      const costPerMile = 0.1;
      const totalCost = baseCost + (params.distance * costPerMile);
      return totalCost;
    }
  }
  // After end