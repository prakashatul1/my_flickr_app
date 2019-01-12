# Generated by Django 2.1.5 on 2019-01-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0002_auto_20190112_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickrgroup',
            name='name',
        ),
        migrations.AddField(
            model_name='flickrgroup',
            name='group_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flickrgroup',
            name='nsid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nsid',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
