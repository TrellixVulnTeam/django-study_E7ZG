# Generated by Django 2.2.4 on 2019-09-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_consent', models.CharField(max_length=200)),
                ('membership_terms', models.TextField(max_length=10000)),
                ('check_01', models.CharField(max_length=200)),
                ('privacy', models.TextField(max_length=10000)),
                ('check_02', models.CharField(max_length=200)),
                ('overseas_transfer', models.TextField(max_length=10000)),
                ('check_03', models.CharField(max_length=200)),
                ('three_party', models.TextField(max_length=20000)),
                ('check_04', models.CharField(max_length=200)),
                ('marketing', models.TextField(max_length=10000)),
                ('check_05', models.CharField(max_length=200)),
            ],
        ),
    ]
