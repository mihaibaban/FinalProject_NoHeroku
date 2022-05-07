from django.urls import path

from ourteam import views

urlpatterns = [
    path('our-team/',views.OurTeamTemplateView.as_view(), name='our_team')
]