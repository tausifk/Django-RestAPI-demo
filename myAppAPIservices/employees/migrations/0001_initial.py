# Generated by Django 2.0.6 on 2018-09-28 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('contact_preference', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('department', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('photo_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceAppraisel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kra_rating', models.IntegerField()),
                ('promotion', models.BooleanField()),
                ('percentage_increment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('performance_year', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
    ]