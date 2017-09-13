from django.conf.urls import include, url
from django.contrib import admin
from app import views
urlpatterns = [
    # Examples:
    url(r'^$', views.ForumIndexView.as_view(), name='home'),
    url(r'^detailed/(?P<pk>[0-9]+)/', views.ForumDetailedView.as_view(), name='detailed'),
    # url(r'^detailed_post/', views.RecordInterest.as_view(), name='record'),
    url(r'^sort/(?P<pk>[0-9]+)/', views.SortdView.as_view(), name='sort'),
    # url(r'^blog/', include('blog.urls')),
]
