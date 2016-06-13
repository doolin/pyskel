#!/usr/bin/env python

import unittest
import sys
sys.path.append('../lib')
from pyskel import *

class TestPySkel(unittest.TestCase):

    def setUp(self):
        # dummy
        self.testing = True

    def test_foo_is_blacklisted(self):
        ps = PySkel()
        assert ps.foo_is_blacklisted() == 'bar'

    def tearDown(self):
        # dummy
        self.testing = False

if __name__ == '__main__':
    unittest.main()
