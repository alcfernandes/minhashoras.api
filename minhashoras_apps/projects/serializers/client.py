from rest_framework import serializers

from ..models import Client


class ClientSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'account', 'name', 'email', 'notes']


class ClientListSerializer(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        fields = ['id', 'account', 'name', 'email']


class ClientCreateUpdateSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('account',)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('account', None)
        client = Client.objects.create(account=user.account, **validated_data)
        return client
