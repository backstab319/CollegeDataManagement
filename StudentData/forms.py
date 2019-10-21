from django import forms

class AddStudentDataForm(forms.Form):
    name = forms.CharField(max_length=35)
    age = forms.IntegerField(max_value=100)
    address = forms.CharField(max_length=50)
    course = forms.CharField(max_length=20)
    phone = forms.FloatField()