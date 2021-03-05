# Generated by Django 3.1.5 on 2021-03-05 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
        ('profiles', '0001_initial'),
        ('subscription', '0004_subscription_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='checkout.order'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription', to='profiles.userprofile'),
        ),
    ]