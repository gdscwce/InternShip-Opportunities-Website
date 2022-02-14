from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import InternShip


class InternShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternShip
        fields = ["id", "name", "image", "paid",
                  "stipend", "duration", "role", "date"]
    # name = serializers.CharField(max_length=100)
    # image = serializers.CharField(max_length=100)
    # paid = serializers.BooleanField(default=True)
    # stipend = serializers.CharField(max_length=50)
    # duration = serializers.CharField(max_length=50)
    # role = serializers.CharField(max_length=50)
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return InternShip.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.paid = validated_data.get("paid", instance.paid)
    #     instance.stipend = validated_data.get("stipend", instance.stipend)
    #     instance.duration = validated_data.get("duration", instance.duration)
    #     instance.role = validated_data.get("role", instance.role)
    #     instance.date = validated_data.get("date", instance.date)
    #     instance.save()
    #     return instance
