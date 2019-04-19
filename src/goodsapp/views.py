from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Menu, Book
# Create your views here.


class MenuList(ListView):
    queryset = Menu.objects.filter(parent_menu__isnull=True)


class BookListView(ListView):
    model = Book
    extra_context = {'menu_list': Menu.objects.all()}


class BookDetailView(DetailView):
    model = Book
