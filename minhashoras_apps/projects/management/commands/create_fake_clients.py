import logging

from django.core.management.base import BaseCommand

from minhashoras_apps.accounts.models import Account

from ...fixture_factories import ClientFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Creates fake data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--account_id',
            type=int,
            help='The ID of the account to use for the clients',
            default=None,
        )
        parser.add_argument(
            '--quantity',
            type=int,
            help='The number of clients to create',
            default=100,
        )

    def handle(self, *args, **kwargs):
        account_id = kwargs['account_id']
        quantity = kwargs['quantity']
        account = None

        if account_id is not None:
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(
                        f'Account with ID {account_id} does not exist'
                    )
                )
                logger.error(f'Account with ID {account_id} does not exist')
                return

        for i in range(quantity):
            ClientFactory(account=account)
            logger.info(f'Created client {i + 1} of {quantity}')
