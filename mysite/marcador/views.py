from django.shortcuts import render

# displays public bookmarks
from django.shortcuts import get_object_or_404, redirect, render

from .models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.public.all()
    context = {'bookmarks': bookmarks}#bookmarks are stored in a dictionary array
    return render(request, 'marcador/bookmark_list.html', context)
