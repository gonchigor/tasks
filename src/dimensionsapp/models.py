from django.db import models

# Create your models here.
class Dimension(models.Model):
    name = models.CharField("Наименование", max_length=50, unique=True)
    description = models.TextField("Описание", blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']



class Author(Dimension):
    biography = models.TextField("Биография", blank=True, )
    class Meta(Dimension.Meta):
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Serie(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'серия'
        verbose_name_plural = 'серии'


class Jenre(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class PublishingHouse(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'издательство'
        verbose_name_plural = 'издательства'


class FormatBook(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'формат'
        verbose_name_plural = 'форматы'

class Binding(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = 'переплет'
        verbose_name_plural = 'переплеты'


class AgeRestriction(Dimension):
    class Meta(Dimension.Meta):
        verbose_name = "возрастное ограничение"
        verbose_name_plural = "возрастные ограничения"
        ordering = []