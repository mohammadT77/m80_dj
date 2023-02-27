from django.db import models

# Create your models here.
from core.models import BaseModel, User


class Course(BaseModel):
    name = models.TextField(max_length=10, null=False, blank=False)
    credits = models.IntegerField(default=2, null=False, blank=False)

    semester = models.ForeignKey("Semester", on_delete=models.RESTRICT)
    professor = models.ForeignKey("Professor", on_delete=models.RESTRICT)
    students = models.ManyToManyField("Student", through='StudentCourse')


class Exam(BaseModel):
    mid_mark = models.IntegerField(null=True, blank=True)
    final_mark = models.IntegerField(null=True, blank=True)

    student_course = models.ForeignKey('StudentCourse', on_delete=models.RESTRICT)


class Semester(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()


class StudentCourse(BaseModel):
    course = models.ForeignKey("Course", on_delete=models.RESTRICT)
    student = models.ForeignKey("Student", on_delete=models.RESTRICT)


class Student(User):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Professor(User):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'
    position = models.TextField(max_length=10, blank=True, null=True)


class Operator(User):
    class Meta:
        proxy = True
