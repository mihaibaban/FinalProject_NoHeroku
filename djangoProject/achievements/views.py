from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class AchievementTemplateView(TemplateView):
    template_name = 'achievements/our_achievements.html'