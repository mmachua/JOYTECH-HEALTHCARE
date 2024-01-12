# Generated by Django 3.2 on 2022-10-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20220723_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('id_number', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patientid', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='patientidupload',
            name='idno',
            field=models.IntegerField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='patientidupload',
            name='patientid',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]