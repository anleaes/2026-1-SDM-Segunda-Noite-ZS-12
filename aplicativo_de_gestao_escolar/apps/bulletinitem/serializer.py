from .models import Bulletinitem
from rest_framework import serializers

class BulletinitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletinitem
        fields = '__all__'
        