from django.contrib import admin

from .models import Register, Profile, Quote

admin.site.register(Register)
admin.site.register(Profile)
admin.site.register(Quote)