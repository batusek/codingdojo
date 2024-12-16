export class Item {
    constructor(public price: number, public quantity: number, public isTaxable: boolean) {}
}
  
export class PriceCalculator {
    constructor(public taxRate: number) {}
  
    calculateTotalPrice(items: Item[]): number {
      // TODO: extract method for calculating tax
      let total = 0;
      for (const item of items) {
        total += item.price * item.quantity;
        if (item.isTaxable) {
          total += item.price * item.quantity * this.taxRate;
        }
      }
      return total;
    }
  }
  
  // After start
  export class PriceCalculatorAfter {
    constructor(public taxRate: number) {}
  
    calculateTotalPrice(items: Item[]): number {
      let total = 0;
      for (const item of items) {
        total += item.price * item.quantity;
        total += this.calculateTax(item);
      }
      return total;
    }
  
    calculateTax(item: Item): number {
      if (item.isTaxable) {
        return item.price * item.quantity * this.taxRate;
      } else {
        return 0;
      }
    }
  }
  // After end