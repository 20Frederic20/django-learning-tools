from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create_post'),
    path('<uuid:uuid>/show', views.show_post, name="show_post"),
    path('<uuid:uuid>/share', views.share_post, name="share_post"),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
