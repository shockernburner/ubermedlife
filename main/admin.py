from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Doctor, Service, PatientProfile, Consultation, TravelPlan, Testimonial, NewsArticle

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital', 'city', 'consultation_fee', 'is_available', 'created_at')
    list_filter = ('specialization', 'city', 'is_available', 'created_at')
    search_fields = ('name', 'name_chinese', 'hospital', 'specialization')
    list_editable = ('is_available', 'consultation_fee')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'name_chinese', 'specialization', 'photo')
        }),
        (_('Hospital Information'), {
            'fields': ('hospital', 'city', 'consultation_fee', 'is_available')
        }),
        (_('Professional Details'), {
            'fields': ('experience_years', 'education', 'biography', 'biography_bangla')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'price_range', 'duration', 'is_active', 'created_at')
    list_filter = ('service_type', 'is_active', 'created_at')
    search_fields = ('name', 'name_bangla', 'description')
    list_editable = ('is_active',)

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'gender', 'preferred_language', 'created_at')
    list_filter = ('gender', 'preferred_language', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'consultation_type', 'status', 'scheduled_date', 'created_at')
    list_filter = ('consultation_type', 'status', 'scheduled_date', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__name', 'chief_complaint')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'scheduled_date'

@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'hospital', 'city', 'treatment_type', 'status', 'travel_date', 'estimated_cost')
    list_filter = ('status', 'city', 'travel_date', 'visa_assistance', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__name', 'hospital', 'treatment_type')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'travel_date'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'treatment', 'rating', 'is_featured', 'is_published', 'created_at')
    list_filter = ('rating', 'is_featured', 'is_published', 'created_at')
    search_fields = ('patient_name', 'patient_name_bangla', 'treatment', 'testimonial')
    list_editable = ('is_featured', 'is_published')

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'is_featured', 'published_at', 'created_at')
    list_filter = ('is_published', 'is_featured', 'published_at', 'created_at')
    search_fields = ('title', 'title_bangla', 'content', 'excerpt')
    list_editable = ('is_published', 'is_featured')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
