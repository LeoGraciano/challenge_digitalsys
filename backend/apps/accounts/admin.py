from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from apps.accounts.forms import UserChangeForm, UserCreationForm
User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    readonly_fields = ["last_login", "date_joined", "id"]
    ordering = ['email']
    search_fields = ['email', 'name']
    list_display = ['email', 'is_active',
                    'is_staff', 'is_superuser']
    filter_display = ['is_active', 'is_staff',
                      'is_superuser']

    fieldsets = (
        (
            "Fields",
            {
                "fields": (
                    "id",
                    'name',
                    "email",

                    "date_joined",
                    "last_login",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "password",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "Fields",
            {
                "fields": (
                    "code",
                    'name',
                    "email",
                    "date_joined",
                    "last_login",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "password1",
                    "password2",
                    "firstAccess"
                )
            },
        ),
    )
