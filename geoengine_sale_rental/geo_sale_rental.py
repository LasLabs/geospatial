# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley
#    Copyright: 2015 LasLabs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.addons.base_geoengine import geo_model, fields


class SaleRental(geo_model.GeoModel):
    """Add geo_point to sale.rental"""
    _inherit = "sale.rental"

    geo_point = fields.GeoPoint(
        'Addresses coordinate', related='partner_id.geo_point')