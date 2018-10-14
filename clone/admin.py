from django.contrib import admin
from .models import Project,Profile,DesignRating,ContentRating,UsabilityRating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(DesignRating)
admin.site.register(ContentRating)
admin.site.register(UsabilityRating)
