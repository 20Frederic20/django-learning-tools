from django.urls import path

from .views import index, show, share

app_name="blog"

urlpatterns = [
    path('', index, name='index'),
    path('<uuid:uuid>/show', show, name="show"),
    path('<uuid:uuid>/share', share, name="share")
]
