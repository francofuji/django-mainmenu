#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/06/2011

@author: francofuji@gmail.com
'''

from django.db import models

class MainMenu(models.Model):
    slug = models.SlugField(max_length = 50)
    name = models.CharField(max_length = 50, unique = True)
    url = models.CharField(max_length = 150)
    order = models.SmallIntegerField(unique = True)
    enabled = models.BooleanField(default = True)
    
    def __unicode__(self):
        return self.name
