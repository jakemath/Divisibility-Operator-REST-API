# Generated by Django 2.2.3 on 2019-07-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigint_app', '0005_delete_div_rule'),
    ]

    operations = [
        migrations.CreateModel(
            name='div_rule',
            fields=[
                ('divisor', models.TextField(primary_key=True, serialize=False)),
                ('divisor_size', models.BigIntegerField()),
                ('rule', models.TextField()),
                ('rule_size', models.BigIntegerField()),
                ('negative_rule', models.BooleanField()),
            ],
        ),
    ]
