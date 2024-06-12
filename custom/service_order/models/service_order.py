from odoo import api, fields, models

class ServiceOrder(models.Model):
    _name = "service.order"
    _description = "Table service order"

    seller = fields.Many2one("sale.order",string="Atendente")
    partner_id = fields.Many2one("res.partner",string="Cliente")
    date_issue = fields.Date(string="Data de emissão")
    service_id = fields.Many2many("product.product", string="Serviço")
    obs = fields.Text(string="Observações")
    amount_total = fields.Float(string="Total", compute="_compute_total")
    state = fields.Selection(
        [
            ('open', 'Open'),
            ('progress', 'Progress'),
            ('closed', 'Closed'),
            ('cancel', 'Cancel'),
         ],
        string='Status',
        default='open'
    )

    @api.depends('service_id')
    def _compute_total(self):
        total = sum(line.lst_price for line in self.service_id)
        self.amount_total = total