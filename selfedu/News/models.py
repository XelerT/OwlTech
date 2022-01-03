from django.db import models
from django import forms
from PIL import Image

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)
# Create your models here.
class Article(models.Model):
    title = models.CharField('Название', max_length=50);
    subtitle = models.CharField('Краткое описание', max_length=250);
    text = models.TextField('Основной текст');
    image_News = models.ImageField(upload_to=upload_location, null = True, blank = True, height_field="height_field", width_field="width_field");
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    date = models.DateTimeField('Дата и время публикации');

    def __str__(self):
        return self.title
