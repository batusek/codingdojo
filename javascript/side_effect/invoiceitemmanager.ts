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
  
