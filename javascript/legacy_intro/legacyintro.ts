import { writeFileSync } from 'fs';

export class InvoiceItemManager {
    saveItemTotalAmount(quantity: number, price: number, taxRate: number) {
        const total = quantity * price
        const tax = total * taxRate
        const totalWithTax = total + tax
        
        writeFileSync('invoice_items.csv', `${quantity};${price};${taxRate};${totalWithTax}\n`, { flag: 'a' });
    }
}

// After start
export class InvoiceItemManagerRefactored {
    saveItemTotalAmount(quantity: number, price: number, taxRate: number) {
        const totalWithTax = this.calculateTotal(quantity, price, taxRate)
        
        writeFileSync('invoice_items.csv', `${quantity};${price};${taxRate};${totalWithTax}\n`, { flag: 'a' });
    }

    calculateTotal(quantity, price, taxRate) {
        const total = quantity * price
        const tax = total * taxRate
        const totalWithTax = total + tax
        return totalWithTax
    }
}
// After end
