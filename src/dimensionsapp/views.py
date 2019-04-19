from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding, AgeRestriction
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'serie_detail'
        return context


class JenreListView(ListView):
    model = Jenre

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'jenre_detail'
        return context


class PublishingHouseListView(ListView):
    model = PublishingHouse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'publishing_house_detail'
        return context


class FormatBookListView(ListView):
    model = FormatBook

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'format_book_detail'
        return context


class BindingListView(ListView):
    model = Binding

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'binding_detail'
        return context


class AgeRestrictionListView(ListView):
    model = AgeRestriction

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_detail'] = 'age_restriction_detail'
        return context


class AuthorListView(ListView):
    model = Author
