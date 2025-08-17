from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from django.urls import path
from users.views import UserProfileView, PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')


urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
]

urlpatterns += router.urls