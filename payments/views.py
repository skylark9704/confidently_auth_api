from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from payments.lib.payments import create_subscription, get_invoices

import json


class CreateSubscription(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        customer_id = data['customerId']
        payment_method_id = data['paymentMethodId']
        price_id = data['priceId']

        subscription = create_subscription(
            customer_id=customer_id,
            payment_method_id=payment_method_id,
            price_id=price_id
        )
        return Response(subscription)


class GetInvoices(APIView):

    def get(self, request):

        payload = {"invoices": [0, 1, 2, 3, 4, 5]}

        return Response(payload)
