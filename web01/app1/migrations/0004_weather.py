# Generated by Django 4.1.1 on 2022-09-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Temp(C)')),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
