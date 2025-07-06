from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = _('User Profiles')

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_user_type', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'userprofile__user_type')
    
    def get_user_type(self, obj):
        return obj.userprofile.user_type if hasattr(obj, 'userprofile') else 'N/A'
    get_user_type.short_description = _('User Type')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'phone', 'preferred_language', 'email_notifications', 'created_at')
    list_filter = ('user_type', 'preferred_language', 'email_notifications', 'sms_notifications', 'created_at')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone')
    readonly_fields = ('created_at', 'updated_at')
