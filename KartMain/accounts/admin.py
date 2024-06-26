from django.contrib import admin

from .models import UserProfile,Account
from orders.models import Payment,Order,OrderProduct
from store.models import Product,Variation,ReviewRating,ProductGallery


admin.site.register(UserProfile)
admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)

