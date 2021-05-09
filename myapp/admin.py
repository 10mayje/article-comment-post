from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import UserProfile,Image,Image2,Blog,Comment,Like
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'
    fk_name = 'user'
class ProfileImage(admin.StackedInline):
    model = Image
    can_delete = False
    verbose_name_plural = 'image'
    fk_name = 'user'



class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,ProfileImage)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Image2)
admin.site.register(Comment)
admin.site.register(Like)