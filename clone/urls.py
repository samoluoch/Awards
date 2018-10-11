from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^instagram/$',views.instagram,name = 'instagram'),
    url(r'^$',views.home,name = 'home'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_project, name='upload_project'),
    url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
    url(r'^upload/$', views.upload_project, name='upload_image'),
    url(r'^api/merch/$', views.MerchList.as_view())

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)