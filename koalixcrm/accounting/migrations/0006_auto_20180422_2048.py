# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-22 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoUserExtension', '0004_auto_20171210_2126'),
        ('accounting', '0005_auto_20171110_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['account_number'], 'verbose_name': 'Account', 'verbose_name_plural': 'Account'},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountNumber',
            new_name='account_number',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountType',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='isACustomerPaymentAccount',
            new_name='is_a_customer_payment_account',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='isopeninterestaccount',
            new_name='is_open_interest_account',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='isopenreliabilitiesaccount',
            new_name='is_open_reliabilities_account',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='isProductInventoryActiva',
            new_name='is_product_inventory_activa',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='accountingPeriod',
            new_name='accounting_period',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bookingDate',
            new_name='booking_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bookingReference',
            new_name='booking_reference',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='fromAccount',
            new_name='from_account',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='toAccount',
            new_name='to_account',
        ),
        migrations.RenameField(
            model_name='productcategorie',
            old_name='lossAccount',
            new_name='loss_account',
        ),
        migrations.RenameField(
            model_name='productcategorie',
            old_name='profitAccount',
            new_name='profit_account',
        ),
        migrations.AddField(
            model_name='accountingperiod',
            name='template_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoUserExtension.DocumentTemplate', verbose_name='Referred Template'),
        ),
    ]
