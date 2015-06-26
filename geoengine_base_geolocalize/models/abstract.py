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

import logging
from openerp import api, fields
from openerp import exceptions
from openerp.tools.translate import _
from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields
import abc


try:
    import requests
except ImportError:
    logger = logging.getLogger(__name__)
    logger.warning('requests is not available in the sys path')


_logger = logging.getLogger(__name__)


class Address(object):
    ''' Generic Address interface to provide unified data for child objs    '''
    street = ''
    postal_code = ''
    city = ''
    state = ''
    country = ''
    country_codes = ''
    
    def __dict__(self, ):
        return dict(
            street = self.street,
            postalCode = self.postal_code,
            city = self.city,
            state = self.state,
            country = self.country,
            countryCodes = self.country_codes,
        )
    

class GeoAbstract(geo_model.GeoModel, abc.ABCMeta):
    ''' Create an abstract Geolocalization object for use with models '''
    
    ''' The following represent methods unique to children,
            Thus must be overridden in the children    '''
            
    @abc.abstractproperty
    def _inherit(self, ):
        ''' Model to inherit from   '''
        pass
    
    @abc.abstractproperty
    def address(self, ):
        ''' Abstract property for returning an address interface '''
        pass
    
    ''' Below are the generic methods for geo handlings '''

    @api.one
    def geocode_address(self):
        """Get the latitude and longitude by requesting "openstreetmap.org"
        see http://nominatim.openstreetmap.org/
        """
        
        url = 'http://nominatim.openstreetmap.org/search'
        
        params = { 'limit': 1, 'format': 'json',  }
        params.update(self.address)
        
        request_result = requests.get(url, params=params)
        
        try:
            request_result.raise_for_status()
            
        except Exception as e:
            _logger.exception('Geocoding error')
            raise exceptions.Warning(_(
                'Geocoding error. \n %s') % e.message)
        
        vals = request_result.json()
        vals = vals and vals[0] or {}
        
        self.write({
            'latitude': vals.get('lat'),
            'longitude': vals.get('lon'),
            'date_localization': fields.Date.today()
        })

    @api.one
    def geo_localize(self):
        self.geocode_address()
        return True

    @api.one
    @api.depends('latitude', 'longitude')
    def _get_geo_point(self):
        if not self.latitude or not self.longitude:
            self.geo_point = False
        else:
            self.geo_point = geo_fields.GeoPoint.from_latlon(
                self.env.cr, self.latitude, self.longitude)

    geo_point = geo_fields.GeoPoint(
        readonly=True, store=True, compute='_get_geo_point')
