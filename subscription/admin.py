from django.contrib import admin
from .models import Subscription


# from checkout.models import Order, OrderLineItem


# Register your models here.


    # Code about how to make readonly_fields with ModelAdmin comes from:
    # https://stackoverflow.com/questions/44718355/how-show-related-object-in-django-admin-from-the-model-with-a-foreign-key-point#44725212
# class SubscriptionAdmin(admin.ModelAdmin):
#     readonly_fields = ['get_order_number', 'get_full_name',
#                        'get_email', 'get_date',
#                        'get_phone_number', 'get_street_address1',
#                        'get_street_address2', 'get_town_or_city',
#                        'get_postcode', 'get_county', 'get_country']

#     def get_order_number(self, subscription):
#         return subscription.order.order_number

#     def get_full_name(self, subscription):
#         return subscription.order.full_name

#     def get_email(self, subscription):
#         return subscription.order.email

#     def get_date(self, subscription):
#         # Code about how to format date comes from:
#         # https://www.programiz.com/python-programming/datetime/strftime
#         return subscription.order.date.strftime("%Y-%m-%d, %H:%M:%S")

#     def get_phone_number(self, subscription):
#         return subscription.order.phone_number

#     def get_street_address1(self, subscription):
#         return subscription.order.street_address1

#     def get_street_address2(self, subscription):
#         return subscription.order.street_address2

#     def get_town_or_city(self, subscription):
#         return subscription.order.town_or_city

#     def get_postcode(self, subscription):
#         return subscription.order.postcode

#     def get_county(self, subscription):
#         return subscription.order.county

#     def get_country(self, subscription):
#         return subscription.order.country


admin.site.register(Subscription)

# SubscriptionAdmin