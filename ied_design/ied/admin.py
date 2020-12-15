# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 3rd party imports
from django.contrib import admin

# Custom model imports
from ied.models import AttribType, Attribute, AttribValue
from ied.models import IED, LogicalNode, LogicalDevice, DataObject

# ******************* Group *********************


class AttribValueInline(admin.TabularInline):
    model = AttribValue
    extra = 0


class AttributeAdmin(admin.ModelAdmin):
    model = Attribute

    inlines = [AttribValueInline]
# ****************** End Group ******************
#
# ******************* Group *********************


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0


class DataObjectAdmin(admin.ModelAdmin):
    model = DataObject
    inlines = [AttributeInline]

# ****************** End Group ******************
#
# ******************* Group *********************


class DataObjectInline(admin.TabularInline):
    model = DataObject
    extra = 0


class LogicalNodeAdmin(admin.ModelAdmin):
    model = LogicalNode

    inlines = [DataObjectInline]
# ****************** End Group ******************
#
# ******************* Group *********************


class LogicalDeviceInLine(admin.TabularInline):
    model = LogicalDevice
    extra = 0


class IEDAdmin(admin.ModelAdmin):
    model = IED
    fields = ['name', 'description']
    search_fields = ['name']

    inlines = [LogicalDeviceInLine]

# ****************** End Group ******************

# Register your models here.


admin.site.register(AttribType)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(IED, IEDAdmin)
admin.site.register(LogicalNode, LogicalNodeAdmin)
admin.site.register(LogicalDevice)
admin.site.register(DataObject, DataObjectAdmin)
