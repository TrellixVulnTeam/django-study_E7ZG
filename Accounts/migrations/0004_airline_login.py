# Generated by Django 2.2.4 on 2019-09-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20190908_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('password', models.IntegerField(max_length=200)),
            ],
        ),
    ]
