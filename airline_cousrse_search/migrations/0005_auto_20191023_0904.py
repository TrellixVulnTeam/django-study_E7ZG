# Generated by Django 2.2.1 on 2019-10-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_cousrse_search', '0004_cargoall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargoall',
            name='cargo_flight_section',
            field=models.CharField(choices=[('김포(GMP) - 제주(CJU)', '김포(GMP) - 제주(CJU)'), ('김포(GMP) - 부산(PUS)', '김포(GMP) - 부산(PUS)'), ('부산(PUS) - 제주(CJU)', '부산(PUS) - 제주(CJU)'), ('부산(PUS) - 김포(GMP)', '부산(PUS) - 김포(GMP)'), ('제주(CJU) - 김포(GMP)', '제주(CJU) - 김포(GMP)'), ('제주(CJU) - 부산(PUS)', '제주(CJU) - 부산(PUS)')], max_length=300),
        ),
    ]
