from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

@permission_required("education.view_exam", login_url='/admin/login/', raise_exception=True)
def student_exams_view(request, exam_id):
    user = request.user
    groups = ",".join(map(lambda g:g.name,user.groups.all())) if not user.is_anonymous else "Anon"
    # if Exam(exam_id).student_course.student.id == user.id:
    #     # Permitted
    # else:
    #     # Not permitted!
    return HttpResponse(f"Hello World! {groups}")
