# Generated by Django 3.2.5 on 2021-10-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='Img/', verbose_name='Картинка'),
        ),
    ]
