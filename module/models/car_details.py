from odoo import models, fields,api # type: ignore
from odoo import http
from odoo.http import request
import json


class CarDetails(models.Model):
    _name = "car.details"
    _description = "Car Details"


    name = fields.Char(string="Car Name", required=True)
    model = fields.Integer("Car Model")
    image = fields.Binary(string="image")    
    car_type = fields.Selection([('sedan' , 'Sedan'),
                                     ('suv', 'Suv'),
                                     ('hatchback','Hatcback'),
                                     ('luxury','Luxury'),
                                     ('sports' , 'Sports')],
                                     "Car Type")
    fuel_type = fields.Selection([('petrol','Petrol'),
                                  ('desiel','Desiel'),
                                  ('cng','CNG')],
                                  "Fuel_Type")
    
    maintenance_status = fields.Selection([('under_maintenance','Under Maintenance'),],
                                          "Maintenance Status")

    available = fields.Selection([('booked', 'Booked'),
                              ('unbooked', 'Unbooked'),
                              ],
                              "Available")
    
    start_date = fields.Date("Booking Date")
    end_date = fields.Date("Car Return Date")
    

    status = fields.Selection([('unbooked', 'Unbooked'),
                               ('booked', 'Booked'),
                               ('under_maintenance' , 'Under Maintenance'),],
                               "Status", default='unbooked')
    
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


    #model

    model = fields.Text("Model")
    model_year = fields.Char("Model Year")
    transmission = fields.Selection([('automatic' , 'Automatic'),
                                     ('manual' , 'Manual')],
                                     "Transmission")
    color = fields.Char("Car Color")
    seats = fields.Integer("Seats Numbers")
    doors = fields.Integer("Doors Numbers")

    #Engine details

    power_unit = fields.Selection([
        ('power', 'kW'),
        ('horsepower', 'Horsepower')
        ], 'Power Unit', default='power', required=True)
    

    description = fields.Text("Note")


    #vehical details

    order_date = fields.Date("Order Date")
    registration_date = fields.Date("Registration Date")
    cancellation_date = fields.Date("Cancellation Date")
    chassis_number = fields.Integer("Chassis Number")
    
    maintenance_id = fields.One2many("car.maintenance" , "car_id" , string = "Maintenance")



    def action_open_maintenance_wizard(self):
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'maintenance.wizard',
        'view_mode': 'form',
        'target': 'new',  
        'context': {
            'default_car_id': self.id,
        }
    }


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = vals.get('name', '').title() 
        return super().create(vals_list)
    


class CarDetailsController(http.Controller):

    @http.route('/api/a', type='json', auth='public', csrf=False)
    def create_car(self, **kwargs):
        print(kwargs)
        try:
            car = request.env['car.details'].sudo().create(kwargs)
            return {
                'success': True,
                'car_id': car.id,
                'message': 'Car created successfully.'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


