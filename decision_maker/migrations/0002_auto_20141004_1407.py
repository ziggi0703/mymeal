# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decision_maker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='link_to_menu',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
