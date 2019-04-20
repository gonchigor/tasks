from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding, AgeRestriction
from dimensionsapp.form import SearchFormAuthor, ListViewFilter
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
    extra_context = {'url_detail': 'serie_detail', 'menu_list': Menu.objects.all()}


class JenreListView(ListViewFilter):
    model = Jenre
    extra_context = {'url_detail': 'jenre_detail', 'menu_list': Menu.objects.all()}


class PublishingHouseListView(ListViewFilter):
    model = PublishingHouse
    extra_context = {'url_detail': 'publishing_house_detail', 'menu_list': Menu.objects.all()}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_detail'] = 'publishing_house_detail'
    #     return context


class FormatBookListView(ListViewFilter):
    model = FormatBook
    extra_context = {'url_detail': 'format_book_detail', 'menu_list': Menu.objects.all()}


class BindingListView(ListViewFilter):
    model = Binding
    extra_context = {'url_detail': 'binding_detail', 'menu_list': Menu.objects.all()}


class AgeRestrictionListView(ListViewFilter):
    model = AgeRestriction
    extra_context = {'url_detail': 'age_restriction_detail', 'menu_list': Menu.objects.all()}


class AuthorListView(ListViewFilter):
    model = Author
    form = SearchFormAuthor
    extra_context = {'url_detail': 'author_detail', 'menu_list': Menu.objects.all()}

    def get_queryset(self):
        qs = super().get_queryset()
        param = self.request.GET.get('pk', 0)
        qs = qs.filter(pk__gte=param)
        return qs


class SerieCreateView(CreateView):
    pass
