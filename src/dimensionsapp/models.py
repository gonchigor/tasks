from django.db import models

# Create your models here.
class Dimension(models.Model):
    name = models.CharField("Наименование", max_length=50, )
    description = models.TextField("Описание", blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']



class Author(Dimension):
    biography = models.TextField("Биография", blank=True, )
    class Meta(Dimension.Meta):
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Serie(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class Jenre(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class PublishingHouse(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class FormatBook(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'

class Binding(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'Переплет'
        verbose_name_plural = 'Переплеты'


