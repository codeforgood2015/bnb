# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteers', '0025_auto_20150125_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voucher',
            name='generateDate',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
