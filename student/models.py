from django.db import models
from django.db import models


class my_student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField(max_length=200)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return "{}".format(self.id)

class my_mark(models.Model):
    student_id = models.ForeignKey(my_student, on_delete=models.CASCADE)
    sub1 = models.IntegerField(max_length=200)
    sub2 = models.IntegerField(max_length=200)
    sub3 = models.IntegerField(max_length=200)
    sub4 = models.IntegerField(max_length=200)
    sub5 = models.IntegerField(max_length=200)

    def __str__(self):
        return "{}".format(self.student_id)




