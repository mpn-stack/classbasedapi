# Generated by Django 3.2.23 on 2024-02-15 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.IntegerField(default=1)),
                ('expire_data', models.DateTimeField()),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
