from rest_framework import serializers
from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'payment_date',
            'paid_course',
            'paid_lesson',
            'payment_amount',
            'payment_method',
            'payment_method_display'
        ]

class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']