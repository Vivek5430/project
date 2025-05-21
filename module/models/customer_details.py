from odoo import models, fields,api# type: ignore
from odoo.exceptions import UserError #type: ignore


class Customer(models.Model):
    _name = "customer.details"
    _description = "Customer Details"

    
    name = fields.Char("Name")
    image = fields.Binary(string="Image")
    email = fields.Char("Email")
    language = fields.Selection([('english', 'English'),
                                ('hindi', 'Hindi'),
                                ('french', 'French')],
                                "Language")
    phone = fields.Char("Phone")
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    driving_license = fields.Char("Driving License")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    rental_status = fields.Selection([
        ('active', 'Active Rental'),
        ('past', 'Past Customer')
    ], default='past')
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    rental_count = fields.Integer("Rental Count", default=0)




    vehicle_available = fields.Many2one("car.details" , string = "Select Car")
    bills_id = fields.One2many("account.move", "customer_id", string="Bills")
    


    
    def action_open_invoice_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'invoice.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_member_id': self.id,
                'default_start_date': self.start_date,
                'default_end_date': self.end_date,
                'default_street': self.street,
                'default_street2': self.street2,
                'default_city': self.city,
                'default_vehical_available': self.vehicle_available.id,
            }
        }

    @api.onchange('vehicle_available')
    def _onchange_vehicle_available(self):
        if self._origin and self._origin.vehicle_available != self.vehicle_available:

            if self._origin.vehicle_available:
                self._origin.vehicle_available.status = "unbooked"

            if self.vehicle_available:
                self.vehicle_available.status = "booked"
            


    def create(self, vals):
        record = super().create(vals)
        if record.vehicle_available:
            record.vehicle_available.status = "booked"
        return record

    def write(self, vals):
        for rec in self:
            old_vehicle = rec.vehicle_available
            res = super().write(vals)
            if 'vehicle_available' in vals:
                new_vehicle = rec.vehicle_available
                if old_vehicle and old_vehicle != new_vehicle:
                    old_vehicle.status = "unbooked"
                if new_vehicle:
                    new_vehicle.status = "booked"
        return res
        

    @api.onchange('vehicle_available')
    def _onchange_vehicle_available(self):
        if self.vehicle_available  and self.vehicle_available.status == 'under_maintenance':
            self.vehicle_available= False
            
            return{
                'warning' : {
                    'title' : "Car Not Avilable",
                    'message' : "This car is curruntly not avilable. Please select anothere Car",
                }
            }

    @api.model    
    def create(self,vals):
        car = self.env['car.details'].browse(vals.get('vehicle_available'))
        if car.status == "under_maintenance" :
            raise UserError("You cannot book a car that is under manintenance")
        return super().create(vals)
    


    def write(self,vals):
        if 'vehicle_available' in vals:
            car = self.env['car.details'].browse(vals.get('vehicle_available'))
            if car.status == "under_maintenance":
                raise UserError("You cannot book a car that is under manintenance")
            return super().write(vals)

