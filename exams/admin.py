from django.contrib import admin

from .models import (
    ExamResult,
    SubjectMark,
    ClassSubject,
)


admin.site.register(ExamResult)
admin.site.register(SubjectMark)
admin.site.register(ClassSubject)