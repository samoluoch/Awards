from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_project, name='upload_project'),
    # url(r'^search/$', views.search_profile, name='search_profile'),
    url(r'^search/$', views.search_project, name='search_project'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
    url(r'^upload/$', views.upload_project, name='upload_image'),
    url(r'^api/projects/$', views.MerchList.as_view()),
    url(r'^api/profiles/$', views.ProfileMerch.as_view()),
    # url(r'^api/merchprofile/$', views.MerchListProfile.as_view())
    # url(r'^rate/project/(\d+)$', views.rate, name='rate'),
    url(r'^post/(?P<project_id>[0-9]+)/review_design/$', views.add_design, name='add_design'),
    url(r'^post/(?P<project_id>[0-9]+)/review_usability/$', views.add_usability, name='review_usability'),
    url(r'^post/(?P<project_id>[0-9]+)/review_content/$', views.add_content, name='review_content'),


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)