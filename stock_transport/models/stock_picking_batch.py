
from odoo import api, fields, models, _


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"
    
    
    vehicle_ids = fields.Many2one('fleet.vehicle', string='vehicles')
    vehicle_categories = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')

    stock_dock_id = fields.Many2one('stock.dock')
    lines = fields.Integer(compute='_compute_lines',store=True)
    transfer = fields.Integer(compute='_compute_transfers',store=True)

    weight = fields.Float(string='Weight (kg)', compute="_compute_progressbar", store=True)
    volume = fields.Float(string='Volume (m^3)', compute="_compute_progressbar", store=True)
    date = fields.Date()

    @api.depends('picking_ids')
    def _compute_transfers(self):
        for record in self:
            curr = len(record.picking_ids)
            record.transfer = curr

    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            curr = len(record.move_line_ids)
            record.lines = curr




    

    @api.depends('picking_ids', 'vehicle_categories')
    def _compute_progressbar(self):
        temp_w = 0
        temp_v = 0

        for record in self:
            temp_w = sum((line.total_wh_weight) for line in record.picking_ids) 
            temp_v = sum((line.total_wh_volume) for line in record.picking_ids)

        if self.vehicle_categories.max_weight > 0:
            self.weight = (temp_w/self.vehicle_categories.max_weight) * 100
        else:
            self.weight = 0

        if self.vehicle_categories.max_volume > 0:
            self.volume = (temp_v/self.vehicle_categories.max_volume) * 100
        else:
            self.volume = 0