from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from django.urls import path
from users.views import UserProfileView, PaymentViewSet, UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')


urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListAPIView.as_view(), name='users_list'),
    path('update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('destroy/', UserDestroyAPIView.as_view(), name='user_destroy'),
]

urlpatterns += router.urls