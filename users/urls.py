from users.apps import UsersConfig
from django.urls import path
from users.views import UserProfileView

app_name = UsersConfig.name


urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
]