from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin
from .models import Author, Book

author_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class BookInline(TabularDynamicInlineAdmin):
    model = Book

class AuthorAdmin(DisplayableAdmin):
    inlines = (BookInline,)
    fieldsets = deepcopy(DisplayableAdmin.fieldsets) + author_extra_fieldsets

admin.site.register(Author, AuthorAdmin)
# Register your models here.
