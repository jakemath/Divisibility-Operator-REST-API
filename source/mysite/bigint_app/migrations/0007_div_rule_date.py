# Generated by Django 2.2.3 on 2019-08-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigint_app', '0006_div_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='div_rule',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
