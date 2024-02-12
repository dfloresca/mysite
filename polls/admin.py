from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Song, Artist, Album
# admin.site.register(Question)
# admin.site.register(Choice)



class SongInline(admin.TabularInline):
    model=Song
    extra=3


class AlbumAdminInline(admin.TabularInline):
    model=Album
    extra=3

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['title']})
    ]
    inlines=[SongInline]
    list_display = ["title","artist"]
    list_filter=['title','artist__name']
    search_fields = [ "title" ,  "artist__name"]
class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['name']})
    ]
    inlines = [AlbumAdminInline]
    list_display = ['name']
    search_fields = [ 'name' ]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['question_text'] }),
        ("Date information", {"fields":["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)