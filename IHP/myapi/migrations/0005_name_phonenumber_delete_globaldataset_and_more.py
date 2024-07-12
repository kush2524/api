# Generated by Django 4.0.1 on 2024-06-07 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_globaldataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='GlobalDataset',
        ),
        migrations.AddField(
            model_name='name',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.phonenumber'),
        ),
        migrations.AddField(
            model_name='name',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]