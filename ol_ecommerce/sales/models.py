from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    image = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.customer.email} : {self.datetime}'


class OrderDetail(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order.id} : {self.product.name}'


class Payment(models.Model):

    class PaymentStatus(models.TextChoices):
        """
        Payment statuses are defined in a similar way as paypal does.
        reference: https://cutt.ly/zndlLsW
        """
        PENDING = 'P'
        ON_HOLD = 'OH'
        REFUNDED = 'R'
        DENIED = 'D'
        COMPLETE = 'C'

    status = models.CharField(
        max_length=2,
        choices=PaymentStatus.choices,
    )
    method = models.CharField(max_length=100)
    order = models.ManyToManyField(Order)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.id} : {self.status}'


class Shipment(models.Model):

    class ShipmentStatus(models.TextChoices):
        SENT = 'S'
        RECEIVED = 'R'

    address = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2,
        choices=ShipmentStatus.choices,
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.order.customer.email}'


@receiver(post_save, sender=Shipment)
def shipping_notification(sender, instance, created, **kwargs):
    if not created:
        order = instance.order.id
        user = instance.order.customer.username
        message = f'{user} your shipment [{order}] has arrived.'
        print(message)
