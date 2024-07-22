from django.contrib import admin
from .models import Author, Genre, Audiobook, Review
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Audiobook)
admin.site.register(Review)
# Register your models here.
