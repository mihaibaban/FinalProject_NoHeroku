from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from catalog.forms import CatalogForm
from catalog.models import Catalog
from student.models import Student

class CatalogTemplateView(TemplateView):
    template_name = 'catalog/catalog_template.html'

# def add_grade(request):
#     context = {
#         "students":Student.objects.all()
#     }
#     return render(request,'catalog/add_grade.html',context)



class CatalogCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'catalog/add_grade.html' #specificam calea catre fisierul html unde vom avea un fromular
    model = Catalog
    form_class = CatalogForm

    success_url = reverse_lazy('home') #dupa salvarea datelor din formular vom fii redirectionati catre pagina home
    #!'home'  este nameul url-ului


    #! reverse_lazy('home') -> home este denumirea url-ului din aplicatia home->urls.py
    permission_required = 'student.add_student'


    def get_context_data(self, **kwargs):
        context = super(CatalogCreateView, self).get_context_data(**kwargs)
        context["students"]=Student.objects.all()
        return context


class CatalogListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    template_name = 'catalog/list_of_grades.html'
    model = Catalog
    # context_object_name = 'all_grades'

    def get_queryset(self):
        return Catalog.objects.all()

    def get_context_data(self,**kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        filtered_context = {}
        for i in Catalog.objects.all():
            if i.private_name not in filtered_context:
                filtered_context[i.private_name] = {}
            if i.materie not in filtered_context[i.private_name]:
                filtered_context[i.private_name][i.materie] = []
            filtered_context[i.private_name][i.materie].append(i.nota_elev)

        context['all_grades'] = filtered_context
        return context





    permission_required = 'student.view_list_of_students'

