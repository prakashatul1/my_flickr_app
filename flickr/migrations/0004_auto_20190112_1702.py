# Generated by Django 2.1.5 on 2019-01-12 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0003_auto_20190112_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickrgroup',
            name='id',
        ),
        migrations.AlterField(
            model_name='flickrgroup',
            name='nsid',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]