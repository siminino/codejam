import unittest
from alienlang import alien_trans

class TestAlienLanguage(unittest.TestCase):

    def test_1_palavra_a_deve_retornar_1(self):
        self.assertEqual('Case #1: 1', alien_trans(1,1,1,'a','a'))

    def test_code_jam_2(self):
        self.assertEqual('Case #1: 2\nCase #2: 1\nCase #3: 3\nCase #4: 0', alien_trans(3,5,4,'abc\nbca\ndac\ndbc\ncba','(ab)(bc)(ca)\nabc\n(abc)(abc)(abc)\n(zyx)bc'))

unittest.main()
