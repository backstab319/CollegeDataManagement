from django.urls import path
from StudentData.views import *

urlpatterns = [
    path('', StudentDataPage.as_view(), name='studentdata'),
    path('add/', AddStudentData.as_view(), name="addstudentdata"),
    path('view/', ViewStudentData.as_view(), name="viewstudentdata"),
    path('result/', ResultPage.as_view(), name='result'),
    path('view/<int:pk>/', EditStudentData.as_view(), name='editstudentdata'),
    path('delete/', ViewAndDelete.as_view(), name='viewanddelete'),
    path('delete/<int:pk>/', DeleteStudentData.as_view(), name='deletestudentdata'),
]
