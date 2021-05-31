"""
In this file the reports related to the purchase orders are added.
"""
from django.db import connection


def orders_paid_or_sent():
    """
    Retrieve orders that have been paid or shipped.
    """
    with connection.cursor() as cursor:
        sql = """
            SELECT
                sales_order."id" AS order_id,
                auth_user.first_name,
                auth_user.last_name,
                sales_order.datetime
            FROM
                sales_order
                INNER JOIN sales_shipment ON sales_order."id" = sales_shipment.order_id
                INNER JOIN sales_payment_order ON sales_order."id" = sales_payment_order.order_id
                INNER JOIN sales_payment ON sales_payment_order.payment_id = sales_payment."id"
                INNER JOIN auth_user ON sales_order.customer_id = auth_user."id"
            WHERE
                sales_payment.status = 'C'
                OR sales_shipment.status = 'S'
            """
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
