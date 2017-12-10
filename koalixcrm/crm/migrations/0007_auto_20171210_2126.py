# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoUserExtension', '0004_auto_20171210_2126'),
        ('crm', '0006_auto_20171210_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextParagraphInDocumentTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('BS', 'Before subject'), ('AS', 'After subject'), ('BT', 'Before total'), ('AT', 'After total'), ('BW', 'Before wishes'), ('AW', 'After wishes'), ('C1', 'Custom 1'), ('C2', 'Custom 2'), ('C3', 'Custom 3'), ('C4', 'Custom 4')], max_length=2, verbose_name='Purpose')),
                ('text_paragraph', models.TextField(verbose_name='Text')),
                ('document_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoUserExtension.DocumentTemplate')),
            ],
            options={
                'verbose_name': 'TextParagraphInDocumentTemplate',
                'verbose_name_plural': 'TextParagraphInDocumentTemplates',
            },
        ),
        migrations.AlterField(
            model_name='textparagraphinsalescontract',
            name='purpose',
            field=models.CharField(choices=[('BS', 'Before subject'), ('AS', 'After subject'), ('BT', 'Before total'), ('AT', 'After total'), ('BW', 'Before wishes'), ('AW', 'After wishes'), ('C1', 'Custom 1'), ('C2', 'Custom 2'), ('C3', 'Custom 3'), ('C4', 'Custom 4')], max_length=2, verbose_name='Purpose'),
        ),
    ]
