import pytest
from rest_framework.test import APIClient

from ...models import User

API_USERS_ME_URL = '/api/users/me/'
API_USERS_URL = '/api/users/'


@pytest.mark.django_db
def test_it_should_be_possible_to_retrieve_my_user(user, user_other_account):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get(API_USERS_ME_URL)
    assert response.status_code == 200
    assert response.data['id'] == user.id

    # Ensure there are multiple users
    assert User.objects.count() == 2


@pytest.mark.django_db
def test_it_should_be_possible_to_update_my_user_data(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    update_user_data = {
        'name': 'Name Updated',
    }
    response = api_client.patch(API_USERS_ME_URL, data=update_user_data)
    assert response.status_code == 200
    assert response.data['name'] == update_user_data['name']


@pytest.mark.django_db
def test_it_should_not_be_possible_to_create_a_user(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    new_user_data = {
        'name': 'New User',
        'email': 'teste@teste.com',
    }
    response = api_client.post(API_USERS_URL, data=new_user_data)
    assert response.status_code == 404


@pytest.mark.django_db
def test_it_should_not_be_possible_to_update_a_user_by_its_id(
    user,
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    update_user_data = {
        'name': 'Name Updated',
    }
    response = api_client.patch(
        f'{API_USERS_URL}/{user.id}', data=update_user_data
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_it_should_not_be_possible_to_delete_a_user_by_its_id(
    user,
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.delete(f'{API_USERS_URL}/{user.id}')
    assert response.status_code == 404


@pytest.mark.django_db
def test_it_should_not_be_possible_to_retrieve_a_user_by_its_id(
    user,
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get(f'{API_USERS_URL}/{user.id}')
    assert response.status_code == 404


@pytest.mark.django_db
def test_it_should_not_be_possible_to_list_users(
    user,
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get(API_USERS_URL)
    assert response.status_code == 404
