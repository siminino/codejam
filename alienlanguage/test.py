import unittest
from alienlang import alien_trans, list_letter

class TestAlienLanguage(unittest.TestCase):

    def test_1_palavra_a_deve_retornar_1(self):
        self.assertEqual('Case #1: 1', alien_trans(1,1,1,'a','a'))

    def test_code_jam_2(self):
        self.assertEqual('Case #1: 2\nCase #2: 1\nCase #3: 3\nCase #4: 0', alien_trans(3,5,4,'abc\nbca\ndac\ndbc\ncba','(ab)(bc)(ca)\nabc\n(abc)(abc)(abc)\n(zyx)bc'))

    def test_code_jam_3(self):
        self.assertEqual('Case #1: 1\nCase #2: 2\nCase #3: 0', alien_trans(3,4,3,'abc\nbca\ndac\ndbc\ncba','(ab)(ca)(abcd)\n(cd)b(ac)\nc(acd)(ac)'))

class TestListLetter(unittest.TestCase):

    def test_deve_retornar_ac_b_dc(self):
        self.assertEqual(['ac','b','dc'], list_letter('(ac)b(dc)') )

    def test_deve_retornar_acsd_fdseasdds_abc_d_adsaa_asd_poqwea_asdd_a(self):
        self.assertEqual(['acsd','fdseasdds','abc','d','adsaa','asd','poqwea','asdd','a'], list_letter('(acsd)(fdseasdds)(abc)d(adsaa)(asd)(poqwea)(asdd)a'))

unittest.main()
