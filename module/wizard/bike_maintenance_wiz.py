from odoo import models , fields #type: ignore


class BikeMaintenance(models.Model):
    _name="bike.maintenancewiz"
    _description="Maintenanace Details"



    bike_id = fields.Many2one("bike.details", string = "Bike Name")
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
    




    def bike_add_to_maintenance(self):
        maintenance = self.env['bike.maintenance'].create({
            'bike_id': self.bike_id.id,
            'maintenance_type': self.maintenance_type,
            'maintenance_date': self.maintenance_date,
            'odometer_reading': self.odometer_reading,
            'cost': self.cost,
            'status': 'draft',
        })
    
        if self.car_id:
            self.car_id.maintenance_id = [(4, maintenance.id)]
    
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance',
            'res_model': 'bike.maintenance',
            'view_mode': 'form',
            'res_id': maintenance.id,
            'target': 'current',
        }
