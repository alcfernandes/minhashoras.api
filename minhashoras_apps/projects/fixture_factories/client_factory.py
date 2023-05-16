import factory
from factory.django import DjangoModelFactory

from minhashoras_apps.accounts.fixture_factories import AccountFactory

from ..models import Client


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    account = factory.SubFactory(AccountFactory)
    name = factory.Faker('name')
    email = factory.Faker('email')
    notes = factory.Faker('text')
