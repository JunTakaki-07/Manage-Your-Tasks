from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Myassignment
from django.urls import reverse_lazy



# Create your views here.
from django.views.generic import ListView
from .models import Myassignment


def is_tasklist(request):
    object_list = Myassignment.objects.all()
    return render(request, 'list.html', {'object_list':object_list})



def is_detail(request, pk):
    object = Myassignment.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})


class Is_delete(DeleteView):
    template_name = 'delete.html'
    model = Myassignment
    success_url = reverse_lazy('tasklist')



class Is_create(CreateView):
    template_name = 'create.html'
    model = Myassignment
    fields = ("task_name", "task_description", "task_purpose", "task_key_goal_indicators")
    success_url = reverse_lazy('tasklist')


class Is_update(UpdateView):
    template_name = 'update.html'
    model = Myassignment
    fields = ("task_name", "task_description", "task_purpose", "task_key_goal_indicators")
    success_url = reverse_lazy('tasklist')



