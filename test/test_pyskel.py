import sys
sys.path.append('./lib')
from pyskel import *

class TestPySkel:
    def setUp(self):
        self.testing = True

    def test_foo_is_blacklisted(self):
        ps = PySkel()
        # Invoke with `-s` to see printing:
        # `pipenv run pytest -s`
        print("from test")
        assert ps.foo_is_blacklisted() == 'bar'

    def tearDown(self):
        self.testing = False