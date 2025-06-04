import { appendFileSync } from 'fs';

export class InvoiceItemManager {
    saveItemTotalAmount(quantity: number, price: number, taxRate: number): void {
      const total = quantity * price;
      const tax = total * taxRate;
      const totalWithTax = total + tax;
  
      const line = `${quantity};${price};${taxRate};${totalWithTax}\n`;
      appendFileSync('invoice_items.csv', line);
    }
  
  }
  
  // After start
  export class InvoiceItemManagerWithIsolatedSideEffect {
    saveItemTotalAmount(quantity: number, price: number, taxRate: number): void {
      const total = quantity * price;
      const tax = total * taxRate;
      const totalWithTax = total + tax;
  
      const line = `${quantity};${price};${taxRate};${totalWithTax}\n`;
      this.save(line);
    }
  
    protected save(line: string): void {
      appendFileSync('invoice_items.csv', line);
    }
  }
  // After end