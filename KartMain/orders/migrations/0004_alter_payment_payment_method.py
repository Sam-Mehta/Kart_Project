# Generated by Django 5.0.3 on 2024-06-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderproduct_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('PayPal', 'PayPal'), ('RazorPay', 'RazorPay')], max_length=100),
        ),
    ]
