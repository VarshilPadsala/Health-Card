# Generated by Django 3.2.16 on 2022-12-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health_App', '0002_doctor_medical_store_patient_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='Medication',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
