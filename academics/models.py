from django.db import models


class AcademicYear(models.Model):

    year_name = models.CharField(
        max_length=20,
        unique=True,
    )

    is_active = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "-year_name",
        ]

    def __str__(self):

        return self.year_name