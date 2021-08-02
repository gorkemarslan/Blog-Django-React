from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, HelloWorldView

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="register"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('hello/', HelloWorldView.as_view(), name='hello_world')
]