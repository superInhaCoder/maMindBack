from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from django.utils.translation import gettext_lazy as _

from myapp.models import SocialPlatform, User, CheckList, UserCheck, UserGoal
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(SocialPlatform)
class SocialAdmin(admin.ModelAdmin):
    pass
    
    actions = None
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    

class UserGoalInline(admin.TabularInline):
    model = UserGoal
    fields = ['created_date', 'content', 'success']
    
class UserCheckInline(admin.TabularInline):
    model = UserCheck
    fields = ['selected_date', 'value']

@admin.register(User)
# class UserAdmin(DjangoUserAdmin):
class UserAdmin(admin.ModelAdmin):
    actions = None
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    

    inlines = [
        UserGoalInline,
        UserCheckInline
    ]

    '''
    fieldsets = (
        (_('Personal info'), {'fields': ('full_name', 'email', 'social', 'id', 'sub', 'password', )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            # 'groups',
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'date_birth')}),
    )
    ordering = ('-sub', '-date_joined')
    list_filter = ('social', 'date_joined', 'last_login')
    list_display = ('full_name', 'email', 'date_joined', 'last_login', 'social', 'id', 'sub', 'is_active')
    search_fields = ('full_name', 'id')
    readonly_fields = ('full_name', 'email', 'social', 'id', 'sub', 'password', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'date_birth',)
    '''
    
@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'content')
    ordering = ('id',)
    
@admin.register(UserCheck)
class UserCheckAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'user', 'check_list_id', 'selected_date', 'value')
    ordering = ('id',)
    pass
    
@admin.register(UserGoal)
class UserGoalAdmin(admin.ModelAdmin):
    pass