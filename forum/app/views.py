from django.shortcuts import render
from django.views import generic
# Create your views here.


class ForumIndexView(generic.TemplateView):
    template_name = "base.html"
