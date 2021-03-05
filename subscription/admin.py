from django.contrib import admin
from .models import Subscription
# from checkout.models import Order, OrderLineItem


# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ['get_order_number', 'get_full_name',
                       'get_email', 'get_date',
                       'get_phone_number', 'get_country',
                       'get_postcode', 'get_town_or_city',
                       'get_street_address1', 'get_street_address2',
                       'get_county']

    def get_order_number(self, subscription):
        return subscription.order.order_number

    def get_full_name(self, subscription):
        return subscription.order.full_name

    def get_email(self, subscription):
        return subscription.order.email

    def get_date(self, subscription):
        return subscription.order.date.strftime("%Y-%m-%d, %H:%M:%S")

    def get_phone_number(self, subscription):
        return subscription.order.phone_number

    def get_country(self, subscription):
        return subscription.order.country

    def get_postcode(self, subscription):
        return subscription.order.postcode

    def get_town_or_city(self, subscription):
        return subscription.order.town_or_city

    def get_street_address1(self, subscription):
        return subscription.order.street_address1

    def get_street_address2(self, subscription):
        return subscription.order.street_address2

    def get_county(self, subscription):
        return subscription.order.county


admin.site.register(Subscription, SubscriptionAdmin)
