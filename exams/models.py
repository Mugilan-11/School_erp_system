from django.db import models
from students.models import Student


class ExamResult(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    exam_name = models.CharField(
        max_length=100
    )

    total_marks = models.IntegerField(
        default=0
    )

    percentage = models.FloatField(
        default=0
    )

    grade = models.CharField(
        max_length=5,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def calculate_result(self):

        subject_marks = self.subjectmark_set.all()

        total_obtained = sum(
            subject.mark_obtained
            for subject in subject_marks
        )

        total_maximum = sum(
            subject.maximum_mark
            for subject in subject_marks
        )

        self.total_marks = total_obtained

        if total_maximum > 0:

            self.percentage = (
                total_obtained / total_maximum
            ) * 100

        if self.percentage >= 90:
            self.grade = 'A+'

        elif self.percentage >= 80:
            self.grade = 'A'

        elif self.percentage >= 70:
            self.grade = 'B'

        elif self.percentage >= 60:
            self.grade = 'C'

        elif self.percentage >= 50:
            self.grade = 'D'

        else:
            self.grade = 'F'

        self.save()

    def __str__(self):

        return f"{self.student} - {self.exam_name}"


class SubjectMark(models.Model):

    exam_result = models.ForeignKey(
        ExamResult,
        on_delete=models.CASCADE
    )

    subject_name = models.CharField(
        max_length=100
    )

    mark_obtained = models.IntegerField()

    maximum_mark = models.IntegerField(
        default=100
    )

    def __str__(self):

        return f"{self.subject_name}"