from django.conf.urls import include, url
from django.contrib import admin
from app import views
urlpatterns = [
    # Examples:
    url(r'^$', views.ForumIndexView.as_view(), name='home'),
    url(r'^detailed$', views.ForumDetailedView.as_view(), name='detailed'),
    # url(r'^blog/', include('blog.urls')),
]
