from django.contrib.auth.models import User
from django.db import models

class StoreCategory(models.Model):
    name = models.CharField(max_length=70)
    picture = models.ImageField(upload_to='store_category_images/')
    
    def __repr__(self):
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=70)
    picture = models.ImageField(upload_to='item_category_images/')
    
    def __repr__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer_avatar/')
    registrated_at = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return self.user.username

class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='store_owner_avatar/')
    registrated_at = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return self.user.username

class Store(models.Model):
    name = models.CharField(max_length=70)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    
    def __repr__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=70)
    picture = models.ImageField(upload_to='item_images/')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    info = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    def __repr__(self):
        return self.name
   
class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        return str(self.id)

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        return str(self.id)