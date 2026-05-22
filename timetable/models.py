from django.db import models

from teachers.models import Teacher


class Timetable(models.Model):

    DAYS = [

        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),

    ]

    class_name = models.CharField(
        max_length=20
    )

    subject = models.CharField(
        max_length=100
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    day = models.CharField(
        max_length=20,
        choices=DAYS
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    def __str__(self):

        return f"{self.class_name} - {self.subject}"