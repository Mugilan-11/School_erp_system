from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Teacher(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    phone_validator = RegexValidator(
        regex=r"^\+?[0-9]{10,15}$",
        message="Enter a valid phone number.",
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="teacher_profile",
    )

    first_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    last_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    employee_id = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    subject = models.CharField(
        max_length=100,
        db_index=True,
    )

    qualification = models.CharField(
        max_length=150,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    phone = models.CharField(
        max_length=15,
        validators=[phone_validator],
    )

    joining_date = models.DateField(
        null=True,
        blank=True,
    )

    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to="teachers/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = [
            "first_name",
            "last_name",
        ]
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    @property
    def full_name(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        ).strip()

    def clean(self):

        if (
            self.joining_date
            and self.joining_date > timezone.now().date()
        ):
            raise ValidationError(
                {
                    "joining_date":
                    "Joining date cannot be in the future."
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.employee_id}"
            f" - "
            f"{self.full_name}"
        )