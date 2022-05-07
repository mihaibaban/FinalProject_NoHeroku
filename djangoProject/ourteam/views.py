from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class OurTeamTemplateView(TemplateView):
    template_name = 'ourTeam/our_team.html'