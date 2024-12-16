import { writeFileSync } from 'fs';

export class InvoiceItemManager {
    saveItemTotalAmount(quantity: number, price: number, taxRate: number) {
        const total = quantity * price
        const tax = total * taxRate
        const totalWithTax = total + tax
        
        writeFileSync('invoice_items.csv', `${quantity};${price};${taxRate};${totalWithTax}\n`, { flag: 'a' });
    }
}

