from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import NewUser
from profiles.models import UserProfile


from django.forms import TextInput, Textarea




'''class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name')
    list_filter = ('email', 'username', 'first_name',
                   'is_active', 'is_staff')
    ordering = ('datetime',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('first_name', 'middle_name', 'last_name', 'country', 'gender', 'datetime')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name',
                       'password1', 'password2', 'is_active', 'is_staff', 'datetime')
        }),)'''


admin.site.register(NewUser)