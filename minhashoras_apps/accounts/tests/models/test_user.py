import pytest
import uuid
from django.core.exceptions import ValidationError
from minhashoras_apps.accounts.models import User


@pytest.mark.django_db
def test_user_creation():
    # Create a new User instance
    user = User(email="test_user@example.com", name="Test User", is_staff=True)
    user.set_password("testpassword")
    user.save()

    # Retrieve the user from the database
    retrieved_user = User.objects.get(email="test_user@example.com")

    # Check if the retrieved user's attributes match the original user's attributes
    assert retrieved_user.email == "test_user@example.com"
    assert retrieved_user.name == "Test User"
    assert retrieved_user.is_active is True
    assert retrieved_user.is_staff is True
    assert isinstance(retrieved_user.uuid, uuid.UUID)


@pytest.mark.django_db
def test_email_validation():
    # Create a new User instance with an invalid email address
    user = User(email="invalid_email", name="Invalid Email User")
    user.set_password("testpassword")

    # Check if saving the user with an invalid email raises a ValidationError
    with pytest.raises(ValidationError):
        user.full_clean()


@pytest.mark.django_db
def test_required_fields():
    # Check if the required fields are correct
    assert User.REQUIRED_FIELDS == ['name']
    assert User.USERNAME_FIELD == 'email'
