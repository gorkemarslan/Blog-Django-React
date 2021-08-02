from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list'),
]
