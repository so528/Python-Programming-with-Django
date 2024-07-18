from django.urls import path
from django.views.generic import TemplateView

urlpatters =[
    path('about/', TemplateView.as_view(template_name = "about.html"))
]