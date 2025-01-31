# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Ansil pv (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

# from odoo import fields, models


# class Website(models.Model):
#     """
#     Inheriting fields into website
#     """
#     _inherit = "website"

#     enable_messenger = fields.Boolean("Enable Messenger",
#                                       help="Enable for show page id field")
#     fb_id_page = fields.Char("Facebook Page Id", help="To add facebook page id")

from odoo import fields, models

class Website(models.Model):
    """
    Inheriting fields into website for Messenger Integration
    """
    _inherit = "website"

    enable_messenger = fields.Boolean(
        "Enable Messenger",
        help="Enable Messenger integration on the website"
    )

    fb_id_page = fields.Char(
        "Facebook Page Id",
        help="Enter Facebook Page ID for Messenger integration"
    )

    fb_app_id = fields.Char(
        "Facebook App Id",
        help="Enter Facebook App ID for Messenger integration"
    )

    fb_app_secret = fields.Char(
        "Facebook App Secret",
        help="Enter Facebook App Secret for Messenger integration"
    )

    fb_access_token = fields.Char(
        "Facebook Access Token",
        help="Enter Facebook Access Token for Messenger integration"
    )

    # Add any other fields needed for Messenger or other integrations
