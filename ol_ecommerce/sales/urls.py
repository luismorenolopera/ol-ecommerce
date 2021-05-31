from django.urls import path
from sales.views import (
    ProductViewset,
    OrderViewset,
    OrderDetailViewset,
    PaymentViewset,
    ShipmentViewset,
    orders_report,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewset)
router.register('orders', OrderViewset)
router.register('product-order', OrderDetailViewset)
router.register('payments', PaymentViewset)
router.register('shipments', ShipmentViewset)

urlpatterns = [
    path('orders_report', orders_report),
]

urlpatterns += router.urls
