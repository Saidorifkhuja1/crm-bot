import uuid

from django.db import models

from user.models import PHONE_REGEX


class Haridor(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    ism_familiya = models.CharField(max_length=255)
    tugilgan_sana = models.DateField()
    dokon_nomi = models.CharField(max_length=255)
    firma_nomi = models.CharField(max_length=255)
    guvoxnoma_rasmi = models.ImageField(upload_to='certificates/')
    dokon_rasmi = models.ImageField(upload_to='shop_photos/')
    telefon_raqami = models.CharField(validators=[PHONE_REGEX], max_length=21,default="+998931112233")
    maxsus_soz = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism_familiya

