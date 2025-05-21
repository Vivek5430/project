# from odoo import models, fields, api #type: ignore
# # from odoo.exceptions import UserError 



# class Booking(models.TransientModel):
#     _name = "booking.wizard"
#     _description = "Booking Wizard"



#     car_id = fields.Many2one("car.details" , string = "Select Car")

#     @api.onchange('car_id')
#     def _onchange_car_id(self):
#         if self.car_id and self.car_id.status == 'under_maintenance':
#             return{
#                 'warning': {
#                     'title' : "Car in Maintenance",
#                     'message' : "The Selected car is curruntly in Under Maintenanace. Please choose any Other Car."
#                 }
#             }

