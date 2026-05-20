from django.db import models
from accounts.models import CustomUser


class Timetable(models.Model):

    DAY_CHOICES = (

        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )

    class_name = models.CharField(
        max_length=20
    )

    section = models.CharField(
        max_length=10
    )

    subject = models.CharField(
        max_length=100
    )

    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={
            'role': 'TEACHER'
        }
    )

    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    room_number = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.class_name} - {self.subject}"