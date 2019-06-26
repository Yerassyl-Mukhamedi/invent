from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

def post_list(request):
    posts = Worker.objects.order_by('job')
    return render(request, 'blog/post_list.html', {'posts': posts})

def specific(request):
    posts = Worker.objects.order_by('job')
    return render(request, 'blog/specific.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Worker, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})