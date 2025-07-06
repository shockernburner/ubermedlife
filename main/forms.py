from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Consultation, TravelPlan, Doctor

class ConsultationForm(forms.ModelForm):
    """Form for consultation requests"""
    
    class Meta:
        model = Consultation
        fields = ['doctor', 'consultation_type', 'chief_complaint', 'medical_documents']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'consultation_type': forms.Select(attrs={'class': 'form-control'}),
            'chief_complaint': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'medical_documents': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'doctor': _('Select Doctor'),
            'consultation_type': _('Consultation Type'),
            'chief_complaint': _('Chief Complaint / Symptoms'),
            'medical_documents': _('Medical Documents (Optional)'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.filter(is_available=True)
        self.fields['chief_complaint'].help_text = _('Please describe your symptoms or medical concerns in detail.')

class TravelPlanForm(forms.ModelForm):
    """Form for travel plan requests"""
    
    class Meta:
        model = TravelPlan
        fields = [
            'doctor', 'treatment_type', 'estimated_duration', 
            'visa_assistance', 'accommodation_assistance', 
            'translator_required', 'notes'
        ]
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'treatment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'estimated_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'visa_assistance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'accommodation_assistance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'translator_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'doctor': _('Preferred Doctor'),
            'treatment_type': _('Type of Treatment'),
            'estimated_duration': _('Estimated Duration'),
            'visa_assistance': _('Need Visa Assistance'),
            'accommodation_assistance': _('Need Accommodation Assistance'),
            'translator_required': _('Need Translator'),
            'notes': _('Additional Notes'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.filter(is_available=True)

class ContactForm(forms.Form):
    """Contact form"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=_('Full Name')
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label=_('Email Address')
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=_('Phone Number'),
        required=False
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=_('Subject')
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        label=_('Message')
    )

class PatientProfileForm(forms.ModelForm):
    """Form for patient profile"""
    
    class Meta:
        from .models import PatientProfile
        model = PatientProfile
        fields = [
            'phone', 'date_of_birth', 'gender', 'address', 
            'emergency_contact', 'medical_history', 'preferred_language'
        ]
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preferred_language': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone': _('Phone Number'),
            'date_of_birth': _('Date of Birth'),
            'gender': _('Gender'),
            'address': _('Address'),
            'emergency_contact': _('Emergency Contact'),
            'medical_history': _('Medical History'),
            'preferred_language': _('Preferred Language'),
        }
