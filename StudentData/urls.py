from django.urls import path
from StudentData.views import *

urlpatterns = [
    path('', StudentDataPage.as_view(), name='studentdata'),
    path('add/', AddStudentData.as_view(), name="addstudentdata"),
    path('view/', ViewStudentData.as_view(), name="viewstudentdata"),
    path('delete/', DelStudentData.as_view(), name="deletestudentdata"),
    path('update/', GetUpdateName.as_view(), name="updatestudentdata"),
    path('result/', ResultPage.as_view(), name='result'),
]
