from django.contrib import admin

from purchase.models import PurchaseRequest, PurchaseList

class PurchaseListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_product = ['user']
    readonly_fields = ['user']

    class Meta:
        model = PurchaseList

admin.site.register(PurchaseList, PurchaseListAdmin)

class PurchaseRequestAdmin(admin.ModelAdmin):
    list_filter = ['buyer', 'item']
    list_display = ['buyer', 'item']
    search_fields = ['buyer__username', 'buyer__email', 'item__product_name']

    class Meta:
        modal = PurchaseRequest

admin.site.register(PurchaseRequest, PurchaseRequestAdmin)
