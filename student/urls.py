from django.urls import path
from . import views

urlpatterns = [
    path("list_view/", views.list_view),
    path("add_students/", views.add_students),
    path("students/edit_marks/", views.edit_marks),
    path("students/marks/<int:id>", views.marks_view),
    path("students/update_marks/<int:id>", views.update),
    path("update/<int:id>", views.student_update),
]