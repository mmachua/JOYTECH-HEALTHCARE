# Generated by Django 3.2 on 2023-04-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inpatient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='ward',
            field=models.CharField(choices=[('FEMALE_MEDICAL_WARD', 'FEMALE MEDICAL WARD'), ('MALE_MEDICAL_WARD', 'MALE MEDICAL WARD'), ('SURGICAL_WARD', 'SURGICAL WARD'), ('MALE_SURGICAL_WARD', 'MALE SURGICAL WARD'), ('FEMALE_SURGICAL_WARD', 'FEMALE SURGICAL WARD'), ('MARTERNITY_WARD', 'MARTERNITY WARD'), ('FEMALE_MEDICAL_WARD', 'FEMALE MEDICAL WARD'), ('PAEDIATRICS', 'PAEDIATRICS')], max_length=30),
        ),
    ]