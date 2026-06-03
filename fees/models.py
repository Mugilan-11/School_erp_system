from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from students.models import Student


class Fee(models.Model):

    PAID = "Paid"
    PENDING = "Pending"

    STATUS_CHOICES = [
        (PAID, PAID),
        (PENDING, PENDING),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="fees",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    payment_date = models.DateField()

    due_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        db_index=True,
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:

        ordering = [
            "-payment_date",
        ]

        indexes = [
            models.Index(
                fields=[
                    "payment_date",
                ]
            ),
            models.Index(
                fields=[
                    "status",
                ]
            ),
        ]

    def clean(self):

        if self.amount <= 0:

            raise ValidationError(
                {
                    "amount":
                    "Amount must be greater than zero."
                }
            )

        if (
            self.payment_date
            and self.payment_date > timezone.now().date()
        ):

            raise ValidationError(
                {
                    "payment_date":
                    "Payment date cannot be in the future."
                }
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )

    def __str__(self):

        return (
            f"{self.student.name}"
            f" - ₹{self.amount}"
        )