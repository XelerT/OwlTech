from django.db import models
from django.contrib.postgres.fields import ArrayField
from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
# from tinymce.widgets import TinyMCE

class ProductManager():

    def create_product(self, product_name, product_descr):
        if not product_name:
            raise ValueError("Product must have name")
        if not product_descr:
            raise ValueError("Product must have a description")

        product = self.model(
            product_name=product_name,
            product_descr=product_descr,
        )
        product.save(using=self._db)
        return product


def get_product_image_filepath(self, filename):
    return f'product_image/{self.pk}/{product_image.png}'

def get_default_product_image():
    return "media_cdn/default_product.png"

def product_directory_path(self,filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'product_{0}/{1}'.format(self.id, filename)

class Product(models.Model):

    product_name    = models.CharField(max_length=100, unique=True)
    product_descr   = models.CharField(max_length=250)
    date_created    = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    product_image   = models.ImageField(max_length=255, upload_to=get_product_image_filepath, null=True, blank=True, default=get_default_product_image)
    product_cost    = models.FloatField(default=0)
    product_type    = models.CharField(max_length=100)
    product_creator = models.CharField(max_length=50)
    product_video   = EmbedVideoField(default='https://www.youtube.com/watch?v=SlLIEU2e7BA')
    product_file    = models.FileField(upload_to=product_directory_path, null=True)
    content         = RichTextField()
    content_tiny    = models.TextField()


    def __str__(self):
        return self.product_name
