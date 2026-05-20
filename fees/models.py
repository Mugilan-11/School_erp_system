from django.db import models
from students.models import Student


class Fee(models.Model):

    STATUS_CHOICES = (

        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.student} - {self.amount}"