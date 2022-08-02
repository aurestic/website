# -*- coding: utf-8 -*-

from openerp.addons.web import http
from openerp.addons.website.controllers.main import Website


class WebsiteInhCookieFirst(Website):
    @http.route(
        "/legal/cookies-policy",
        type="http",
        auth="public",
        website=True,
    )
    def cookiefirst_index(self, **kw):
        page = "website_cookiefirst.cookies_policy"
        return self.page(page)
