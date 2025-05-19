# serializers.py

from rest_framework import serializers
from .models import Maxsulot

class MaxsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = '__all__'
