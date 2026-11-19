from django.contrib import admin
from .models import Articles, Category

# Register your models here.


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
  filter_horizontal = ('categories',)


admin.site.register(Category)
