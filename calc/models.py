from django.db import models

# Create your models here.
class student(models.Model):

    student_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    year= models.PositiveIntegerField()
    dob= models.DateField()


class teacher(models.Model):

    teacher_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    subject= models.TextField()


class lecture(models.Model):

    lecture_id = models.AutoField(primary_key=True)
    name= models.TextField()
    date= models.DateField()
    subject= models.ForeignKey(teacher, on_delete=models.CASCADE)


class assignment(models.Model):

    assignment_id = models.AutoField(primary_key=True)
    name= models.TextField()
    due_date= models.DateField()
    publish_date = models.ForeignKey(lecture, on_delete=models.CASCADE)
    #lecture_id = models.ForeignKey(lecture, on_delete=models.SET_NULL)


