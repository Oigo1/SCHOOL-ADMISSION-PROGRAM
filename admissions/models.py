from django.db import models
from decimal import Decimal

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Fee(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    @property
    def fee_balance(self):
        # Determine total fee based on the student's class year
        class_year_fees = {
            '1': Decimal('70000.00'),
            '2': Decimal('70000.00'),
            '3': Decimal('70000.00'),
            '4': Decimal('80000.00'),
            '5': Decimal('80000.00'),
            '6': Decimal('80000.00'),
            '7': Decimal('80000.00'),
            '9': Decimal('90000.00'),
        }
        # Get the total fee based on the student's class year, defaulting to 70,000 if class_year is missing
        total_fee = class_year_fees.get(self.student.class_year, Decimal('70000.00'))

        # Calculate the fee balance
        return total_fee - self.amount_paid

    def __str__(self):
        return f"{self.student} - Fee"

class ActivityStatus(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bus = models.BooleanField(default=False)
    library = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    exams = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - Activities"
    

class YearlyFee(models.Model):
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Yearly Fee: {self.total_fee}"