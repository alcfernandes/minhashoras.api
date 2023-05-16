import pytest
from rest_framework.test import APIClient

from ...models import Client

API_CLIENTS_URL = '/api/clients/'


@pytest.mark.django_db
def test_it_should_be_possible_to_list_clients_of_the_users_account(
    user, client, client_other_account
):

    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get(API_CLIENTS_URL)

    # Check if the response includes only the client of the user's account
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == client.id

    # Check if database really has more than one client
    assert Client.objects.count() == 2  # sanity check


@pytest.mark.django_db
def test_it_should_be_possible_to_retrieve_a_client_of_the_users_account(
    user, client, client_other_account
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.get(f'{API_CLIENTS_URL}{client.id}/')
    assert response.status_code == 200
    assert response.data['id'] == client.id


@pytest.mark.django_db
def test_it_should_be_possible_to_create_a_client_on_user_account(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    new_client_data = {
        'name': 'New Client',
        'email': 'new_client@test.com',
        'notes': 'Some notes about the new client',
    }
    response = api_client.post(API_CLIENTS_URL, data=new_client_data)
    assert response.status_code == 201
    assert response.data['account'] == user.account.uuid
    assert response.data['email'] == new_client_data['email']


@pytest.mark.django_db
def test_it_should_be_possible_to_update_a_client_on_user_account(
    user, client
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    updated_client_data = {
        'name': 'Updated Client',
    }
    response = api_client.patch(
        f'{API_CLIENTS_URL}{client.id}/', data=updated_client_data
    )
    assert response.status_code == 200
    assert response.data['name'] == updated_client_data['name']


@pytest.mark.django_db
def test_it_should_not_be_possible_to_update_a_client_of_another_account(
    user, client, client_other_account
):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    updated_client_data = {
        'name': 'Updated Client',
    }
    response = api_client.patch(
        f'{API_CLIENTS_URL}{client_other_account.id}/',
        data=updated_client_data,
    )
    assert response.status_code == 404
    assert (
        Client.objects.get(id=client_other_account.id).name != 'Updated Client'
    )


@pytest.mark.django_db
def test_it_should_be_possible_to_archive_a_client(user, client):
    api_client = APIClient()
    api_client.force_authenticate(user=user)

    response = api_client.delete(f'{API_CLIENTS_URL}{client.id}/')
    assert response.status_code == 204
    assert Client.objects.get(id=client.id).is_active is False
