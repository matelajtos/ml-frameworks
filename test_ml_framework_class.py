import unittest
from ml_framework_class import MLFramework
from math import sqrt
import copy


class TestMLFramework(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c_mlf_1 = MLFramework('https://github.com/tensorflow/tensorflow')
        cls.c_mlf_2 = MLFramework('http://github.com/BVLC/caffe')
        cls.c_mlf_3 = MLFramework('https://github.com/opencv/opencv')

    @classmethod
    def tearDownClass(cls):
        """Once the database is set up, this might be needed."""
        pass

    def setUp(self):
        self.mlf_1 = copy.deepcopy(self.c_mlf_1)
        self.mlf_2 = copy.deepcopy(self.c_mlf_2)
        self.mlf_3 = copy.deepcopy(self.c_mlf_3)

    def tearDown(self):
        """Once the database is set up, this might be needed."""
        pass

    def test_create_api_link(self):
        self.assertEqual(self.mlf_1.create_api_link(), 'http://api.github.com/repos/tensorflow/tensorflow')
        self.mlf_1.link = 'https://google.com'
        self.assertRaises(RuntimeError, self.mlf_1.create_api_link)

        self.assertEqual(self.mlf_2.create_api_link(), 'http://api.github.com/repos/BVLC/caffe')
        self.assertEqual(self.mlf_3.create_api_link(), 'http://api.github.com/repos/opencv/opencv')
        
    def test_get_contributors(self):
        self.assertNotEqual(self.mlf_1.contributor_count, '')
        self.assertTrue(self.mlf_1.contributor_count >= 0)

        self.assertNotEqual(self.mlf_2.contributor_count, '')
        self.assertTrue(self.mlf_2.contributor_count >= 0)

        self.assertNotEqual(self.mlf_3.contributor_count, '')
        self.assertTrue(self.mlf_3.contributor_count >= 0)

    def test_score(self):
        self.assertEqual(self.mlf_1.score, int(sqrt(self.mlf_1.star_count**2
                                                    + self.mlf_1.watch_count**2
                                                    + self.mlf_1.fork_count**2
                                                    + self.mlf_1.contributor_count**2)))

        self.assertEqual(self.mlf_2.score, int(sqrt(self.mlf_2.star_count**2
                                                    + self.mlf_2.watch_count**2
                                                    + self.mlf_2.fork_count**2
                                                    + self.mlf_2.contributor_count**2)))

        self.assertEqual(self.mlf_3.score, int(sqrt(self.mlf_3.star_count**2
                                                    + self.mlf_3.watch_count**2
                                                    + self.mlf_3.fork_count**2
                                                    + self.mlf_3.contributor_count**2)))


if __name__ == '__main__':
    unittest.main()
