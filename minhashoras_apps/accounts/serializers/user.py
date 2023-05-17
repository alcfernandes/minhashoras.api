from rest_framework import serializers

from ..models import User


class UserRestrictUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
        ]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'is_active',
            'created_at',
            'updated_at',
            'archived_at',
            'uuid',
        ]
        read_only_fields = (
            'id',
            'is_active',
            'created_at',
            'updated_at',
            'archived_at',
            'uuid',
            'email',
        )
