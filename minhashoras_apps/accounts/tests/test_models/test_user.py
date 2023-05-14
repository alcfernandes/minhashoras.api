import uuid

import pytest

from minhashoras_apps.accounts.models import Account, User


@pytest.mark.django_db
def test_it_should_be_possible_to_create_a_user():
    user = User.objects.create_user(
        email='test_user@example.com',
        password='testpassword',
        name='Test User',
        is_staff=True,
    )

    retrieved_user = User.by_id(user.id)
    assert retrieved_user.email == 'test_user@example.com'
    assert retrieved_user.name == 'Test User'
    assert retrieved_user.is_active is True
    assert retrieved_user.is_staff is True
    assert isinstance(retrieved_user.uuid, uuid.UUID)


@pytest.mark.django_db
def test_it_should_not_be_possible_to_create_a_user_with_an_invalid_email():
    with pytest.raises(ValueError):
        User.objects.create_user(
            email='invalid_email',
            password='testpassword',
            name='Invalid Email User',
            is_staff=True,
        )


@pytest.mark.django_db
def test_it_should_be_possible_to_create_a_user_with_an_account_as_its_owner(
    account,
):
    user = User.objects.create_user(
        email='test_user@example.com',
        password='testpassword',
        name='Test User',
        account=account,
        is_owner=True,
    )

    retrieved_user = User.objects.get(email='test_user@example.com')
    assert retrieved_user.account == account

    retrieved_account = Account.by_id(account.id)
    assert retrieved_account.owner == user
