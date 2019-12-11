from django.contrib import admin

from sub.models import Contact, Category, Product, Substitute


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Substitute)

