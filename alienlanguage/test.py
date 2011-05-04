import unittest
from alienlang import alien_trans, list_letter, times_in_words

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

class TestTimesInWords(unittest.TestCase):

    def test_do_caso_de_test_2_de_small_deve_retornar_certo(self):
        word_test = 'nwlr(nqxb)bm(dgqw)bh'
        words = 'nwlrbbmqbh\ncdarzowkky\nhiddqscdxr\njmowfrxsjy\nbldbefsarc\nbynecdyggx\nxpklorelln\nmpapqfwkho\npkmcoqhnwn\nkuewhsqmgb\nbuqcljjivs\nwmdkqtbxix\nmvtrrbljpt\nnsnfwzqfjm\nafadrrwsof\nsbcnuvqhff\nbsaqxwpqca\ncehchzvfrk\nmlnozjkpqp\nxrjxkitzyx\nacbhhkicqc\noendtomfgd\nwdwfcgpxiq\nvkuytdlcgd\newhtacioho\nrdtqkvwcsg'.split('\n')
        self.assertEqual(1, times_in_words(words, word_test, list_letter(word_test), 10))

    def test_de_caso_teste_deve_retornar_3(self):
        word_test = '(ab)(etca)(de)(hd)'
        words = 'aedh\nated\nbaeh\naaae'.split('\n')
        self.assertEqual(3, times_in_words(words, word_test, list_letter(word_test), 4))

unittest.main()
