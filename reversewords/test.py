import unittest
from codigo import reverse_words

class TestReverseWords(unittest.TestCase):


    def test_python_deve_retornar_python(self):
        self.assertTrue('python', reverse_words('python'))

    def test_hello_world_deve_retornar_world_hello(self):
        self.assertEqual('world hello', reverse_words('hello world'))

    def test_i_like_python_deve_retornar_python_like_i(self):
        self.assertEqual('python like i', reverse_words('i like python'))

    def test_this_is_a_test_deve_retornar_test_a_is_this(self):
        self.assertTrue('test a is this', reverse_words('this is a test'))
unittest.main()
