# Generated by Django 2.2.7 on 2019-11-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecordLog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='log_id',
            field=models.TextField(default='0YX4fM54H6VRAQNdpuDixEzRSPIlHqLj', max_length=32),
        ),
    ]