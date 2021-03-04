from django.contrib import admin
from .models import Subscription


# Register your models here.

admin.site.register(Subscription)


class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ['get_full_name']

    def get_full_name(self, subscription):
        return subscription.order.full_name

