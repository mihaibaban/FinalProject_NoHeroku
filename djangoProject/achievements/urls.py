from django.urls import path

from achievements import views

urlpatterns = [
    path('our-achievements',views.AchievementTemplateView.as_view(), name='our_achievements')
]