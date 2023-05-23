import pytest

from ...serializers import ClientListSerializer, ClientRetrieveSerializer


@pytest.mark.django_db
def test_it_should_be_possible_to_use_client_list_serializer(client):
    # Serializa o objeto client
    serializer = ClientListSerializer(client)

    # Verifica se os campos retornados são os esperados
    expected_fields = {
        'id',
        'name',
        'email',
        'quick_info',
        'is_active',
        'uuid',
    }
    data = serializer.data
    assert set(data.keys()) == expected_fields


@pytest.mark.django_db
def test_it_should_be_possible_to_use_client_retrieve_serializer(client):
    # Serializa o objeto client
    serializer = ClientRetrieveSerializer(client)

    # Verifica se os campos retornados são os esperados
    expected_fields = {
        'id',
        'name',
        'email',
        'quick_info',
        'notes',
        'is_active',
        'created_at',
        'updated_at',
        'archived_at',
        'uuid',
    }
    data = serializer.data
    assert set(data.keys()) == expected_fields
