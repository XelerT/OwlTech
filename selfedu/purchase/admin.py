from django.contrib import admin

from purchase.models import PurchaseRequest, PurchaseList

class PurchaseListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_product = ['user']
    readonly_fields = ['user']

    class Meta:
        model = FriendList

admin.site.register(PurchaseList, PurchaseListAdmin)
