from odoo import models, fields

class CustomProject(models.Model):
    _name = 'custom.project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Custom Project'

    name = fields.Char(string='Project Name', required=True)
    user_id = fields.Many2one('res.users', string='Project Manager')
    description = fields.Text(string='Description')

    inventory_line_ids = fields.One2many(
        'custom.project.line',
        'project_id',
        string='Inventory Lines'
    )
