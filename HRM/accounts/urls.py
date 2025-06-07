from django.urls import path
from .views import CustomUserSearchView, UserCreateView, DeleteOrEditUserView, CreateGroupView



urlpatterns = [
    path("users/search/", CustomUserSearchView.as_view(), name="search-users"),
    path("user/register/", UserCreateView.as_view(), name="register-user"),
    path("users/slug:slug/", DeleteOrEditUserView.as_view(), name="user-edit-delete"),
    path("user/create-group/", CreateGroupView.as_view(), name="create-group"),
]
