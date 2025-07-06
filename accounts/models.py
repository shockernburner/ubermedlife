from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """Extended user profile"""
    USER_TYPES = [
        ('patient', _('Patient')),
        ('staff', _('Staff')),
        ('admin', _('Admin')),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='patient', verbose_name=_('User Type'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone Number'), blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Avatar'), blank=True, null=True)
    preferred_language = models.CharField(max_length=10, choices=[('en', 'English'), ('bn', 'বাংলা')], default='en')
    email_notifications = models.BooleanField(default=True, verbose_name=_('Email Notifications'))
    sms_notifications = models.BooleanField(default=True, verbose_name=_('SMS Notifications'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile when user is created"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save user profile when user is saved"""
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
