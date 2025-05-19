import uuid

from django.db import models

class Maxsulot(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    hajmi = models.CharField(max_length=500)
    narxi = models.IntegerField()

    def __str__(self):
        return self.hajmi

