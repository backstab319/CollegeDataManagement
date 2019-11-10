from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from StudentData.forms import AddStudentDataForm, DUStudentData
from StudentData.models import StudentData
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy

# Create your views here.
class DeleteStudentData(DeleteView):
    success_url = '/StudentData/delete/'
    model = StudentData

class ViewAndDelete(ListView):
    template_name = 'StudentData/DeleteStudentData.html'
    model = StudentData

    def get_context_data(request, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EditStudentData(UpdateView):
    model = StudentData
    fields = ['name','age','address','phone','course']
    template_name = 'StudentData/UpdateStudentData.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ViewStudentData(ListView):
    '''template_name = "StudentData/ViewStudentData.html"
    data_model = StudentData
    
    def get_context_data(self, **kwargs):
        data = self.data_model.objects.all()
        context = super().get_context_data(**kwargs)
        context['data'] = data
        return context'''

    template_name = "StudentData/ViewStudentData.html"
    model = StudentData

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentDataPage(TemplateView):
    template_name = "StudentData/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddStudentData(CreateView):
    template_name = "StudentData/AddStudentData.html"
    model = StudentData
    fields = ['name','age','address','course','phone']
    success_url = "/StudentData/result/"

class ResultPage(TemplateView):
    template_name = "StudentData/result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CDMPage(TemplateView):
    template_name = "StudentData/CDM.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DelStudentData(DeleteView):
    template_name = "StudentData/DeleteStudentData.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)