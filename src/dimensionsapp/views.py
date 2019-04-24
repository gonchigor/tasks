from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding,\
    AgeRestriction
from dimensionsapp.form import SearchFormAuthor, ListViewFilter, AuthorModel, JenreModel, SerieModel,\
    PublishingHouseModel, FormatBookModel, BindingModel, AgeRestrictionModel
from django.views.generic import TemplateView
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


class SerieListView(ListViewFilter):
    model = Serie
    extra_context = {'url_detail': 'serie_detail'}


class JenreListView(ListViewFilter):
    model = Jenre
    extra_context = {'url_detail': 'jenre_detail'}


class PublishingHouseListView(ListViewFilter):
    model = PublishingHouse
    extra_context = {'url_detail': 'publishing_house_detail'}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_detail'] = 'publishing_house_detail'
    #     return context


class FormatBookListView(ListViewFilter):
    model = FormatBook
    extra_context = {'url_detail': 'format_book_detail'}


class BindingListView(ListViewFilter):
    model = Binding
    extra_context = {'url_detail': 'binding_detail', }


class AgeRestrictionListView(ListViewFilter):
    model = AgeRestriction
    extra_context = {'url_detail': 'age_restriction_detail'}


class AuthorListView(ListViewFilter):
    model = Author
    form = SearchFormAuthor
    extra_context = {'url_detail': 'author_detail'}


class MenuView(TemplateView):
    template_name = 'goodsapp/menu_view.html'


class SerieCreateView(CreateView):
    model = Serie
    form_class = SerieModel


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorModel


class JenreCreateView(CreateView):
    model = Jenre
    form_class = JenreModel


class PublishingHouseCreateView(CreateView):
    model = PublishingHouse
    form_class = PublishingHouseModel


class FormatBookCreateView(CreateView):
    model = FormatBook
    form_class = FormatBookModel


class BindingCreateView(CreateView):
    model = Binding
    form_class = BindingModel


class AgeRestrictionCreateView(CreateView):
    model = AgeRestriction
    form_class = AgeRestrictionModel
