from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Menu
# Create your views here.


class MenuList(ListView):
    queryset = Menu.objects.filter(parent_menu__isnull=True)
