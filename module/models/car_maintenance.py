from odoo import models , fields #type: ignore


class CarMaintenance(models.Model):
    _name = "car.maintenance"
    _description = "Car Maintenance Details"



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



    def create(self,vals):
        car = self.env['car.details'].browse(vals.get('car_id'))
        if car:
            car.status = "under_maintenance"

        return super().create(vals)
    
    def write(self,vals):
        res = super().write(vals)
        if 'car_id' in vals:
            for rec in self:
                rec.car_id.status = "under_maintenance"
    
        return res


