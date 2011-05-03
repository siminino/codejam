import unittest
from storecredit import s_credit

class TestStoreCredit(unittest.TestCase):

    def test_10_credits_1_item_10_deve_retornar_1(self):
        self.assertEqual('1', s_credit(10,1,'10'))

    def test_100_credits_3_itens_deve_retornar_2_3(self):
        self.assertEqual('2 3', s_credit(100,3,'5 75 25'))

    def test_200_credit_7_itens_deve_retornar_1_4(self):
        self.assertEqual('1 4', s_credit(200,7,'150 24 79 50 88 345 3'))

    def test_8_credit_8_itens_deve_retornar_4_5(self):
        self.assertEqual('4 5', s_credit(8,8,'2 1 9 4 4 56 90 3'))

unittest.main()
