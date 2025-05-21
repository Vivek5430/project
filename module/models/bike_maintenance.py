from odoo import models ,fields #type: ignore


class BikeMaintenance(models.Model):
    _name="bike.maintenance"
    _description = "Bike Maintenance Details"


    bike_id = fields.Many2one("bike.details", string="Bike Name")
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
        bike = self.env['bike.details'].browse(vals.get('bike_id'))
        if bike:
            bike.status = "under_maintenance"

        return super().create(vals)
    

    def write(self,vals):
        res = super().write(vals)
        if 'bike_id' in vals:
            for rec in self:
                rec.bike_id.status = "under_maintenance"

        return res        
