from django.contrib import admin
from .models import Member
from .forms import CustomMemberCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Member
    form = CustomMemberCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_member',
                    'is_treasurer',
                    'is_storekeeper',
                    'is_secretary',
                    'is_troop_leader',
                    'is_scoutmaster',
                )
            }
        )
    )


admin.site.register(Member, CustomUserAdmin)

# admin.site.register(Member)
