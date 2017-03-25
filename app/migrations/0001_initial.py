# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('ccx', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['ccx'],
            },
        ),
    ]
