import unittest
from codigo import spelling

class TestT9Spelling(unittest.TestCase):

    def test_a_deve_retornar_2(self):
        self.assertEqual('2', spelling('a'))

    def test_b_deve_retornar_22(self):
        self.assertEqual('22', spelling('b'))

    def test_c_deve_retornar_222(self):
        self.assertEqual('222', spelling('c'))

    def test_ac_deve_retornar_2_222(self):
        self.assertEqual('2 222', spelling('ac'))

    def test_bca_deve_retornar_22_222_2(self):
        self.assertEqual('22 222 2', spelling('bca'))

    def test_hi_deve_retornar_44_444(self):
        self.assertEqual('44 444', spelling('hi'))

    def test_yes_deve_retornar_999_33_7777(self):
        self.assertEqual('999337777', spelling('yes'))

    def test_hello_world_deve_retornar_4433555_555666096667775553(self):
        self.assertEqual('4433555 555666096667775553', spelling('hello world'))

unittest.main()
