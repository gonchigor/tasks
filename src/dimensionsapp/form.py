from django import forms
from django.views.generic import ListView


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
            qs = qs.filter(name__startswith=name)
        return qs
