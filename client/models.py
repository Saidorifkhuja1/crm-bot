import uuid

from django.db import models

from user.models import PHONE_REGEX


class Client(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    shop_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates/')
    shop_photo = models.ImageField(upload_to='shop_photos/')
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=21,default="+998931112233")
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

