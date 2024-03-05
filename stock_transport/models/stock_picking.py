from odoo import _,fields, models

class Picking(models.Model):
    _inherit = "stock.picking"
    

    total_wh_weight = fields.Float(compute='_compute_total_wh_weight')
    total_wh_volume = fields.Float(compute='_compute_total_wh_weight')

    

    def _compute_total_wh_weight(self):
      for record in self:
            record.total_wh_weight = sum((line.product_id.weight * line.product_uom_qty) for line in record.move_ids)
            record.total_wh_volume = sum((line.product_id.volume * line.product_uom_qty) for line in record.move_ids)

      
     