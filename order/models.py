import uuid
from django.db import models

from client.models import Haridor
from product.models import Maxsulot


class Buyurtma(models.Model):
    TOLOV_TURLARI = (
        ('naqd', 'Naqd'),
        ('karta', 'Karta'),
        ('click', 'Click / Payme'),
    )

    STATUSLAR = (
        ('yangi', 'Yangi'),
        ('tasdiqlangan', 'Tasdiqlangan'),
        ('yetkazilgan', 'Yetkazilgan'),
    )

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client = models.ForeignKey(Haridor, on_delete=models.CASCADE, related_name='buyurtmalar')
    maxsulot_033 = models.PositiveIntegerField(default=0)  # 0.33L soni
    maxsulot_05 = models.PositiveIntegerField(default=0)   # 0.5L soni
    maxsulot_1 = models.PositiveIntegerField(default=0)    # 1L soni

    tolov_turi = models.CharField(max_length=20, choices=TOLOV_TURLARI)
    izoh = models.TextField(blank=True, null=True)
    shartnoma_qabul_qilindi = models.BooleanField(default=False)
    umumiy_summa = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUSLAR, default='yangi')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Buyurtma {self.uid} - {self.client.ism}"

    def save(self, *args, **kwargs):
        # Mahsulot narxlarini bazadan olamiz
        narx_033 = Maxsulot.objects.filter(hajmi='0.33 L').first()
        narx_05 = Maxsulot.objects.filter(hajmi='0.5 L').first()
        narx_1 = Maxsulot.objects.filter(hajmi='1 L').first()

        self.umumiy_summa = (
            (self.maxsulot_033 * (narx_033.narxi if narx_033 else 0)) +
            (self.maxsulot_05 * (narx_05.narxi if narx_05 else 0)) +
            (self.maxsulot_1 * (narx_1.narxi if narx_1 else 0))
        )
        super().save(*args, **kwargs)

