import unittest
from ml_framework_class import Git
from math import sqrt

class GithubTestCase(unittest.TestCase):
    def setUp(self):
        self.git_1 = Git('https://github.com/tensorflow/tensorflow')

    def test_get_api_link(self):
        self.assertEqual(self.git_1.get_api_link(), 'http://api.github.com/repos/tensorflow/tensorflow')
        self.git_1.link = 'https://google.com' 
        self.assertRaises(RuntimeError, self.git_1.get_api_link)
        
    def test_get_contributors(self):
        self.assertNotEqual(self.git_1.contributors, '')
        self.assertTrue(self.git_1.contributors >= 0)

    def test_value(self):
        self.assertEqual(self.git_1.value, int(sqrt(self.git_1.stars**2
                                                 + self.git_1.watch**2
                                                 + self.git_1.forks**2
                                                 + self.git_1.contributors**2)))


if __name__ == '__main__':
    unittest.main()

