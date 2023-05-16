from pytest_factoryboy import LazyFixture, register

from .accounts.fixture_factories import AccountFactory, UserFactory
from .projects.fixture_factories import ClientFactory

# Account factories
register(AccountFactory)
register(AccountFactory, 'other_account')

# User factories
register(UserFactory)
register(
    UserFactory, 'user_other_account', account=LazyFixture('other_account')
)

# Client factories
register(ClientFactory)
register(
    ClientFactory, 'client_other_account', account=LazyFixture('other_account')
)
