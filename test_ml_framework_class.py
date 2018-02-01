import unittest
import ml_framework_class
from math import sqrt
import copy
import requests
import requests_mock
import json


@requests_mock.mock()
def get_response(api_link, m):
    repo_name = api_link.split('/')[-1]
    filename = 'test_responses/' + repo_name + '.json'
    with open(filename, 'r') as f:
        fake_response = f.read()
    m.get(api_link, headers={'status': '200 OK'}, text=fake_response)
    return requests.get(api_link)


def get_contributor_count(api_link):
    repo_name = api_link.split('/')[-1]
    with open('test_responses/contributors.json') as f:
        return json.load(f)[repo_name]


ml_framework_class.get_response = get_response
ml_framework_class.get_contributor_count = get_contributor_count


class TestMLFramework(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c_mlf_1 = ml_framework_class.MLFramework('https://github.com/tensorflow/tensorflow')
        cls.c_mlf_2 = ml_framework_class.MLFramework('http://github.com/BVLC/caffe')
        cls.c_mlf_3 = ml_framework_class.MLFramework('https://github.com/opencv/opencv')
        cls.c_mlf_4 = ml_framework_class.MLFramework('https://github.com/scikit-learn/scikit-learn')
        cls.c_mlf_5 = ml_framework_class.MLFramework('https://github.com/keras-team/keras')

    @classmethod
    def tearDownClass(cls):
        """Once the database is set up, this might be needed."""
        pass

    def setUp(self):
        self.mlf_1 = copy.deepcopy(self.c_mlf_1)
        self.mlf_2 = copy.deepcopy(self.c_mlf_2)
        self.mlf_3 = copy.deepcopy(self.c_mlf_3)
        self.mlf_4 = copy.deepcopy(self.c_mlf_4)
        self.mlf_5 = copy.deepcopy(self.c_mlf_5)

    def tearDown(self):
        """Once the database is set up, this might be needed."""
        pass

    def test_create_api_link(self):
        self.assertEqual(self.mlf_1.create_api_link(), 'http://api.github.com/repos/tensorflow/tensorflow')
        self.mlf_1.link = 'https://google.com'
        self.assertRaises(ml_framework_class.MLFramework.InvalidLinkException, self.mlf_1.create_api_link)
        
        self.assertEqual(self.mlf_2.create_api_link(), 'http://api.github.com/repos/BVLC/caffe')
        self.assertEqual(self.mlf_3.create_api_link(), 'http://api.github.com/repos/opencv/opencv')
        self.assertEqual(self.mlf_4.create_api_link(), 'http://api.github.com/repos/scikit-learn/scikit-learn')
        self.assertEqual(self.mlf_5.create_api_link(), 'http://api.github.com/repos/keras-team/keras')

        
    def test_get_contributors(self):
        self.assertEqual(self.mlf_1.contributor_count, 1296)
        self.assertEqual(self.mlf_2.contributor_count, 257)
        self.assertEqual(self.mlf_3.contributor_count, 848)
        self.assertEqual(self.mlf_4.contributor_count, 1014)
        self.assertEqual(self.mlf_5.contributor_count, 616)
        

    def test_score(self):
        self.assertEqual(self.mlf_1.score, int(sqrt(87663**2 + 7354**2 + 42761**2 + 1296**2)))
        self.assertEqual(self.mlf_2.score, int(sqrt(22621**2 + 2148**2 + 13846**2 + 257**2)))
        self.assertEqual(self.mlf_3.score, int(sqrt(21849**2 + 1955**2 + 15805**2 + 848**2)))
        self.assertEqual(self.mlf_4.score, int(sqrt(25327**2 + 2010**2 + 12930**2 + 1014**2)))
        self.assertEqual(self.mlf_5.score, int(sqrt(24937**2 + 1499**2 + 9084**2 + 616**2)))


if __name__ == '__main__':
    unittest.main()
