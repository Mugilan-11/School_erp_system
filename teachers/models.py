from django.db import models
from django.conf import settings


class Teacher(models.Model):

    GENDER_CHOICES = [

        ('Male', 'Male'),
        ('Female', 'Female'),

    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    employee_id = models.CharField(
        max_length=100,
        unique=True
    )

    subject = models.CharField(
        max_length=100
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to='teachers/',
        null=True,
        blank=True
    )

    def __str__(self):

        return f"{self.first_name} {self.last_name}"