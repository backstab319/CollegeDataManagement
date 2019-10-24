from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from StudentData.forms import AddStudentDataForm, DUStudentData
from StudentData.models import StudentData
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

# Create your views here.
class ViewStudentData(TemplateView):
    template_name = "StudentData/ViewStudentData.html"
    data_model = StudentData
    
    def get_context_data(self, **kwargs):
        data = self.data_model.objects.all()
        context = super().get_context_data(**kwargs)
        context['data'] = data
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

class GetUpdateName(FormView):
    template_name = "StudentData/UpdateStudentData.html"
    success_url = '/StudentData/update/'
    form_class = DUStudentData

    def form_valid(self, form):
        return super().form_valid(form)

class UpdateStudentData(UpdateView):
    template_name = "StudentData/UpdateStudentData.html"
    fields = ['name','age','address','course','phone']

    def get_object(self, data):
        return StudentData.objects.get(name="hello1234")