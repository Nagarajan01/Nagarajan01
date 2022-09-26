from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
def list_view(request):
	ob1 = my_student.objects.all()
	return render(request, 'list_view.html', {"ob1" : ob1})

def add_students(request):
	form = student_Form(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
	return render(request,'form_view.html',{'form':form})

def student_update(request, id):
	update_mark = my_student.objects.get(id = id)
	form = student_Form(request.POST or None, request.FILES or None, instance=update_mark)
	if form.is_valid():
		form.save()
	return render(request, 'update_view.html', {'form': form})

def edit_marks(request, id):
	update_mark = my_student.objects.get(id=id)
	my_mark = student_marks(request.POST or None, request.FILES or None, instance=update_mark)
	if my_mark.is_valid():
		my_mark.save()
	return render(request, 'marks_view.html', {'form': my_mark})

def marks_view(request, id):
	mark = my_mark.objects.filter(student_id_id = id)
	return render(request, 'marks_view.html', {'form': mark})

def update(request, id):
	update_mark = my_mark.objects.get(student_id_id = id)
	form = student_marks(request.POST or None, request.FILES or None, instance=update_mark)
	if form.is_valid():
		form.save()
	return render(request, 'update_view.html', {'form': form})


















