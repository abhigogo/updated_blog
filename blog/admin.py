from django.contrib import admin
from blog.models import user_profile, post, comment


# Register your models here.

admin.site.register(user_profile)
admin.site.register(post)
admin.site.register(comment)