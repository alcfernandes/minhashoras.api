import factory
from factory.django import DjangoModelFactory

from ..models import Account


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Faker('name')
