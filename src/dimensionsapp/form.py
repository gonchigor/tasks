from django import forms
from django.views.generic import ListView
from .models import Author, Jenre, PublishingHouse, Serie, FormatBook, Binding, AgeRestriction


class SearchForm(forms.Form):
    search = forms.CharField(label='Наименование', required=False)


class SearchFormAuthor(forms.Form):
    search = forms.CharField(label='Имя', required=False)


class ListViewFilter(ListView):
    form = SearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET:
            context['form'] = self.form({'search': self.request.GET['search']})
        else:
            context['form'] = self.form()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if 'search' in self.request.GET and self.request.GET['search'] != '':
            name = self.request.GET['search']
            qs = qs.filter(name__istartswith=name)
        return qs


class AuthorModel(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class JenreModel(forms.ModelForm):
    class Meta:
        model = Jenre
        fields = '__all__'


class PublishingHouseModel(forms.ModelForm):
    class Meta:
        model = PublishingHouse
        fields = '__all__'


class SerieModel(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'


class FormatBookModel(forms.ModelForm):
    class Meta:
        model = FormatBook
        fields = '__all__'


class BindingModel(forms.ModelForm):
    class Meta:
        model = Binding
        fields = '__all__'


class AgeRestrictionModel(forms.ModelForm):
    class Meta:
        model = AgeRestriction
        fields = '__all__'
