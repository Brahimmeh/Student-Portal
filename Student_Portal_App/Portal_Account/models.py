from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"Master"),(2,"Staff"),(3,"Teacher"),(4,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class MasterU(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=1, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=2)
    role=models.CharField(max_length=1000)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=3)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    duration=models.CharField(max_length=255,default="1")
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=4)
    gender=models.CharField(max_length=255)
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Mark(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    value=models.FloatField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Attendance_Student(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField()
    status=models.CharField(max_length=255,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Attendance_Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField()
    status=models.CharField(max_length=255,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Compliant_Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher_name= models.CharField(max_length=255,default="")
    Subject_name= models.CharField(max_length=255,default="")
    complaint = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Compliant_Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    Student_name= models.CharField(max_length=255,default="")
    Student_class= models.CharField(max_length=255,default="")
    Student_course= models.CharField(max_length=255,default="")
    complaint = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Note_Student(models.Model):
    id = models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE,default=1)
    Note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# class Note_Staff(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            MasterU.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance)
        if instance.user_type==3:
            Teacher.objects.create(admin=instance,address="")
        if instance.user_type==4:
            Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_start_year="2020-01-01",session_end_year="2021-01-01",address="",profile_pic="",gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.masteru.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.teacher.save()
    if instance.user_type==4:
        instance.students.save()