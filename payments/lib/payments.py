import stripe

stripe.api_key = 'sk_test_51H9PmEALgFhcfNxqNRIqD9ue2kWcJGNN5Kp4u0pJDsU3isNkgbvCUoAxdMoWzkXGXAO7V6DMc6ITPdzG7zaXL0oj00CUQd7HXS'


def create_subscription(customer_id, price_id, payment_method_id):
    try:

        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=customer_id
        )
        # Set the default payment method on the customer
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method': payment_method_id,
            },
        )

        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'price': price_id
                }
            ],
            expand=['latest_invoice.payment_intent'],
        )
        print('Subscription ', subscription)
        return subscription
    except Exception as e:
        print(e)
        return {"error": {"status": True, "message": "Subscription creation failed"}}


def get_invoices(customer_id):
    pass
