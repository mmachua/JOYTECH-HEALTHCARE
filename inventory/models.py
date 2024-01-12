from django.db import models
import datetime
# Create your models here.
from django.db import models

class Equipment(models.Model):
    DEPARTMENT_CHOICES = (
        ('RAD', 'Radiology'),
        ('CARD', 'Cardiology'),
        ('SURG', 'Surgery'),
        ('LAB', 'Laboratory'),
        ('RECORDS', 'Records'),
        ('CLINICAL', 'Clinical'),
        ('DT', 'Dental'),
        ('OPT', 'Optical'),
        ('ADMIN', 'Administration'),
        ('THEATRE', 'Theatre'),
        ('SPCLINIC', 'Special-Clinic'),
        ('NURSE', 'Nursing'),
        ('TRIAGE', 'TRIAGE'),
        ('MCH', 'MCH'),
        ('FILING', 'Filing'),
        ('ADMINOFFICE', 'Admin office'),
        ('PHARM', 'Pharmacy'),
        ('GT', 'Geriatrics'),
        ('REHAB', 'Rehab'),
        ('ACC', 'Accounts'),
        ('DIR', 'Director Office'),
        ('KITCHEN', 'Kitchen'),
        ('RECEPTION', 'Reception'),
        # Add more department choices as needed
    )

    STATE_CHOICES = (
        ('Operational', 'Operational'),
        ('Maintenance', 'Maintenance'),
        ('Replacement', 'Replacement'),
        ('Other', 'Other'),
    )

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    in_charge = models.CharField(max_length=100)
    unique_identifier = models.CharField(max_length=20, unique=True)
    date_registered = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        if not self.unique_identifier:
            # Generate unique identifier based on department and a sequential number
            equipment_count = Equipment.objects.filter(department=self.department).count() + 1
            self.unique_identifier = f'{self.department}-{equipment_count:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
