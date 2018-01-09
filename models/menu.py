# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('List'), False, URL('default', 'index')),
    ('Create', False, URL('default', 'create'))
]

if auth.has_membership('managers'):
    response.menu.append(('Manage', False, URL('default', 'manage')))