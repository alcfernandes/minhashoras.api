from pytest_factoryboy import register

from .accounts.fixture_factories import AccountFactory, UserFactory

register(AccountFactory)
register(UserFactory)
