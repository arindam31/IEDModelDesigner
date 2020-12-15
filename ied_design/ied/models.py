# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class IED(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class LogicalDevice(models.Model):
    name = models.CharField(max_length=100)
    ied = models.ForeignKey(IED, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, default='')

    abbr = 'LD'

    def __str__(self):
        return self.name

class LogicalNode(models.Model):
    name = models.CharField(max_length=100)
    logical_device = models.ForeignKey(LogicalDevice, on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=200, default="")

    abbr = 'LN'

    def __str__(self):
        return self.name

class DataObject(models.Model):
    name = models.CharField(max_length=100)
    logical_node = models.ForeignKey(LogicalNode, on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=200, default="")

    abbr = 'DO'

    def __str__(self):
        return self.name


class AttribType(models.Model):
    name = models.CharField(max_length=3, unique=True)
    desciption = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = "AttibuteType"
        verbose_name_plural = "AttriButeTypes"

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    attrib_type = models.ForeignKey(AttribType, on_delete=models.PROTECT, )
    description = models.CharField(max_length=200, default="")
    data_object = models.ForeignKey(DataObject, on_delete=models.CASCADE, null=True)

    class AttribChoice(models.TextChoices):
        MANDATORY = 'M'
        OPTIONAL = 'O'
        CONDITIONAL = 'C'

    attrib_choice = models.CharField(
        max_length=2,
        choices=AttribChoice.choices,
        default=AttribChoice.MANDATORY,
    )

    def __str__(self):
        return self.name

class AttribValue(models.Model):
    value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.value

