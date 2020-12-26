from django.urls import path

from . import views

urlpatterns = [
    # ex: /ied/5/details/
    path('ied/<int:ied_id>/details/', views.details_ied, name='ied_details'),
    path('ied/<int:ied_id>/tree/', views.ied_tree, name='ied_tree'),
]
