from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task

class TaskManagerAdminSite(admin.AdminSite):
    pass

task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")
#task_manager_admin_site.register(User, UserAdmin)
@admin.register(User, site=task_manager_admin_site)
class Custom_User_admin(UserAdmin):
    model = User
    
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Custom fields",
            {
                "fields": (
                    'role',
                )
            }
        )
    )
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Custom field",
            {
                "fields": (
                    "role",
                )
            }
        )
    )

@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "executor", "deadline"]
    list_display_links = ["title"]
    search_fields = ["title"]
