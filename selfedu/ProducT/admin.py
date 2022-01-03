from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Product
from tinymce.widgets import TinyMCE
from django.db import models

class tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):

	list_display=["product_name"]
	formfield_overrides ={models.TextField: {'widget': TinyMCE()}}

admin.site.register(Product, tutorialAdmin)
