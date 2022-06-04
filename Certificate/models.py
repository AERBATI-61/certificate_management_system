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

# qr
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Barcode
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



class Product(models.Model):
    name = models.CharField(max_length=200)
    country_id = models.CharField(max_length=1, null=True)
    manufacturer_id = models.CharField(max_length=6,null=True)
    number_id = models.CharField(max_length=5, null=True)
    barcode = models.ImageField(upload_to='barcode/', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)






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
    org_name                = models.ManyToManyField('Organization')
    activity_name           = models.CharField(max_length=64, null=False, blank=False)
    activity_image          = models.ImageField(upload_to='activity', blank=True, null=True)
    active                  = models.BooleanField()
    address                 = models.TextField()
    description             = models.TextField()
    starttime               = models.DateTimeField(auto_now_add=False)
    endtime                 = models.DateTimeField(auto_now_add=False)
    slug                    = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.activity_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.activity_name)
        super().save(*args, **kwargs)

    @property
    def Is_Past(self):
        today = date.today()
        if self.starttime.date() < today:
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
    host_name = models.ManyToManyField('Host', )
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.cer_name) + " ( " + str(self.participant_name) + " )"

    class Meta:
        ordering = ["cer_name"]


class ContactUs(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    surname = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    activity = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email


class SendEmail(models.Model):
    fullname = models.CharField(max_length=64, null=True, blank=True)
    subject = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname + ' ' + self.subject





class Host(models.Model):
    host_name = models.CharField(max_length=64, null=False, blank=False)
    surname = models.CharField(max_length=64, null=False, blank=False)
    activity_name = models.ManyToManyField('Activity',)
    position = models.CharField(max_length=64, blank=True, null=True)
    host_image = models.ImageField(upload_to='host', blank=True, null=True)

    def __str__(self):
        return self.host_name



'''
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
'''




class Website(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)




class GoogleForm(models.Model):
    activity_name = models.CharField(max_length=132, blank=True, null=True)
    our_forms = models.ImageField(upload_to='google_forms', blank=True, verbose_name="Google Form")

    def __str__(self):
        return str(self.activity_name)