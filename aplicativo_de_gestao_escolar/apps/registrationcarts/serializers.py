from .models import RegistrationCart
from rest_framework import serializers

class RegistrationCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCart
        fields = '__all__'