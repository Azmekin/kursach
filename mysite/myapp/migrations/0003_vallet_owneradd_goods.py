# Generated by Django 4.2 on 2023-05-08 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_alter_chawo_quest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web', models.TextField(max_length=100)),
                ('money', models.IntegerField(default=0)),
                ('vallet_number', models.TextField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=5)),
                ('img_res', models.TextField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=51)),
                ('cost', models.IntegerField(default=0)),
                ('image', models.TextField(max_length=100)),
                ('sold_type', models.BooleanField(default=False)),
                ('IS_3D', models.BooleanField(default=False)),
                ('IS_2D', models.BooleanField(default=False)),
                ('IS_AUDIO', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
