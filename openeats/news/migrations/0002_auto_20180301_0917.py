# Generated by Django 2.0.2 on 2018-03-01 08:17

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='frontpage',
            field=models.BooleanField(default=False, help_text='determines if the story appears on the front page', verbose_name='frontpage'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/news/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug'),
        ),
    ]