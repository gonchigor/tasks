from goodsapp.models import Book
from dimensionsapp.models import *


def create_author(data):
    aut = Author(name=data['name'])
    if 'description' in data.keys():
        aut.description = data['description']
    if 'biography' in data.keys():
        aut.biography = data['biography']
    aut.save()


def delete_author(id):
    try:
        if type(id) == int:
            aut = Author.objects.get(id=id)
        else:
            aut = Author.objects.get(name=id)
        aut.delete()
    except Author.DoesNotExist:
        print(id, 'doesn\'t find')


def count_authors(name=None):
    if name is None:
        return Author.objects.count()
    return Author.objects.filter(name__startswith=name).count()


def update_authors(data):
    name = data.pop("name")
    return Author.objects.update_or_create(name=name, defaults=data)


def bulk_create_authors(count, default_name):
    list = [Author(name=default_name + str(i)) for i in range(1, count + 1)]
    return Author.objects.bulk_create(list)


def author_book(author):
    if type(author) == str:
        author = Author.objects.get(name=author)
    return author.book_set.all()


def print_author_book(author):
    for book in author_book(author):
        print(book.description())


class ObjUtil:
    def __init__(self, model_class):
        self.model_class = model_class

    def create(self, data):
        aut = self.model_class(name=data['name'])
        if 'description' in data.keys():
            aut.description = data['description']
        aut.save()

    def bulk_create(self, count, default_name):
        list = [self.model_class(name=default_name + str(i)) for i in range(1, count + 1)]
        self.model_class.objects.bulk_create(list)

    def count(self, name=None):
        if name is None:
            return self.model_class.objects.count()
        return self.model_class.objects.filter(name__startswith=name).count()

    def delete(self, id):
        try:
            if type(id) == int:
                aut = self.model_class.objects.get(id=id)
            else:
                aut = self.model_class.objects.get(name=id)
            aut.delete()
        except self.model_class.DoesNotExist:
            print(id, 'doesn\'t find')

    def update(self, data):
        di = data.copy()
        name = di.pop("name")
        return self.model_class.objects.update_or_create(name=name, defaults=di)

    def get_or_create(self, data):
        di = data.copy()
        name = di.pop("name")
        return self.model_class.objects.get_or_create(name=name, defaults=di)


def create_book(book_dict):
    book = Book(name=book_dict['name'],
                price=book_dict['price'],
                year_publishing=book_dict['year_publishing'],
                count_pages=book_dict['count_pages'],
                isbn=book_dict['isbn'],
                weight=book_dict['weight'],
                count_books=book_dict['count_books'],
                is_active=book_dict['is_active'],
                rate=book_dict['rate'])
    serie_obj, created = ObjUtil(Serie).update(book_dict['serie'])
    book.serie = serie_obj
    binding_obj, created = ObjUtil(Binding).get_or_create(book_dict['binding'])
    book.binding = binding_obj
    book.format_book = ObjUtil(FormatBook).get_or_create(book_dict['format_book'])[0]
    book.age_restrictions = ObjUtil(AgeRestriction).get_or_create(
        book_dict['age_restrictions'])[0]
    book.publisher = ObjUtil(PublishingHouse).get_or_create(
        book_dict['publisher'])[0]
    book.save()
    aut_gen = ObjUtil(Author)
    for author in book_dict['authors']:
        aut_obj, created = aut_gen.get_or_create(author)
        book.authors.add(aut_obj)
    jen_gen = ObjUtil(Jenre)
    for jenre in book_dict['jenre']:
        jen_obj, created = jen_gen.update(jenre)
        book.jenre.add(jen_obj)
    book.save()
