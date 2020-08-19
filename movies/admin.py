from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'desh', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock',
                    'release_year', 'daily_bhada', 'star')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
