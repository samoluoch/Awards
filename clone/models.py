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

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class Project(models.Model):
    '''
    This is project class model
    '''
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='image/', null=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User)
    url = models.URLField(max_length =100)
    rating = models.TextField()
    # likes = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()


    def delete_project(self):
        self.delete()

    def update_caption(self):
        self.save()

    def get_project_id(cls, id):
        project = Project.objects.get(pk=id)
        return project

    class Meta:
        ordering = ('-pub_date',)

    @classmethod
    def search_profile(cls, search_term):
        profiles = cls.objects.filter(profile__icontains=search_term)
        return profiles

    @classmethod
    def get_profile_projects(cls, profile):
        projects = Project.objects.filter(profile__id=profile)
        return projects

    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects

    def __str__(self):
        return self.title


class Rate(models.Model):
    design = models.FloatField(default=0.0)
    usability = models.FloatField(default=0.0)
    content = models.FloatField(default=0.0)
    profile = models.ForeignKey(Profile, related_name='profile_rating')
    project = models.ForeignKey(Project, related_name='project_rating')
