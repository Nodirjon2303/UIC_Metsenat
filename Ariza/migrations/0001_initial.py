# Generated by Django 4.0.5 on 2022-06-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ariza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('yuridik', 'Yuridik shaxs'), ('jismoniy', 'Jismoniy shaxs')], max_length=255)),
                ('fish', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=25)),
                ('amount', models.BigIntegerField()),
                ('tashkilot', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('yangi', 'Yangi ariza tashlandi'), ('moderatsiya', 'Moderatsya jarayonida'), ('tasdiqlangan', 'Tasdiqlangan'), ('cancel', 'Bekor qilingan')], default='yangi', max_length=125, null=True)),
            ],
        ),
    ]
