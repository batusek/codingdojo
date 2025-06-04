    
    
class InvoiceRun:
    def run(self, year: int, month: int):
        for invoice in self.get_invoices(year,month):
            self.process_invoice(invoice)
            print(f"Invoice {invoice} created")
            
            
class InvoiceRun:
    def run(self, year: int, month: int):
        f = open("output.html","w")
        f.write("<html><body>\n")
        f.write('<table border="1">\n')
        f.write("<tr><th>Invoice No</th><th>Amount</th></tr>")
        
        for invoice in self.get_invoices(year,month):
            self.process_invoice(invoice)
            f.write("<tr>\n")
            f.write(f'<td>{invoice.id}</td>')
            f.write(f'<td>{invoice.amount}</td>')
            f.write("</tr>\n")

        f.write("</tr></table>\n")
        f.write("</body></html>\n")
        f.close()


class InvoiceRunObserver:
    def start(self):
        
    def end(self):
        
    def observe_invoice(invoice:Invoice):

class InvoiceRun:
    def __init__(self, observer: InvoiceRunObserver):
        self.observer = observer
        
    def run(self, year: int, month: int):
        observer.start()
        for invoice in self.get_invoices(year,month):
            self.process_invoice(invoice)
            observer.observe_invoice(invoice)
        observer.end()

class PrintObserver(InvoiceRunObserver):
    def start(self):
        print("Invoice run started")
        
    def end(self):
        print("Invoice run finished")
        
    def observe_invoice(invoice:Invoice):
        print(f"Invoice {invoice} created")
    
    
class PrintObserver(InvoiceRunObserver):
    def start(self):
        self.f = open("output.html","w")
        self.f.write("<html><body>\n")
        self.f.write('<table border="1">\n')
        self.f.write("<tr><th>Invoice No</th><th>Amount</th></tr>")
        
    def end(self):
        self.f.write("</tr></table>\n")
        self.f.write("</body></html>\n")
        self.f.close()
        
    def observe_invoice(invoice:Invoice):
        self.f.write("<tr>\n")
        self.f.write(f'<td>{invoice.id}</td>')
        self.f.write(f'<td>{invoice.amount}</td>')
        self.f.write("</tr>\n")
    
