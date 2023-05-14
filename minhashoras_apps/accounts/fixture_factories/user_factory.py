import factory
from factory.django import DjangoModelFactory

from ..models import User
from .account_factory import AccountFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    name = factory.Faker('name')
    account = factory.SubFactory(AccountFactory)
    is_owner = factory.Faker('pybool')
