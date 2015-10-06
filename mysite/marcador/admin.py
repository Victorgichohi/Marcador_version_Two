from django.contrib import admin

from .models import Bookmark, Tag

#these displays the various fields as stated
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')#These fields will be shown in the list view
    list_editable = ('is_public',)#These fields are editable in the list view .
    list_filter = ('is_public', 'owner__username')#These fields can be filtered in the list view based on their values.
    #These fields can be searched for in the list view based on their values. A search field will be shown above the list.
    search_fields = ['url', 'title', 'description']
    readonly_fields = ('date_created', 'date_updated')# These fields are not editable in the detail view.


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
