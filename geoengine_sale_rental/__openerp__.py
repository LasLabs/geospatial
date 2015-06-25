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
{'name': 'Geospatial support for sale_rental',
 'version': '0.0.5',
 'category': 'GeoBI',
 'author': "LasLabs, Odoo Community Association (OCA)",
 'license': 'AGPL-3',
 'website': 'https://laslabs.com',
 'depends': [
     'base',
     'geoengine_partner',
     'sale',
     'sale_rental'
 ],
 'data': [
     'geo_sale_rental_view.xml'
 ],
 'installable': True,
 'application': True,
 'active': False,
}
