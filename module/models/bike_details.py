from odoo import models, fields, api #type:ignore


class Bikedetails(models.Model):
    _name="bike.details"
    _description="This model contains details about bikes renating"



    name = fields.Char(string="Bike Name")
    model= fields.Integer(string="Model Year")
    image=fields.Binary(string="Image")
    bike_type= fields.Selection([('sports', 'Sports'),
                                 ('caferacer', 'Caferacer'),
                                 ('electric', 'Electric'),
                                 ('off-road', 'Off-road'),
                                 ('standard', 'Standard')],
                                 string="Bike Type", default="sports")
    bike_maintenance = fields.Selection([('under_maintenance', 'Under Maintenance'),
                                         ],"Maintenance Status")
    
    bike_available = fields.Selection([('booked', 'Booked'),
                                       ('unbooked', 'Unbooked'),],
                                       "Available") 
    
    book_date = fields.Date("Booking Date")
    end_date = fields.Date("Bike Return Date")
    # country_id=fields.Many2one("res.country", string="country")
    # phone=fields.Char("Phone")



    rent_hour = fields.Float("Rent / Hour")
    rent_day = fields.Float("Rent / Day")
    rent_week = fields.Float("Rent / Week")
    rent_month = fields.Float("Rent / Month")
    rent_year = fields.Float("Rent / Year")
    rent_kilometer = fields.Float("Rent / Kilometer")
    rent_mile = fields.Float("Rent / Mile")

    charge_hour = fields.Float("Charge / Hour")
    charge_day = fields.Float("Charge / Day")
    charge_week = fields.Float("Charge / Week")
    charge_month = fields.Float("Charge / Month")
    charge_year = fields.Float("Charge / Year")
    charge_kilometer = fields.Float("Charge / Kilometer")
    charge_mile = fields.Float("Charge / Mile")

    #bike details

    chassis_number = fields.Char("Chassis Number")
    description = fields.Text("Note")

    
    def action_open_maintenance_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Wizard',
            'res_model': 'maintenance.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context' : {
                'default_'
            }
        }
    


    
    # @api.onchange('country_id')
    # def _onchange_country_id(self):
    #     if self.country_id and self.country_id.phone_code:
    #         self.phone = f"+{self.country_id.phone_code} "
