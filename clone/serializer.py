from rest_framework import serializers
from .models import Profile, Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'user', 'photo')


    class Meta:
        model = Project
        fields = ('image', 'description', 'url')

