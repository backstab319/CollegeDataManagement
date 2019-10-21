from django.urls import path
from StudentData.views import StudentDataManager

urlpatterns = [
    path('', StudentDataManager.StudentDataView, name='studentdata'),
    path('add/', StudentDataManager.AddStudentData, name="addstudentdata"),
    path('view/', StudentDataManager.ViewStudentData, name="viewstudentdata"),
    path('delete/', StudentDataManager.DeleteStudentData, name="deletestudentdata"),
    path('update/', StudentDataManager.UpdateStudentData, name="updatestudentdata"),
    path('result/', StudentDataManager.ResultPage, name='result'),
]
