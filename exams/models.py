from django.core.exceptions import ValidationError
from django.db import models

from students.models import Student


class ExamResult(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="exam_results",
    )

    exam_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    total_marks = models.IntegerField(
        default=0,
    )

    percentage = models.FloatField(
        default=0,
    )

    grade = models.CharField(
        max_length=5,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "student",
                    "exam_name",
                ],
                name="unique_student_exam",
            )
        ]

    def calculate_result(self):

        subject_marks = (
            self.subject_marks.all()
        )

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

            self.percentage = round(
                (
                    total_obtained
                    / total_maximum
                ) * 100,
                2,
            )

        else:

            self.percentage = 0

        if self.percentage >= 90:
            self.grade = "A+"

        elif self.percentage >= 80:
            self.grade = "A"

        elif self.percentage >= 70:
            self.grade = "B"

        elif self.percentage >= 60:
            self.grade = "C"

        elif self.percentage >= 50:
            self.grade = "D"

        else:
            self.grade = "F"

class SubjectMark(models.Model):

    exam_result = models.ForeignKey(
        ExamResult,
        on_delete=models.CASCADE,
        related_name="subject_marks",
    )

    subject_name = models.CharField(
        max_length=100
    )

    mark_obtained = models.IntegerField()

    maximum_mark = models.IntegerField(
        default=100
    )

    def __str__(self):
        return self.subject_name
    
class ClassSubject(models.Model):

    student_class = models.CharField(
        max_length=20,
        choices=Student.CLASS_CHOICES,
    )

    subject_name = models.CharField(
        max_length=100,
    )

    class Meta:

        ordering = [
            "student_class",
            "subject_name",
        ]

    def __str__(self):

        return (
            f"{self.student_class} - "
            f"{self.subject_name}"
        )
