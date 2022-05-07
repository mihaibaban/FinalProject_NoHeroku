from django.urls import path

from professor import views

urlpatterns = [
    path('create-professor/', views.ProfessorCreateView.as_view(),name='create_professor'),
    path('list-of-professors/', views.ProfessorListView.as_view(),name='list_of_professors'),
    path('update-professor/<int:pk>/', views.ProfessorUpdateView.as_view(),name='update_professor'),
    path('delete-professor/<int:pk>/', views.ProfessorDeleteView.as_view(),name='delete_professor'),
    path('details-professor/<int:pk>/', views.ProfessorDetailView.as_view(),name='details_professor'),
    path('inactivate-professor/<int:pk>/',views.inactivate_professor,name='inactivate_professor'),
    path('delete-professor-modal/<int:pk>/',views.delete_professor,name='delete_professor_modal'),
    path('get_info_professors_api/',views.ProfessorAPIView.as_view(),name='get-info-professors-api'),
    path('get_professors_api/<int:pk>/',views.ProfessorPKApiView.as_view(),name='get-professors-api'),

]
