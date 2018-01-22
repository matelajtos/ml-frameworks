import unittest
from github_class import Git

class GithubTestCase(unittest.TestCase):
    def setUp(self):
        self.git = Git('Tensorflow', 'https://github.com/tensorflow/tensorflow')

    def test_value(self):
        self.assertEqual(self.git.value, 96010)
        self.assertNotEqual(self.git.value, 64651)


if __name__ == '__main__':
    unittest.main()
