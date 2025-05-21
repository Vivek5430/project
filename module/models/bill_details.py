from odoo import models, fields, api #type: ignore


class Bill(models.Model):
    _name = "bills.details"  
    _description = "Bill Details"


    
    customer_bill_id = fields.Many2one("customer.details", "Vender")
    bill_date = fields.Date("Bill Date")
    payment_type = fields.Selection([('cash' , 'Cash'),
                                     ('Chack' , 'Chack'),
                                     ('credit-card' , 'Credit-card'),
                                     ( 'online-payment','Online-Payment')],
                                     "Payment")
    
    payment_terms = fields.Selection([( 'end of the month' ,'End Of the Month'),
                                     ( 'periods of 2 months' ,'Periods of 2 Months'),
                                     ( 'daily charge' ,'Daily Charge')],
                                     "Payment Terms")
    
    status = fields.Selection([('draft' , 'Draft'),
                               ('paid' , 'Paid')],
                               "Status" , default = "draft")
    
    street = fields.Char("Street")
    street2 = fields.Char("Street 2")
    city = fields.Char("City")
    distence = fields.Float("Enter KM") 
    rent_per_km = fields.Float("Rent Per KM") 
    bill_pay = fields.Float(string="Bill pay")
    add_tax = fields.Float(string = "Add Tax", compute= 'compute_amount')
    total_amount = fields.Float(string= "Total Amount", compute = 'compute_amount')
    driver_id = fields.Many2one("driver.details" , string = "Driver Name")
    customer_id = fields.Many2one("customer.details" , string = "Customer Name")
    vehicle_available = fields.Many2one("car.details" , string = "Select Car")


    @api.depends('add_tax','bill_pay','total_amount')
    def compute_amount(self):
        for record in self:
            record.add_tax =  (record.bill_pay * 0.10)
            record.total_amount = record.add_tax + record.bill_pay



    sequence_number = fields.Char(string = "Sequence Number", readonly = True, index = True, copy = False , default = 'INV/00')

    @api.model
    def create(self, vals):
        if vals.get('sequence_number' , 'New') == 'New':
            vals['sequence_number'] = self.env['ir.sequence'] .next_by_code('bills.details') 
            return super(Bill,self).create(vals)
        

    def copy(self, default = None):
        default = dict(default or {})   
        default.update({'sequence_number' : 'New'})
        return super(Bill,self) .copy(default)    



    


