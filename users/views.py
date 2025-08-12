from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from users.models import Payment
from users.serializer import PaymentSerializer


class UserProfileView(DetailView):
    pass


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['payment_date']
    ordering = ['payment_date']
