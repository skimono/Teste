# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRCA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipo_curso',
            field=models.CharField(max_length=12, default=1),
            preserve_default=False,
        ),
    ]
