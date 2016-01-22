from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    Context = {"form": SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html',Context)