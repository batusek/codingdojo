class InvoiceItemManager:
    def save_item_total_amount(self, quantity: float, price: float, tax_rate: float) -> None:
        total = quantity * price
        tax = total * tax_rate
        total_with_tax = total + tax
        
        with open("invoice_items.csv", "a") as f:
            f.write(f"{quantity};{price};{tax_rate};{total_with_tax}\n")
            
