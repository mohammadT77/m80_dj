from django.contrib import admin

# Register your models here.
from education.models import *

admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Semester)
admin.site.register(StudentCourse)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Operator)
