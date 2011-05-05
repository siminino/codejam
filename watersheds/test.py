import unittest
from watersheds import create_matriz

class TestCreateMatriz(unittest.TestCase):

    def test_1_1_should_return_1(self):
        self.assertEqual('1 1', len_matriz(1,1,'1'))
        self.assertEqual([['1']], create_matriz(1,1,'1'))

    def test_3_3_should_return_3_3(self):
        self.assertEqual('3 3', len_matriz(3,3, '1 2 3\n4 5 6\n7 8 9'))

    def test_5_5_should_return_5_5(self):
        self.assertEqual('5 5', len_matriz(5,5, '1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5'))

    def test_2_3_should_return_2_3(self):
        self.assertEqual('2 3', len_matriz(2,3, '1 2 3\n1 2 3'))


def len_matriz(H, W, content):
    result = []
    matriz = create_matriz(H, W, content)
    result.append(str(len(matriz)))
    for item in range(len(matriz)):
        if len(matriz[item]) == W:
            line_elements = str(len(matriz[item]))
        else:
            return 'Error'
    result.append(line_elements)

    return ' '.join(result)

unittest.main()
