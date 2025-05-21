from odoo import models, fields # type: ignore

class PaymentWizard(models.TransientModel):
    _name = "invoice.wizard"
    _description = "Payment Wizard"

    member_id = fields.Many2one("customer.details", string="Customer", required=True)

    start_date = fields.Date("Start Date", required=True)
    end_date = fields.Date("End Date", required=True)
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    vehicle_available = fields.Many2one("car.details", string="Select Car", required=True, store = True)

    def create_invoice(self):
        invoice = self.env['account.move'].create({
            'customer_id': self.member_id.id,
            'car_id' : self.vehicle_available.id,
            'street' : self.street,
            'street2' : self.street2,
            'city' : self.city,
            
        })

        self.member_id.bills_id = [(4, invoice.id)]

        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': invoice.id,
            'target': 'current',
        }
