# Copyright 2021 Studio73 - Ioan Galan <ioan@studio73.es>
# Copyright 2022 Aures TIC - Jose Zambudio <jose@aurestic.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class Website(models.Model):
    _inherit = "website"

    cookiefirst_identifier = fields.Char(
        string="Cookiefirst ID",
        help="This field holds the ID, needed for Cookiefirst functionality.",
    )
