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

    def no_of_values(self, obj):
        """This gives the number of data objects in this Node"""
        return obj.attribvalue_set.count()

    list_display = ['name', 'no_of_values']
    inlines = [AttribValueInline]
# ****************** End Group ******************
#
# ******************* Group *********************


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0


class DataObjectAdmin(admin.ModelAdmin):


    def no_of_attributes(self, obj):
        """This gives the number of data objects in this Node"""
        return obj.attribute_set.count()

    model = DataObject
    list_display = ['name', 'no_of_attributes']
    inlines = [AttributeInline]

# ****************** End Group ******************
#
# ******************* Group *********************

class LogicalNodeInline(admin.TabularInline):
    model = LogicalNode
    extra = 0

class LogicalDeviceAdmin(admin.ModelAdmin):
    model = LogicalDevice

    def no_of_logical_nodes(self, obj):
        """This gives the number of data objects in this Node"""
        return obj.logicalnode_set.count()

    list_display = ['name', 'no_of_logical_nodes']
    inlines = [LogicalNodeInline]

# ****************** End Group ******************
#
# ******************* Group *********************


class DataObjectInline(admin.TabularInline):
    model = DataObject
    extra = 0


class LogicalNodeAdmin(admin.ModelAdmin):


    def no_of_data_objects(self, obj):
        """This gives the number of data objects in this Node"""
        return obj.dataobject_set.count()

    model = LogicalNode

    list_display = ['name', 'no_of_data_objects']
    inlines = [DataObjectInline]
# ****************** End Group ******************
#
# ******************* Group *********************


class LogicalDeviceInLine(admin.TabularInline):
    model = LogicalDevice
    extra = 0


class IEDAdmin(admin.ModelAdmin):

    def no_of_logical_devices(self, obj):
        """This gives the number of logical devices in this IED"""
        return obj.logicaldevice_set.count()

    model = IED
    fields = ['name', 'description']
    list_display = ['name', 'no_of_logical_devices']
    search_fields = ['name']

    inlines = [LogicalDeviceInLine]

# ****************** End Group ******************

# Register your models here.


admin.site.register(AttribType)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(IED, IEDAdmin)
admin.site.register(LogicalNode, LogicalNodeAdmin)
admin.site.register(LogicalDevice, LogicalDeviceAdmin)
admin.site.register(DataObject, DataObjectAdmin)
