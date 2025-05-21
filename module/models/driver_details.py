from odoo import models, fields #type: ignore


class Driverdetails(models.Model):
    _name = "driver.details"
    _description = "Driver Details"


    name = fields.Char("Name")
    image = fields.Binary(string="Image")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    language = fields.Selection([('english', 'English'),
                                 ('hindi', 'Hindi'),
                                 ('french', 'French')],
                                 "Language")
    driving_license = fields.Char("Driving License")
    address = fields.Text("Address")
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('other','Other')],
                               "Gender")
    age = fields.Integer("Age")
    date_of_birth = fields.Date("Date of Birth")
    country = fields.Char("Country")
        


    def action_view_driver(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Driver',
            'res_model': 'driver.details',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
