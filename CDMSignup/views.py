from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from StudentData.models import StudentData

# Create your views here.
class SelfStudentData(CreateView):
    model = StudentData
    template_name = 'CDMSignup/index.html'
    fields = ['name','age','address','course','phone']
    success_url = '/'

class resultPage(TemplateView):
    template_name = 'CDMSignup/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context