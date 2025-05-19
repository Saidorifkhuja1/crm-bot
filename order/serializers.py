from rest_framework import serializers
from .models import Buyurtma

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'
        read_only_fields = ['uid', 'created_at', 'umumiy_summa']
