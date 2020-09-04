from rest_framework import serializers
from pruebaPrimos.models import Primos
import pruebaPrimos.views

class PrimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primos
        fields = ['numero', 'numeros_primos']

    def create(self, validated_data):
        return Primos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('numero', instance.name)
        instance.name = validated_data.get('numeros_primos', instance.numeros_primos)
        instance.save()
        return instance
