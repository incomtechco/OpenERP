# -*- coding: utf-8 -*-
from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
from datetime import datetime
import datetime
import calendar

class ir_ui_menu(osv.osv):
    _inherit = 'ir.ui.menu'
     
    _columns = {
        'active': fields.boolean('Active'),
        }
    _defaults = {
        'active': True,
    }
ir_ui_menu()

class openerp_menu_mapping(osv.osv):
    _name = 'openerp.menu.mapping'
     
    _columns = {
        'key': fields.char('Key', size = 255),
        'openerp_menu_key': fields.char('Openerp Menu Key', size = 1000),
        }
openerp_menu_mapping()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

