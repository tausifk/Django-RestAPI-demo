# Generated by Django 2.0.6 on 2018-09-27 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kra_points', models.IntegerField()),
                ('promotion', models.BooleanField()),
                ('increment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]