from django.contrib import admin
from product.views import Product,Category,Review,ProductImage
# Register your models here.
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)