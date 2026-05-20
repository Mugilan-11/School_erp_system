from django.db import models
from django.conf import settings


class Student(models.Model):

    CLASS_CHOICES = [

        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
        ('11', 'Class 11'),
        ('12', 'Class 12'),

    ]

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

    admission_no = models.CharField(
        max_length=100,
        unique=True
    )

    student_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to='students/',
        null=True,
        blank=True
    )

    def __str__(self):

        return f"{self.first_name} {self.last_name}"