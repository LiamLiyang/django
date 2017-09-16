from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from app import models
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime



class ForumIndexView(generic.ListView):
    template_name = "sitck/index.html"
    model = models.Sitck



class ForumDetailedView(generic.DetailView):
    template_name = "sitck/detailed.html"
    model = models.Sitck


    def get_object(self, queryset=None):
        post = super(ForumDetailedView, self).get_objects(queryset=None)
        return post

    def get_context_data(self, **kwargs):
        context = super(ForumDetailedView, self).get_context_data(**kwargs)
        com = models.Comment.objects.all().filter(sitck=self.kwargs['pk'])

        context.update({
            'comment_list': eval(com[0].comment_body)if com else ''
        })
        return context

    def post(self, request, *args, **kwargs):
        mode = models.Comment
        this_id = request.POST.get('id', '')
        this_data = request.POST.get('val', '')
        this_user = request.POST.get('user', '')
        mode_data = mode.objects.filter(sitck=self.kwargs['pk'])
        if this_id:
            data = eval(mode_data[0].comment_body)
            user, data1 = this_data.split('@')[1].split('\t')
            data[int(this_id)]['next'].append(
                {'to':user, 'user':this_user,
                 'context':data1, 'date':datetime.datetime.now()})
            mode_data.update(comment_body=data)
        else:
            if not mode_data:
                mode.objects.create(sitck_id=self.kwargs['pk'],comment_body=[{'user':this_user, 'context':this_data, 'date':datetime.datetime.now(), 'next':[], 'index':0}])
            else:
                data = eval(mode_data[0].comment_body)
                data.append({'to':mode_data[0].sitck.user.first_name, 'user':this_user, 'context':this_data, 'date':datetime.datetime.now(), 'next':[], 'index':len(data)})
                mode_data.update(comment_body=data)
        return HttpResponseRedirect(reverse('app:detailed', kwargs={'pk': self.kwargs['pk']}))









class SortdView(generic.ListView):
    template_name = "sitck/index.html"
    model = models.Sitck

    def get_queryset(self):
        """
        重载get_queryset 方法
        :return:
        """
        return super(SortdView, self).get_queryset().filter(cfn=self.kwargs['pk'])




