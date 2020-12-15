# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ied.models import AttribType, Attribute, AttribValue
from ied.models import IED, LogicalNode, LogicalDevice, DataObject

from django.contrib import admin

# Register your models here.
admin.site.register(AttribType)
admin.site.register(Attribute)
admin.site.register(AttribValue)
admin.site.register(IED)
admin.site.register(LogicalNode)
admin.site.register(LogicalDevice)
admin.site.register(DataObject)

