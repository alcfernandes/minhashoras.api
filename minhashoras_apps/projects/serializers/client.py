from rest_framework import serializers

from ..models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'is_active', 'uuid']
        read_only_fields = ('id', 'is_active', 'uuid')


class ClientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'email',
            'notes',
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
        )


class ClientCreateUpdateSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = (
            'id',
            'is_active',
            'created_at',
            'updated_at',
            'archived_at',
            'uuid',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('account', None)
        client = Client.objects.create(account=user.account, **validated_data)
        return client
