from django.contrib import admin
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBag, Purchase

class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'registrated_at')

class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'registrated_at')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'store_category')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'category', 'price', 'quantity', 'info', 'store')

class MyBagAdmin(admin.ModelAdmin):
    list_display = ('customer', 'items', 'total_price')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('items', 'buy_time', 'customer', 'total_price')

admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyBag, MyBagAdmin)
admin.site.register(Purchase, PurchaseAdmin)
