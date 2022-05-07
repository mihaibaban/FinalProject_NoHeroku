from django.urls import path

from catalog import views

urlpatterns = [
    path('catalog/',views.CatalogTemplateView.as_view(), name='catalog'),
    path('upgrade-catalog/',views.CatalogCreateView.as_view(), name='catalog-add-grade'),
    path('list-of-grades/',views.CatalogListView.as_view(), name='list_of_grades')
]