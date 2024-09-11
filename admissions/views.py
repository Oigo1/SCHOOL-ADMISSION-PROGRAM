from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Sum

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'admissions/home.html', {'students': students})

def register_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        class_year = request.POST['class_year']
        
        student = Student.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            age=age,
            class_year=class_year
        )
        ActivityStatus.objects.create(student=student)
        return redirect('pay_fee', student_id=student.id)  # After registration, redirect to student list
    return render(request, 'admissions/register_student.html')

def pay_fee(request, student_id):
    student = Student.objects.get(id=student_id)
    
    # Check if a fee record exists for the student
    fee, created = Fee.objects.get_or_create(student=student)  # No need for 'total_fee', it's in the model logic now

    if request.method == 'POST':
        # Get the new amount paid from the form and convert it to Decimal
        amount_paid = Decimal(request.POST['amount_paid'])

        # Update the amount paid and save the fee record
        fee.amount_paid += amount_paid
        fee.save()

        # Determine percentage paid
        total_fee = fee.fee_balance + fee.amount_paid  # Get total fee from model
        percentage_paid = (fee.amount_paid / total_fee) * Decimal('100')

        # Update activities based on percentage paid
        activity_status, created = ActivityStatus.objects.get_or_create(student=student)
        activity_status.bus = percentage_paid >= Decimal('30.00')
        activity_status.library = percentage_paid >= Decimal('20.00')
        activity_status.lunch = percentage_paid >= Decimal('20.00')
        activity_status.swimming = percentage_paid >= Decimal('10.00')
        activity_status.exams = percentage_paid >= Decimal('80.00')
        activity_status.save()

        return redirect('student_detail', student_id=student_id)

    return render(request, 'admissions/pay_fee.html', {'student': student})


def student_list(request):
    students_by_class = {}
    students = Student.objects.all()

    for student in students:
        if student.class_year not in students_by_class:
            students_by_class[student.class_year] = []
        students_by_class[student.class_year].append(student)

    return render(request, 'admissions/student_list.html', {'students_by_class': students_by_class})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    
    # Get or create the fee record for the student
    fee, created = Fee.objects.get_or_create(student=student)

    # Get or create the activity status for the student
    activity_status, created = ActivityStatus.objects.get_or_create(student=student)

    return render(request, 'admissions/student_detail.html', {
        'student': student,
        'fee': fee,
        'activity_status': activity_status,
    })
