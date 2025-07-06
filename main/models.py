from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Doctor(models.Model):
    """Model for Chinese doctors"""
    SPECIALIZATION_CHOICES = [
        ('cardiology', _('Cardiology')),
        ('neurology', _('Neurology')),
        ('oncology', _('Oncology')),
        ('orthopedics', _('Orthopedics')),
        ('dermatology', _('Dermatology')),
        ('gastroenterology', _('Gastroenterology')),
        ('pediatrics', _('Pediatrics')),
        ('psychiatry', _('Psychiatry')),
        ('radiology', _('Radiology')),
        ('surgery', _('Surgery')),
        ('other', _('Other')),
    ]
    
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    name_chinese = models.CharField(max_length=255, verbose_name=_('Chinese Name'), blank=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, verbose_name=_('Specialization'))
    hospital = models.CharField(max_length=255, verbose_name=_('Hospital'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    experience_years = models.IntegerField(verbose_name=_('Years of Experience'))
    education = models.TextField(verbose_name=_('Education'), blank=True)
    biography = models.TextField(verbose_name=_('Biography'), blank=True)
    biography_bangla = models.TextField(verbose_name=_('Biography (Bangla)'), blank=True)
    photo = models.ImageField(upload_to='doctors/', verbose_name=_('Photo'), blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Consultation Fee (USD)'))
    is_available = models.BooleanField(default=True, verbose_name=_('Available'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class Service(models.Model):
    """Medical services offered"""
    SERVICE_TYPES = [
        ('consultation', _('Teleconsultation')),
        ('second_opinion', _('Second Opinion')),
        ('treatment', _('Treatment in China')),
        ('surgery', _('Surgery')),
        ('diagnostics', _('Diagnostics')),
        ('medication', _('Medication Access')),
        ('travel', _('Medical Travel')),
    ]
    
    name = models.CharField(max_length=255, verbose_name=_('Service Name'))
    name_bangla = models.CharField(max_length=255, verbose_name=_('Service Name (Bangla)'), blank=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES, verbose_name=_('Service Type'))
    description = models.TextField(verbose_name=_('Description'))
    description_bangla = models.TextField(verbose_name=_('Description (Bangla)'), blank=True)
    price_range = models.CharField(max_length=100, verbose_name=_('Price Range'), blank=True)
    duration = models.CharField(max_length=100, verbose_name=_('Duration'), blank=True)
    icon = models.ImageField(upload_to='services/', verbose_name=_('Icon'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    """Extended profile for patients"""
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone Number'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'), null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    address = models.TextField(verbose_name=_('Address'))
    emergency_contact = models.CharField(max_length=255, verbose_name=_('Emergency Contact'))
    medical_history = models.TextField(verbose_name=_('Medical History'), blank=True)
    preferred_language = models.CharField(max_length=10, choices=[('en', 'English'), ('bn', 'বাংলা')], default='en')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Patient Profile')
        verbose_name_plural = _('Patient Profiles')
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Consultation(models.Model):
    """Consultation requests"""
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('scheduled', _('Scheduled')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]
    
    CONSULTATION_TYPES = [
        ('teleconsultation', _('Teleconsultation')),
        ('second_opinion', _('Second Opinion')),
        ('pre_travel', _('Pre-travel Consultation')),
    ]
    
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Patient'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name=_('Doctor'))
    consultation_type = models.CharField(max_length=50, choices=CONSULTATION_TYPES, verbose_name=_('Type'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_('Status'))
    scheduled_date = models.DateTimeField(verbose_name=_('Scheduled Date'), null=True, blank=True)
    chief_complaint = models.TextField(verbose_name=_('Chief Complaint'))
    medical_documents = models.FileField(upload_to='consultations/', verbose_name=_('Medical Documents'), blank=True, null=True)
    notes = models.TextField(verbose_name=_('Notes'), blank=True)
    prescription = models.TextField(verbose_name=_('Prescription'), blank=True)
    follow_up_required = models.BooleanField(default=False, verbose_name=_('Follow-up Required'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Consultation')
        verbose_name_plural = _('Consultations')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient.first_name} - Dr. {self.doctor.name} - {self.consultation_type}"

class TravelPlan(models.Model):
    """Medical travel plans to China"""
    STATUS_CHOICES = [
        ('planning', _('Planning')),
        ('approved', _('Approved')),
        ('visa_processing', _('Visa Processing')),
        ('scheduled', _('Scheduled')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]
    
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Patient'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name=_('Doctor'))
    hospital = models.CharField(max_length=255, verbose_name=_('Hospital'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    treatment_type = models.CharField(max_length=255, verbose_name=_('Treatment Type'))
    estimated_duration = models.CharField(max_length=100, verbose_name=_('Estimated Duration'))
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Estimated Cost (USD)'))
    travel_date = models.DateField(verbose_name=_('Travel Date'), null=True, blank=True)
    return_date = models.DateField(verbose_name=_('Return Date'), null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning', verbose_name=_('Status'))
    visa_assistance = models.BooleanField(default=True, verbose_name=_('Visa Assistance Required'))
    accommodation_assistance = models.BooleanField(default=True, verbose_name=_('Accommodation Assistance'))
    translator_required = models.BooleanField(default=True, verbose_name=_('Translator Required'))
    notes = models.TextField(verbose_name=_('Notes'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Travel Plan')
        verbose_name_plural = _('Travel Plans')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient.first_name} - {self.hospital} - {self.treatment_type}"

class Testimonial(models.Model):
    """Patient testimonials"""
    patient_name = models.CharField(max_length=255, verbose_name=_('Patient Name'))
    patient_name_bangla = models.CharField(max_length=255, verbose_name=_('Patient Name (Bangla)'), blank=True)
    treatment = models.CharField(max_length=255, verbose_name=_('Treatment'))
    testimonial = models.TextField(verbose_name=_('Testimonial'))
    testimonial_bangla = models.TextField(verbose_name=_('Testimonial (Bangla)'), blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name=_('Rating'))
    photo = models.ImageField(upload_to='testimonials/', verbose_name=_('Photo'), blank=True, null=True)
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    is_published = models.BooleanField(default=True, verbose_name=_('Published'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient_name} - {self.rating} stars"

class NewsArticle(models.Model):
    """News and blog articles"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    title_bangla = models.CharField(max_length=255, verbose_name=_('Title (Bangla)'), blank=True)
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    content = models.TextField(verbose_name=_('Content'))
    content_bangla = models.TextField(verbose_name=_('Content (Bangla)'), blank=True)
    excerpt = models.TextField(max_length=500, verbose_name=_('Excerpt'), blank=True)
    featured_image = models.ImageField(upload_to='news/', verbose_name=_('Featured Image'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    is_published = models.BooleanField(default=False, verbose_name=_('Published'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Published At'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('News Article')
        verbose_name_plural = _('News Articles')
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
