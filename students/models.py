from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Student(models.Model):

    CLASS_CHOICES = [
        ("SKG", "SKG"),
        ("JKG", "JKG"),
        ("Grade IA", "Grade IA"),
        ("Grade IB", "Grade IB"),
        ("Grade II", "Grade II"),
        ("Grade III", "Grade III"),
        ("Grade IV", "Grade IV"),
        ("Grade V", "Grade V"),
        ("Grade VI", "Grade VI"),
        ("Grade VII", "Grade VII"),
        ("Grade VIII", "Grade VIII"),
        ("Grade IX", "Grade IX"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student_profile",
    )

    first_name = models.CharField(
        max_length=100,
        db_index=True,
        null=True, 
        blank=True,
    )

    last_name = models.CharField(
        max_length=100,
        db_index=True,
        null=True,
        blank=True,
    )

    admission_no = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )
    name = models.CharField(
        max_length=200,
        db_index=True,
    
    )

    student_id = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        null=True,
        db_index=True,
    )

    student_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES,
        db_index=True,
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    address = models.TextField(
        null=True,
        blank=True, 
    )

    profile_picture = models.ImageField(
        upload_to="students/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "first_name",
            "last_name",
        ]
        verbose_name = "Student"
        verbose_name_plural = "Students"

    @property
    def full_name(self):

        if self.name:
            return self.name

        return (
            f"{self.first_name} "
            f"{self.last_name}"
            ).strip()
    
    def clean(self):

        if (
            self.date_of_birth
            and self.date_of_birth > timezone.now().date()
        ):
            raise ValidationError(
                {
                    "date_of_birth":
                    "Date of birth cannot be in the future."
                }
            )

    def save(self, *args, **kwargs):

        if self.student_id and not self.admission_no:
            self.admission_no = self.student_id

        if self.name and not self.first_name:
            self.first_name = self.name

        if not self.last_name:
            self.last_name = ""

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return (
        f"{self.student_id or self.admission_no}"
        f" - "
        f"{self.full_name}"
    )