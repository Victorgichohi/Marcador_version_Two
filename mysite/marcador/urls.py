from django.conf.urls import url
# this are the urls for our application

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
        #The pattern ^edit/(?<pk>\d+)/$
        #has a variable part which catches the primary key (PK) of a bookmark.
        #The PK is added to every model by Django, so every entry gets a unique identifier.
        # The path /edit/1/ for example leads to the bookmark with the PK 1.
         url(r'^create/$', 'marcador.views.bookmark_create',
        name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'marcador.views.bookmark_edit',
        name='marcador_bookmark_edit'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
