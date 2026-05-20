from django.db import models


class Student(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    admission_no = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    student_class = models.CharField(max_length=50)

    section = models.CharField(max_length=10)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    email = models.EmailField(blank=True, null=True)

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"