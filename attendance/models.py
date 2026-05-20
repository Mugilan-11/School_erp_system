from django.db import models
from students.models import Student


class Attendance(models.Model):

    STATUS_CHOICES = (

        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.student} - {self.date}"