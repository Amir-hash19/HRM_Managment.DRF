from django.urls import path
from .views import CustomUserSearchView



urlpatterns = [
    path("users/search/", CustomUserSearchView.as_view(), name="search-users"),
]
