from odoo import models, fields, api #type: ignore



class BillsInvoice(models.Model):
    _inherit = 'account.move'



    bike_id = fields.Many2one("bike.details" , string="Bike Name")
    car_id = fields.Many2one("car.details" , string="Car Name")
    customer_id=fields.Many2one("customer.details", string="Customer")
    bill_date = fields.Date("Bill Date")
    payment_terms = fields.Selection([( 'end of the month' ,'End Of the Month'),
                                     ( 'periods of 2 months' ,'Periods of 2 Months'),
                                     ( 'daily charge' ,'Daily Charge')],
                                     "Payment Terms")
    street = fields.Char("Street")    
    street2 = fields.Char("Street2")
    city = fields.Char("City")
    payment_type=fields.Selection([('cash', 'Cash'),
                                   ('chack', 'Chack'),
                                   ('credit-card', 'Credit-Card')],
                                   "Payment Type")
    bill_pay = fields.Float(string="Bill Pay")
    add_tax = fields.Float(string="Add Tax", compute="compute_amount")
    total_amount = fields.Float(string="Total Amount", compute="compute_amount")
    


    @api.depends('add_tax','bill_pay','total_amount')
    def compute_amount(self):
        for record in self:
            record.add_tax =  (record.bill_pay * 0.10)
            record.total_amount = record.add_tax + record.bill_pay