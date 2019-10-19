from django.urls import path
from StudentData.views import StudentDataManager

urlpatterns = [
    path('', StudentDataManager.StudentDataView, name='studentdata'),
]
