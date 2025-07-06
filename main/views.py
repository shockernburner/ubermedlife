from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Doctor, Service, Consultation, TravelPlan, Testimonial, NewsArticle, PatientProfile
from .forms import ConsultationForm, TravelPlanForm, ContactForm

def home(request):
    """Home page view"""
    featured_doctors = Doctor.objects.filter(is_available=True)[:6]
    services = Service.objects.filter(is_active=True)[:6]
    featured_testimonials = Testimonial.objects.filter(is_featured=True, is_published=True)[:3]
    featured_news = NewsArticle.objects.filter(is_featured=True, is_published=True)[:3]
    
    context = {
        'featured_doctors': featured_doctors,
        'services': services,
        'featured_testimonials': featured_testimonials,
        'featured_news': featured_news,
    }
    return render(request, 'main/home.html', context)

def services(request):
    """Services page view"""
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'main/services.html', context)

def doctors(request):
    """Doctors listing page"""
    doctors_list = Doctor.objects.filter(is_available=True)
    
    # Filter by specialization
    specialization = request.GET.get('specialization')
    if specialization:
        doctors_list = doctors_list.filter(specialization=specialization)
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        doctors_list = doctors_list.filter(
            Q(name__icontains=search) | 
            Q(hospital__icontains=search) |
            Q(specialization__icontains=search)
        )
    
    paginator = Paginator(doctors_list, 12)
    page_number = request.GET.get('page')
    doctors = paginator.get_page(page_number)
    
    specializations = Doctor.SPECIALIZATION_CHOICES
    
    context = {
        'doctors': doctors,
        'specializations': specializations,
        'current_specialization': specialization,
        'search_query': search,
    }
    return render(request, 'main/doctors.html', context)

def doctor_detail(request, doctor_id):
    """Doctor detail page"""
    doctor = get_object_or_404(Doctor, id=doctor_id, is_available=True)
    context = {
        'doctor': doctor,
    }
    return render(request, 'main/doctor_detail.html', context)

@login_required
def consultation_request(request, doctor_id=None):
    """Consultation request form"""
    doctor = None
    if doctor_id:
        doctor = get_object_or_404(Doctor, id=doctor_id, is_available=True)
    
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = request.user
            if doctor:
                consultation.doctor = doctor
            consultation.save()
            messages.success(request, _('Your consultation request has been submitted successfully!'))
            return redirect('consultation_success')
    else:
        form = ConsultationForm()
        if doctor:
            form.fields['doctor'].initial = doctor
    
    available_doctors = Doctor.objects.filter(is_available=True)
    
    context = {
        'form': form,
        'doctor': doctor,
        'available_doctors': available_doctors,
    }
    return render(request, 'main/consultation_request.html', context)

@login_required
def travel_plan_request(request, doctor_id=None):
    """Travel plan request form"""
    doctor = None
    if doctor_id:
        doctor = get_object_or_404(Doctor, id=doctor_id, is_available=True)
    
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            travel_plan = form.save(commit=False)
            travel_plan.patient = request.user
            if doctor:
                travel_plan.doctor = doctor
            travel_plan.save()
            messages.success(request, _('Your travel plan request has been submitted successfully!'))
            return redirect('travel_plan_success')
    else:
        form = TravelPlanForm()
        if doctor:
            form.fields['doctor'].initial = doctor
    
    available_doctors = Doctor.objects.filter(is_available=True)
    
    context = {
        'form': form,
        'doctor': doctor,
        'available_doctors': available_doctors,
    }
    return render(request, 'main/travel_plan_request.html', context)

@login_required
def dashboard(request):
    """Patient dashboard"""
    consultations = Consultation.objects.filter(patient=request.user).order_by('-created_at')[:5]
    travel_plans = TravelPlan.objects.filter(patient=request.user).order_by('-created_at')[:5]
    
    context = {
        'consultations': consultations,
        'travel_plans': travel_plans,
    }
    return render(request, 'main/dashboard.html', context)

@login_required
def my_consultations(request):
    """User's consultations"""
    consultations_list = Consultation.objects.filter(patient=request.user).order_by('-created_at')
    
    paginator = Paginator(consultations_list, 10)
    page_number = request.GET.get('page')
    consultations = paginator.get_page(page_number)
    
    context = {
        'consultations': consultations,
    }
    return render(request, 'main/my_consultations.html', context)

@login_required
def my_travel_plans(request):
    """User's travel plans"""
    travel_plans_list = TravelPlan.objects.filter(patient=request.user).order_by('-created_at')
    
    paginator = Paginator(travel_plans_list, 10)
    page_number = request.GET.get('page')
    travel_plans = paginator.get_page(page_number)
    
    context = {
        'travel_plans': travel_plans,
    }
    return render(request, 'main/my_travel_plans.html', context)

def testimonials(request):
    """Testimonials page"""
    testimonials_list = Testimonial.objects.filter(is_published=True).order_by('-created_at')
    
    paginator = Paginator(testimonials_list, 12)
    page_number = request.GET.get('page')
    testimonials = paginator.get_page(page_number)
    
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'main/testimonials.html', context)

def news(request):
    """News and articles page"""
    news_list = NewsArticle.objects.filter(is_published=True).order_by('-published_at')
    
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'news': news,
    }
    return render(request, 'main/news.html', context)

def news_detail(request, slug):
    """News article detail"""
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    related_articles = NewsArticle.objects.filter(
        is_published=True
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'main/news_detail.html', context)

def about(request):
    """About us page"""
    return render(request, 'main/about.html')

def contact(request):
    """Contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you would typically send an email or save to database
            messages.success(request, _('Thank you for your message. We will get back to you soon!'))
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)

def consultation_success(request):
    """Consultation request success page"""
    return render(request, 'main/consultation_success.html')

def travel_plan_success(request):
    """Travel plan request success page"""
    return render(request, 'main/travel_plan_success.html')
