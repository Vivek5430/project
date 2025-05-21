from odoo import models, fields #type: ignore



class Maintenance(models.TransientModel):
    _name = "maintenance.wizard"
    _description = "Maintenance Details"



    car_id = fields.Many2one("car.details" , string = "Car Name")  
    maintenance_type = fields.Selection([('service' , 'Service'),
                                         ('repair' , 'Repair'),
                                         ('painting' , 'Painting')],
                                         string = "Maintenance Type")
    maintenance_date = fields.Date("Maintenance Date")
    odometer_reading = fields.Float("Odometer Reading")
    cost = fields.Float("Cost")
    status = fields.Selection([('draft' , 'Draft'),
                               ('completed' , 'Completed')],
                               string = "Status" , default = "draft")
        



    def add_to_maintenance(self):
        maintenance = self.env['car.maintenance'].create({
            'car_id' : self.car_id.id,
            'maintenance_type': self.maintenance_type,
            'maintenance_date': self.maintenance_date,
            'odometer_reading': self.odometer_reading,
            'cost': self.cost,
            'status': 'draft',

        })  

        self.car_id.maintenance_id = [(4, maintenance.id)]

        return {

            'type' : 'ir.actions.act_window',
            'name' : 'Maintenance',
            'res_model' : 'car.maintenance',
            'view_mode' : 'form',
            'res_id' : maintenance.id,
            'target' : 'current',
        }  