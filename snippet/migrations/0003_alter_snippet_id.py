# Generated by Django 4.0.6 on 2022-07-07 09:43

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_alter_snippet_id_alter_snippet_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234', length=5, max_length=40, prefix='', primary_key=True, serialize=False),
        ),
    ]
