from django import forms


from .models import *


class student_Form(forms.ModelForm):
    class Meta:
        model = my_student
        fields = "__all__"

class student_marks(forms.ModelForm):
    class Meta:
        model = my_mark
        fields = "__all__"