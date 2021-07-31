from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'tag', 'title', 'content', 'created_at',
                    'published_at', 'updated_at', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Tag)
