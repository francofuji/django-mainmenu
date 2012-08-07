#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/06/2011

@author: francofuji@gmail.com
'''

from django.conf import settings

GET_MENU_FUNCTION = get_attr(settings, 'GET_MENU_FUNCTION', None)
ACTIVE_MENU_SESSION_VAR = get_attr(settings, 'ACTIVE_MENU_SESSION_VAR', 'active_menu')
