from django.contrib import admin

from .models import Book, Author, Category, Address, Country


class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = { "slug": ('title', ) }
  list_display = ('title', 'author', 'rating')
  list_filter = ('author', 'rating')
  # readonly_fields = ('slug', )


class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Country)
