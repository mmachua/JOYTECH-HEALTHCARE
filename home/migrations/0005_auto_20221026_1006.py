# Generated by Django 3.2 on 2022-10-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220420_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='patient_category',
            field=models.CharField(blank=True, choices=[('InPatient', 'InPatient'), ('OutPatient', 'OutPatient'), ('Maternity', 'Maternity'), ('Special_Clinic', 'Special_Clinic')], max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='patient_category',
            field=models.CharField(blank=True, choices=[('InPatient', 'InPatient'), ('OutPatient', 'OutPatient'), ('Maternity', 'Maternity'), ('Special_Clinic', 'Special_Clinic')], max_length=500),
        ),
    ]