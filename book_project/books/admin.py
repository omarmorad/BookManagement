from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'price', 'appropriate_age', 'get_image')
    list_filter = ('appropriate_age', 'author')
    search_fields = ('title', 'author__name')

    def get_image(self, obj):
        if obj.image:
            return 'Yes'
        return 'No'
    get_image.short_description = 'Has Image'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)