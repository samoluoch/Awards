from django.db import models
from django.contrib.auth.models import User
import numpy as np
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
    def search_project(cls, search_term):
        project = Project.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_profile_projects(cls, profile):
        projects = Project.objects.filter(profile__id=profile)
        return projects

    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_single_project(cls, project_id):
        return cls.objects.get(pk=project_id)

    def average_design(self):
        all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
        return np.mean(all_ratings)

    def average_usability(self):
        all_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(all_ratings)

    def average_content(self):
        all_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return self.title


# class Rate(models.Model):
#     design = models.FloatField(default=0.0)
#     usability = models.FloatField(default=0.0)
#     content = models.FloatField(default=0.0)
#     profile = models.ForeignKey(Profile, related_name='profile_rating')
#     project = models.ForeignKey(Project, related_name='project_rating')
#
#     @classmethod
#     def average_design(cls, project):
#         project_ratings = cls.objects.filter(project=project)
#         rate = [ur.design for ur in project_ratings]
#         mean_design = sum(rate) / len(rate)
#         print(mean_design)
#         return mean_design
#
#     @classmethod
#     def average_usability(cls, project):
#         project_ratings = cls.objects.filter(project=project)
#         rate = [ur.usability for ur in project_ratings]
#         mean_usability = sum(rate) / len(rate)
#         print(mean_usability)
#         return mean_usability
#
#     @classmethod
#     def average_content(cls, project):
#         project_ratings = cls.objects.filter(project=project)
#         rate = [ur.content for ur in project_ratings]
#         mean_content = sum(rate) / len(rate)
#         print(mean_content)
#         return mean_content
#
#
#
#     @property
#     def average_rating(self, null=True):
#         rated = [i for i in [self.design, self.usability,
#                              self.content] if i != None]
#         rating = sum(rated[0:len(rated)]) / len(rated)
#         print(rating)
#         return rating
#
#     @classmethod
#     def get_last_project(cls):
#         return cls.objects.last()


class DesignRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class UsabilityRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class ContentRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)



