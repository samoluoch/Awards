from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

    # @classmethod
    # def search_profile(cls, name):
    #     profile = Profile.objects.filter(user__username__icontains=name)
    #     return profile
    #
    # @classmethod
    # def get_by_id(cls, id):
    #     profile = Profile.objects.get(user=id)
    #     return profile
    #
    # @classmethod
    # def filter_by_id(cls, id):
    #     profile = Profile.objects.filter(user=id).first()
    #     return profile