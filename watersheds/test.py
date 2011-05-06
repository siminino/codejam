import unittest
from watersheds import create_matriz

class TestCreateMatriz(unittest.TestCase):

    def test_1_1_should_return_1(self):
        matriz = create_matriz(1,1,'1')
        self.assertEqual('1 1', len_matriz(1, matriz))
        self.assertEqual([['1']], matriz)

    def test_3_3_should_return_3_3(self):
        matriz = create_matriz(3,3, '1 2 3\n4 5 6\n7 8 9')
        self.assertEqual('3 3', len_matriz(3, matriz))
        self.assertEqual([['1','2','3'],['4','5','6'],['7','8','9']], matriz)

    def test_5_5_should_return_5_5(self):
        matriz = create_matriz(5,5, '1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5')
        self.assertEqual('5 5', len_matriz(5, matriz))
        self.assertEqual([['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5']], matriz) 

    def test_2_3_should_return_2_3(self):
        matriz = create_matriz(2,3,'1 2 3\n1 2 3')
        self.assertEqual('2 3', len_matriz(3, matriz))
        self.assertEqual([['1','2','3'],['1','2','3']], matriz)



def len_matriz(W, matriz):
    result = []
    result.append(str(len(matriz)))
    for item in range(len(matriz)):
        if len(matriz[item]) == W:
            line_elements = str(len(matriz[item]))
        else:
            return 'Error'
    result.append(line_elements)

    return ' '.join(result)

unittest.main()
