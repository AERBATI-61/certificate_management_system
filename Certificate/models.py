from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import timedelta

from django import forms
from django.utils.text import slugify
from datetime import *

from django.views.decorators.cache import never_cache

stack_name = []

level_of_education = (
    ('lisans', 'lisans'),
    ('yükseklisans', 'yükseklisans'),
    ('doktora', 'doktora'),
    ('mezun', 'mezun')
)

type_of_certificate = (
    ("Certificate of Participation ", "Certificate of Participation"),
    ("Certificate of Achievement", "Certificate of Achievement"),
    ("Aword Certificate", "Aword Certificate")
)


class Activity(models.Model):
    org_name = models.ManyToManyField('Organization')
    activity_name = models.CharField(max_length=64, null=False, blank=False)
    activity_image = models.ImageField(upload_to='activity', blank=True, null=True)
    active = models.BooleanField()
    address = models.TextField()
    description = models.TextField()
    starttime = models.DateTimeField(auto_now_add=False)
    endtime = models.DateTimeField(auto_now_add=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.activity_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.activity_name)
        super().save(*args, **kwargs)

    @property
    def Is_Past(self):
        today = date.today()
        if self.starttime.date() < today and self.endtime.time() < datetime.now().time():
            thing = "Past"
        else:
            thing = "Future"
        return thing

    class Meta:
        ordering = ["-starttime"]



class Participant(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    surname = models.CharField(max_length=64, null=False, blank=False)
    activity_name = models.ManyToManyField('Activity', )
    university = models.CharField(max_length=64, null=False, blank=False)
    department = models.CharField(max_length=64, null=False, blank=False)
    edu_deg = models.CharField(max_length=64, blank=False, null=False, choices=level_of_education)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.name


class Organization(models.Model):
    org_name = models.CharField(max_length=64, null=False, blank=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    authorized = models.CharField(max_length=64, null=False, blank=False)
    org_image = models.ImageField(upload_to='organization', blank=True, null=True)
    address = models.TextField()
    org_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.org_name) + " ( " + str(self.authorized) + " )"





class Certificate(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, ('Inactive')),
        (ACTIVE, ('Active')),
    )

    cer_code = models.AutoField(primary_key=True, verbose_name="certificate ID")
    cer_name = models.CharField(max_length=64, null=False, blank=False)
    cer_deg = models.CharField(max_length=64, blank=False, null=False, choices=type_of_certificate)
    active = models.IntegerField(default=0, blank=True, null=True, choices=STATUS)
    cer_description = models.TextField()
    organisation_name = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False, blank=False)
    participant_name = models.ForeignKey(Participant, on_delete=models.CASCADE, null=False, blank=False)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.cer_name) + " ( " + str(self.participant_name) + " )"

    class Meta:
        ordering = ["cer_name"]


class ContactUs(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    surname = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    host_name = models.CharField(max_length=64, null=False, blank=False)
    surname = models.CharField(max_length=64, null=False, blank=False)
    activity_name = models.ManyToManyField('Activity',)
    position = models.CharField(max_length=64, blank=True, null=True)
    host_image = models.ImageField(upload_to='host', blank=True, null=True)

    def __str__(self):
        return self.host_name
