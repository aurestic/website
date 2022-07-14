# Copyright 2021 Studio73 - Ioan Galan <ioan@studio73.es>
# Copyright 2022 Aures TIC - Jose Zambudio <jose@aurestic.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    cookiefirst_identifier = fields.Char(
        string="Cookiefirst ID",
        related="website_id.cookiefirst_identifier",
        readonly=False,
    )
    cookiefirst_enabled = fields.Boolean(
        string="Use Cookiefirst",
        compute="_compute_cookiefirst_enabled",
        inverse="_inverse_cookiefirst_enabled",
    )

    @api.depends("website_id.cookiefirst_identifier")
    def _compute_cookiefirst_enabled(self):
        for record in self:
            record.update({
                "cookiefirst_enabled": bool(record.cookiefirst_identifier),
            })

    def _inverse_cookiefirst_enabled(self):
        for record in self:
            if not record.cookiefirst_enabled:
                record.website_id.update({"cookiefirst_identifier": False})
