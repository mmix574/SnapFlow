from django.core.management.base import BaseCommand,CommandError



from credit.models import CreditExchangeCode
import random

def get_randem_code():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(32):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):

        for _ in range(1,50000):
            c = CreditExchangeCode()
            c.code = get_randem_code()
            c.point = 500
            c.save()
            print(c)
        pass

