from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('consultation/', views.consultation_request, name='consultation_request'),
    path('consultation/<int:doctor_id>/', views.consultation_request, name='consultation_request_doctor'),
    path('travel-plan/', views.travel_plan_request, name='travel_plan_request'),
    path('travel-plan/<int:doctor_id>/', views.travel_plan_request, name='travel_plan_request_doctor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-consultations/', views.my_consultations, name='my_consultations'),
    path('my-travel-plans/', views.my_travel_plans, name='my_travel_plans'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('consultation-success/', views.consultation_success, name='consultation_success'),
    path('travel-plan-success/', views.travel_plan_success, name='travel_plan_success'),
]
