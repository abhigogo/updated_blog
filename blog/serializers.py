from rest_framework import serializers
from .models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('title','created_date','published_date')

