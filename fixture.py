from django.core.management import call_command
from django.db import (transaction, connections, DEFAULT_DB_ALIAS)
from core.models import AmbrUser;

class Fixture(object):
    __name__ = "Fixture"

    def __init__(self, *args):
        self.decorator_args= args

    def __call__(self, f):

        def wrapped_f(*args):
            self.load_fixture(*self.decorator_args)
            print "Decorator arguments:", self.decorator_args
            f(*args)
            print "After f(*args)"
        return wrapped_f


    def load_fixture(self, *fixtures):
        databases = [DEFAULT_DB_ALIAS]
        for db in databases:
            call_command('loaddata', *fixtures,
                **{
                    'verbosity': 0,
                    'commit': True,
                    'database': db
                })
