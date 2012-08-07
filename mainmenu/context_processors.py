#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/06/2011

@author: francofuji@gmail.com
'''

from models import MainMenu

from config import settings

def menu(request):
    get_menu_function = settings.GET_MENU_FUNCTION or get_menu
    menu_temp = get_menu_function(request)

    if not menu_temp:
        return {}

    menu = []

    active_menu = request.session.get(settings.ACTIVE_MENU_SESSION_VAR, False)
    
    for item in menu_temp:
        if item.nombre == menu_actual:
            item.activo = True
        else:
            item.activo = False
        menu.append(item)
    
    if not menu_actual:
        menu[0].activo = True
    
    return {'MENU':menu}

def get_menu(*args, **kwargs):
    return Menu.objects.all().order_by('orden')
