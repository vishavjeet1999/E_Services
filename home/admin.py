from django.contrib import admin
from .models import user_services, category, Comments

# Register your models here.
admin.site.register(user_services)
admin.site.register(category)
admin.site.register(Comments)
