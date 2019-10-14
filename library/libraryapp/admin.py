from django.contrib import admin
from .models import Book, Author, Member, Book_issue


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'price', 'availabel', 'isbn', 'author', 'number_of_books', 'availabel_of_books')
    search_fields = ['book_name']
    ordering = ['price']


admin.site.register(Book, BookAdmin),
admin.site.register(Author),


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')


admin.site.register(Member, MemberAdmin)


class Book_issueAdmin(admin.ModelAdmin):
    list_display = ('date', 'return_date')


admin.site.register(Book_issue, Book_issueAdmin),
