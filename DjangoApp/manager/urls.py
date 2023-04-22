from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('documents/', views.documents, name='documents'),
   path('<id>/document_detail/', views.document_detail, name='document_detail'),
   re_path(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
   re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),
]