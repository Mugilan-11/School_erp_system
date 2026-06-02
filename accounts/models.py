from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):

    ROLE_ADMIN = "ADMIN"
    ROLE_TEACHER = "TEACHER"
    ROLE_STUDENT = "STUDENT"
    ROLE_PARENT = "PARENT"

    ROLE_CHOICES = (
        (ROLE_ADMIN, "Admin"),
        (ROLE_TEACHER, "Teacher"),
        (ROLE_STUDENT, "Student"),
        (ROLE_PARENT, "Parent"),
    )

    phone_validator = RegexValidator(
        regex=r"^\+?[0-9]{10,15}$",
        message="Enter a valid phone number.",
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_STUDENT,
        db_index=True,
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[phone_validator],
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.username