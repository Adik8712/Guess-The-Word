from django.contrib import admin
from .models import Word, Room, GuessedWord


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'is_guessed', 'creator', 'created_at')
    list_filter = ('is_guessed', 'creator')
    search_fields = ('word', 'creator__username')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('word', 'is_guessed')
        }),
        ('Additional Information', {
            'fields': ('creator', 'created_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'creator', 'is_closed', 'created_at')
    list_filter = ('is_closed', 'creator')
    search_fields = ('word__word', 'creator__username')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('word', 'is_closed')
        }),
        ('Additional Information', {
            'fields': ('creator', 'created_at'),
            'classes': ('collapse',) 
        }),
    )


@admin.register(GuessedWord)
class GuessedWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'is_similar', 'word_id', 'creator', 'room', 'created_at')
    list_filter = ('creator', 'room')
    search_fields = ('word', 'creator__username')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('word', 'word_id', 'room', 'creator')
        }),
        ('Other Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)  
        }),
    )
