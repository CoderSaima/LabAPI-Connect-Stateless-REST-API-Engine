from rest_framework import serializers
from .models import labapi_model, asset_record_model
from django.contrib.auth.hashers import make_password

class SecAuthSerializer(serializers.ModelSerializer):
    """
    The Core Translation Engine for labAPI_app.
    Maps relational database fields directly to JSON structures.
    """
    class Meta:
        model = labapi_model
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True} # Keeps password hash completely hidden on reads
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class assset_record_serializer(serializers.ModelSerializer):
    class Meta:
        model = asset_record_model
        fields = ['id', 'title', 'description', 'category', 'created_at']