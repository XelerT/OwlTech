from django.db import models
from django.conf import settings
from django.utils import timezone


class PurchaseList(models.Model):

    # user == who bought
    # purchases == product

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name="user")
    purchases = models.ManyToManyField(settings.AUTH_PRODUCT_MODEL, blank=True,
                                       related_name="purchases")

    def __str__(self):
        return self.user.username

    def add_purchase(self, product):
        if not product in self.purchases.all():
            if self.user.money >= product.product_cost:
                self.user.money -= product.product_cost
                self.purchases.add(product)
                self.save()


class PurchaseRequest(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="buyer")
    item = models.ForeignKey(settings.AUTH_PRODUCT_MODEL,
                             on_delete=models.CASCADE, related_name="item")
    is_active = models.BooleanFiels(blanck=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.buyer.username
    # sender = buyer
    # receiver = item
    def buy(self):
        item_purchase_list = PurchaseList.objects.get(purchases=self.buyer)
        if item_purchase_list:
            item_purchase_list.add_purchase(self.buyer)
            buyer_purchase_list = PurchaseList.objects.get(user=self.buyer)
            if buyer_purchase_list:
                buyer_purchase_list.add_purchase(self.item)
                self.is_active = False
                self.save()
