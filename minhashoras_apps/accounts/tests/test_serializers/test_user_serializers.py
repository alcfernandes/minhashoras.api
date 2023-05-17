import pytest

from ...serializers import UserRestrictUpdateSerializer, UserRetrieveSerializer


@pytest.mark.django_db
def test_it_should_be_possible_to_use_user_restrict_update_serializer(user):
    serializer = UserRestrictUpdateSerializer(user)

    expected_fields = {'name'}
    data = serializer.data
    assert set(data.keys()) == expected_fields


@pytest.mark.django_db
def test_it_should_be_possible_to_use_user_retrieve_serializer(user):
    serializer = UserRetrieveSerializer(user)

    expected_fields = {
        'id',
        'email',
        'name',
        'is_active',
        'created_at',
        'updated_at',
        'archived_at',
        'uuid',
    }
    data = serializer.data
    assert set(data.keys()) == expected_fields
