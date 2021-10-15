from rest_framework import serializers
from .models import PatientModel


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = ('id', 'name', 'pesel', 'gender', 'age')