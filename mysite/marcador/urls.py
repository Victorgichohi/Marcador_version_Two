from django.conf.urls import url
# this are the urls for our application

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
