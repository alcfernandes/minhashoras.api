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
    quick_info = factory.Faker('text')
    notes = factory.Faker('text')
