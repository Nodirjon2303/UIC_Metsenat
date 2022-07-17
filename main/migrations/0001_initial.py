# Generated by Django 4.0.5 on 2022-07-17 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ariza', '0002_ariza_paymenttype_alter_ariza_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=25)),
                ('t_turi', models.CharField(choices=[('bakalavr', 'Bakalavr daraja'), ('magistr', 'Magistratura tlabasi')], max_length=25)),
                ('kontrakt', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('otm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.university')),
            ],
        ),
        migrations.CreateModel(
            name='Homiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('homiy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ariza.ariza')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
