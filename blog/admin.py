from django.contrib import admin
from blog.models import user_profile, Post, comment


# Register your models here.

admin.site.register(user_profile)
admin.site.register(Post)
admin.site.register(comment)