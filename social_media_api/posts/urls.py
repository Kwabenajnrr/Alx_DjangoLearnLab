from django.urls import path
from .views import feed, like_post, unlike_post

urlpatterns = [
    path('feed/', feed),
    path('<int:pk>/like/', like_post),
    path('<int:pk>/unlike/', unlike_post),
    path('<int:pk>/like/', like_post),
    path('<int:pk>/unlike/', unlike_post),
]

