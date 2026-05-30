from .models import Bulletins
from rest_framework import serializers

class BulletinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletins
        fields = '__all__'