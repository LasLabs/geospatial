# -*- coding: utf-8 -*-
##############################################################################
#
#   Author: Laurent Mignon
#   Copyright (c) 2015 Acsone SA/NV (http://www.acsone.eu)
#
#   Abstracted By: Dave Lasley - https://laslabs.com
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

from .abstract import GeoAbstract, Address

class ResPartner(geo_model.GeoModel):
    """Add geo_point to partner using a function field"""
    _inherit = "res.partner"

    @property
    def address(self, ):
        return Address( **{
            'street': self.street or '',
            'postal_code': self.zip or '',
            'city': self.city or '',
            'state':  self.state_id and self.state_id.name or '',
            'country': self.country_id and self.country_id.name or '',
            'country_codes': self.country_id and self.country_id.code or ''
        } )
