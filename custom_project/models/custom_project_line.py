from odoo import models, fields

class CustomProjectLine(models.Model):
    _name = 'custom.project.line'
    _description = 'Project Inventory Line'

    project_id = fields.Many2one('custom.project', string='Project')
    product_id = fields.Many2one('product.product', string='Item', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
