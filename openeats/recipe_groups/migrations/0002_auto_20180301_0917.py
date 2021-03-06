# Generated by Django 2.0.2 on 2018-03-01 08:17

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug'),
        ),
    ]
