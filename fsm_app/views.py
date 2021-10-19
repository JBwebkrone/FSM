from django.shortcuts import render
from django.views.generic import TemplateView

class Testview(TemplateView):
    template_name = "fsm_app/home.html"