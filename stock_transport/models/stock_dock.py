from odoo import _,fields, models


class StockDock(models.Model):
      _name = 'stock.dock'
      _description = "dock to ship"


      name = fields.Char(string='name')