{
    'name': 'stock transport',
    'version': '17.0.1.0.0',
    'author': 'Piyush Sharma',
    'depends': ['stock_picking_batch','fleet'],
    'data':[
      'security/ir.model.access.csv',
      'views/fleet_vehicle_model_views.xml',
      'views/stock_picking_batch_views.xml',
      'views/stock_picking_views.xml',
    ],
    "auto_install": True,
}