from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

def post_list(request):
    posts = Worker.objects.order_by('job')
    blogs = Laptop.objects.filter(name='HP Pavilion').values_list('worker', flat=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'blogs': blogs })

def post_detail(request, pk):
    post = get_object_or_404(Worker, pk=pk)
    notebooks = Laptop.objects.order_by('name')
    printers = Printer.objects.order_by('name')
    return render(request, 'blog/post_detail.html', {'post': post, 'notebooks': notebooks, 'printers': printers})