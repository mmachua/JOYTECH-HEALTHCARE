# Generated by Django 3.2 on 2023-01-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20221026_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]