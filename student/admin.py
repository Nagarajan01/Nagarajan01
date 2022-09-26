from django.contrib import admin
from .models import *

class student(admin.ModelAdmin):
    list_display = ('name', "roll_no", "img")
admin.site.register(my_student, student)

class marks(admin.ModelAdmin):
    list_display = ("student_id", "sub1", "sub2", "sub3", "sub4", "sub5")
admin.site.register(my_mark, marks)
# Register your models here.
