# Generated by Django 5.1.4 on 2024-12-31 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tansaction_id',
            new_name='transaction_id',
        ),
    ]
