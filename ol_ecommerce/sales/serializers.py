from rest_framework import serializers
from sales.models import Product, Order, OrderDetail, Payment, Shipment


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = OrderDetail
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(
        source='get_status_display'
    )

    class Meta:
        model = Payment
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(
        source='get_status_display'
    )

    class Meta:
        model = Shipment
        fields = '__all__'
