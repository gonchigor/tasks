from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding, AgeRestriction
from goodsapp.models import Menu
# Create your views here.


class AuthorDetailView(DetailView):
    model = Author


class SerieDetailView(DetailView):
    model = Serie


class JenreDetailView(DetailView):
    model = Jenre


class PublishingHouseDetailView(DetailView):
    model = PublishingHouse


class FormatBookDetailView(DetailView):
    model = FormatBook


class BindingDetailView(DetailView):
    model = Binding


class AgeRestrictionDetailView(DetailView):
    model = AgeRestriction


class SerieListView(ListView):
    model = Serie
    extra_context = {'url_detail': 'serie_detail', 'menu_list': Menu.objects.all()}


class JenreListView(ListView):
    model = Jenre
    extra_context = {'url_detail': 'jenre_detail', 'menu_list': Menu.objects.all()}


class PublishingHouseListView(ListView):
    model = PublishingHouse
    extra_context = {'url_detail': 'publishing_house_detail', 'menu_list': Menu.objects.all()}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_detail'] = 'publishing_house_detail'
    #     return context


class FormatBookListView(ListView):
    model = FormatBook
    extra_context = {'url_detail': 'format_book_detail', 'menu_list': Menu.objects.all()}


class BindingListView(ListView):
    model = Binding
    extra_context = {'url_detail': 'binding_detail', 'menu_list': Menu.objects.all()}


class AgeRestrictionListView(ListView):
    model = AgeRestriction
    extra_context = {'url_detail': 'age_restriction_detail', 'menu_list': Menu.objects.all()}


class AuthorListView(ListView):
    model = Author
    extra_context = {'url_detail': 'author_detail', 'menu_list': Menu.objects.all()}
