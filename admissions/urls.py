
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),  # For student registration
    path('pay_fee/<int:student_id>/', views.pay_fee, name='pay_fee'),  # For fee payment
    path('student_list/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),  # For student details
]