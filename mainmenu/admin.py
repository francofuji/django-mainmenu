#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/06/2011

@author: francofuji@gmail.com
'''

from django.contrib import admin

from models import MainMenu

class MainMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(MainMenu, MainMenuAdmin)
