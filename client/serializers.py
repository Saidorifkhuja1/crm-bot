from rest_framework import serializers
from .models import Haridor

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haridor
        fields = '__all__'
        read_only_fields = ['uid', 'created_at']
