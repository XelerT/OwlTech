from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=50);
    subtitle = models.CharField('Краткое описание', max_length=250);
    text = models.TextField('Основной текст');

    date = models.DateTimeField('Дата и время публикации');

    def __str__(self):
        return self.title

