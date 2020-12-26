# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ied.models import IED


def details_ied(request, ied_id):
    ied = IED.objects.get(id=ied_id)
    context = {'ied': ied}
    return render(request, 'ied/ied_details.html', context)


def ied_tree(request, ied_id):
    ied = IED.objects.get(id=ied_id)
    context = {'ied': ied}
    return render(request, 'ied/ied_tree.html', context)
