'''make pylint happy'''

import sys
sys.path.append('./lib')
from pyskel import *

class TestPySkel:
    '''make pylint happy'''
    def __init__(self):
        self.data = []
        self.testing = None

    def setup(self):
        '''make pylint happy'''
        self.testing = True

    def test_foo_is_blacklisted(self):
        '''make pylint happy'''
        ps = PySkel()
        # Invoke with `-s` to see printing:
        # `pipenv run pytest -s`
        print("from test")
        assert ps.foo_is_blacklisted() == 'bar'

    def teardown(self):
        '''make pylint happy'''
        self.testing = False
