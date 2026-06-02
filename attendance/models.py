from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from students.models import Student


class Attendance(models.Model):

    PRESENT = "Present"
    ABSENT = "Absent"

    STATUS_CHOICES = [
        (PRESENT, "Present"),
        (ABSENT, "Absent"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    date = models.DateField(
        db_index=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        db_index=True,
    )

    remarks = models.TextField(
        blank=True,
        null=True,
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
            "-date",
            "student__first_name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "student",
                    "date",
                ],
                name="unique_student_attendance_per_day",
            )
        ]

        indexes = [
            models.Index(
                fields=[
                    "date",
                ]
            ),
            models.Index(
                fields=[
                    "status",
                ]
            ),
        ]

    def clean(self):

        if self.date > timezone.now().date():

            raise ValidationError(
                {
                    "date":
                    "Attendance date cannot be in the future."
                }
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )

    def __str__(self):

        return (
            f"{self.student.full_name}"
            f" - "
            f"{self.date}"
            f" - "
            f"{self.status}"
        )