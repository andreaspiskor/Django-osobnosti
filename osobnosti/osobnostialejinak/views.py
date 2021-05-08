from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):

    return render(request, template_name='index.html')

class OsobnostiListView(ListView):
    model = Osobnosti
    context_object_name = 'osobnosti_list'
    template_name = 'list.html'

class OsobnostiDetailView(DetailView):
    model = Osobnosti
    context_object_name = 'osobnosti'
    template_name = 'detail.html'