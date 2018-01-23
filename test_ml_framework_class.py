import unittest
from ml_framework_class import Git
from math import sqrt

class GithubTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.git_1 = Git('https://github.com/tensorflow/tensorflow')
        cls.git_2 = Git('http://github.com/BVLC/caffe')
        cls.git_3 = Git('https://github.com/opencv/opencv')

    def test_get_api_link(self):
        self.assertEqual(self.git_1.get_api_link(), 'http://api.github.com/repos/tensorflow/tensorflow')
        self.git_1.link = 'https://google.com' 
        self.assertRaises(RuntimeError, self.git_1.get_api_link)

        self.assertEqual(self.git_2.get_api_link(), 'http://api.github.com/repos/BVLC/caffe')
        self.assertEqual(self.git_3.get_api_link(), 'http://api.github.com/repos/opencv/opencv')
        
    def test_get_contributors(self):
        self.assertNotEqual(self.git_1.contributors, '')
        self.assertTrue(self.git_1.contributors >= 0)

        self.assertNotEqual(self.git_2.contributors, '')
        self.assertTrue(self.git_2.contributors >= 0)

        self.assertNotEqual(self.git_3.contributors, '')
        self.assertTrue(self.git_3.contributors >= 0)

    def test_value(self):
        self.assertEqual(self.git_1.value, int(sqrt(self.git_1.stars**2
                                                 + self.git_1.watch**2
                                                 + self.git_1.forks**2
                                                 + self.git_1.contributors**2)))

        self.assertEqual(self.git_2.value, int(sqrt(self.git_2.stars**2
                                                 + self.git_2.watch**2
                                                 + self.git_2.forks**2
                                                 + self.git_2.contributors**2)))

        self.assertEqual(self.git_3.value, int(sqrt(self.git_3.stars**2
                                                 + self.git_3.watch**2
                                                 + self.git_3.forks**2
                                                 + self.git_3.contributors**2)))

    def test_get_json(self):
        self.assertTrue(len(self.git_1.get_json()) > 0)
        self.assertTrue(len(self.git_2.get_json()) > 0)
        self.assertTrue(len(self.git_3.get_json()) > 0)


if __name__ == '__main__':
    unittest.main()
