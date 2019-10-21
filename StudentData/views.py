from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from StudentData.forms import AddStudentDataForm
from StudentData.models import StudentData

# Create your views here.
class StudentDataManager:
    def StudentDataView(request):
        return render(request, "StudentData/index.html")

    def AddStudentData(request):
        AddStudentDataTemplate = {}
        if request.method == "POST":
            form = AddStudentDataForm(request.POST)
            if form.is_valid():
                SDM = StudentDataManager()
                SDM.ADDSD(form)
                ShowForm = AddStudentDataForm()
                AddStudentDataTemplate.update({'form':ShowForm})
        else:
            ShowForm = AddStudentDataForm()
            AddStudentDataTemplate.update({'form':ShowForm})
        return render(request, "StudentData/AddStudentData.html",context=AddStudentDataTemplate)

    def ADDSD(request, form):
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        address = form.cleaned_data['address']
        course = form.cleaned_data['course']
        phone = int(form.cleaned_data['phone'])
        data = StudentData.objects.create(name=name, age=age, address=address, course=course, phone=phone)


    def ViewStudentData(request):
        ViewStudentTemplate = {
            'a':None,
        }
        return render(request, "StudentData/ViewStudentData.html", context=ViewStudentTemplate)

    def DeleteStudentData(request):
        return render(request, "StudentData/DeleteStudentData.html")

    def UpdateStudentData(request):
        return render(request, "StudentData/UpdateStudentData.html")

    def ResultPage(request):
        return render(request, "StudentData/result.html")

    def CDM(request):
        return render(request, "StudentData/CDM.html")