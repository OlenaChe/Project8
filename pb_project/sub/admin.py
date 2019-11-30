from django.contrib import admin

from sub.models import Contact, Category, Product, Substitute

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Substitute)

