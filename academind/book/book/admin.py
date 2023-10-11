from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = { "slug": ('title', ) }
  list_display = ('title', 'author', 'rating')
  list_filter = ('author', 'rating')
  # readonly_fields = ('slug', )

admin.site.register(Book, BookAdmin)

