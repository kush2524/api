# Generated by Django 4.0.1 on 2024-06-07 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_spamnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('spam', models.IntegerField(default=0)),
                ('names', models.ManyToManyField(related_name='global_dataset_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]