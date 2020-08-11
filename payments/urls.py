from django.urls import path
from payments.views import CreateSubscription, GetInvoices

urlpatterns = [
    path('subscription/create', CreateSubscription.as_view()),
    path('invoices', GetInvoices.as_view())
]
