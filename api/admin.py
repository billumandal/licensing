from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import Name, UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_plural_name = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'is_staff')
    list_select_related = ('userprofile',)

    def get_ip_addr(self, instance):
        return instance.userprofile.ip_addr
    get_ip_addr.short_description = 'IP Address'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class NameAdmin(admin.ModelAdmin):
    list_display = Name._meta.get_all_field_names()

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Name, NameAdmin)