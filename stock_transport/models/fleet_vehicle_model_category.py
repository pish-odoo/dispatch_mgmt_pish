from odoo import models, fields, api



class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (kg)")
    max_volume = fields.Float(string="Max Volume (m^3)")
    

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            name = f"{record.name} ({record.max_weight} Kg), ({record.max_volume} m^3)"
            record.display_name = name