from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm
from student.models import Student


class StudentCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html' #specificam calea catre fisierul html unde vom avea un fromular
    model = Student
    form_class = StudentForm

    success_url = reverse_lazy('home') #dupa salvarea datelor din formular vom fii redirectionati catre pagina home
    #!'home'  este nameul url-ului

    #! reverse_lazy('home') -> home este denumirea url-ului din aplicatia home->urls.py
    permission_required = 'student.add_student'


class StudentListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    permission_required = 'student.view_list_of_students'


class StudentUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    template_name='student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.change_student'




class StudentDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')

    permission_required = 'student.delete_student'




class StudentDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    template_name = 'student/details_student.html'
    model = Student

    permission_required = 'student.view_student'




@login_required
@permission_required('student.inactivate_student')
def inactivate_student(request,pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list_of_students')

@login_required
@permission_required('student.delete_modal')
def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list_of_students')





