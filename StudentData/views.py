from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class StudentDataManager:
    def StudentDataView(request):
        return render(request, "StudentData/index.html")

    def CDMView(request):
        return render(request, "StudentData/CDM.html")