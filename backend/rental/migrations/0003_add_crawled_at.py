# Generated by Django 2.0.7 on 2018-07-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_add_author_hash'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='house',
            name='house_updated_f87264_idx',
        ),
        migrations.AddField(
            model_name='house',
            name='crawled_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='housets',
            name='crawled_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddIndex(
            model_name='housets',
            index=models.Index(fields=['vendor', 'vendor_house_id', 'updated'], name='house_ts_vendor__68cad2_idx'),
        ),
        migrations.AddIndex(
            model_name='house',
            index=models.Index(fields=['crawled_at'], name='house_crawled_7633f7_idx'),
        ),
    ]