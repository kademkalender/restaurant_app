# Generated by Django 5.1 on 2024-08-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=100)),
                ('res_category', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('publish_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
