from asgiref.sync import sync_to_async
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from sales.models import Product, Order, OrderDetail, Payment, Shipment
from sales.reports.orders import orders_paid_or_sent
from sales.serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderDetailSerializer,
    PaymentSerializer,
    ShipmentSerializer,
)


class ProductViewset(viewsets.ModelViewSet):
    """
    Viewset for Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewset(viewsets.ModelViewSet):
    """
    Viewset for Order model.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewset(viewsets.ModelViewSet):
    """
    Viewset for OrderDetail model.
    """
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class PaymentViewset(viewsets.ModelViewSet):
    """
    Viewset for Payment model.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ShipmentViewset(viewsets.ModelViewSet):
    """
    Viewset for Shipment model.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


@sync_to_async
@api_view(['GET'])
@permission_classes([IsAdminUser])
def orders_report(request):
    orders = orders_paid_or_sent()
    return Response(orders)
