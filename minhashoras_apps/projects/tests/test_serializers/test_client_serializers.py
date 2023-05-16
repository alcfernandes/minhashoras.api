import pytest

from ...serializers import ClientSerializer


@pytest.mark.django_db
def test_client_serializer(client):

    # Serializa o objeto client
    serializer = ClientSerializer(client)

    # Verifica se os dados serializados correspondem ao objeto original
    assert serializer.data['id'] == client.id
    assert serializer.data['account'] == client.account.uuid
    assert serializer.data['name'] == client.name
    assert serializer.data['email'] == client.email
    assert serializer.data['notes'] == client.notes
