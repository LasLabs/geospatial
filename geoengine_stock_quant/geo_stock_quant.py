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

#from openerp import models, fields, api
import logging
from openerp.osv import fields, osv
from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields


_logger = logging.getLogger(__name__)


class StockQuant(geo_model.GeoModel):
    """Add geo_point to stock.quant """
    _inherit = "stock.quant"

    geo_point = geo_fields.GeoPoint('Address Coordinate',
                                    readonly=True, store=True)

    
class StockMove(osv.osv):
    _inherit = 'stock.move'
    
    def write(self, cr, uid, ids, vals, context=None):
        
        super(StockMove, self).write(cr, uid, ids, vals, context)
        
        for move in self.browse(cr, uid, ids, context=context):
            if move.state == 'done':
                
                if move.location_dest_id.usage == 'customer':
                    for quant in move.quant_ids:
                        
                        _logger.info('Internal location quant geo_point - %s', quant.id)
                        
                        try:
                            quant.geo_point = move.partner_id.geo_point
                        except Exception as e:
                            _logger.error(
                                'Unable to apply geo for customer %s\n%s\n',
                                move.partner_id.id, e
                            )
                
                elif move.location_dest_id.usage == 'internal':
                    for quant in move.quant_ids:
                        
                        _logger.info('Internal location quant geo_point - %s', quant.id)
                        
                        try:
                            quant.geo_point = move.location_dest_id.partner_id.geo_point
                        except Exception as e:
                            _logger.error(
                                'Unable to apply geo for location %s\n%s\n',
                                move.location_dest_id.id, e
                            )
                        
                else:
                    _logger.error(
                        'Location type %s not implemented for geo tracking',
                        move.location_dest_id.usage
                    )
                    