import unittest, sys, json
sys.path.insert(0, '..')
from app import app
sys.path.insert(0, '..')
from uber_data import data

class DashAppTestCase(unittest.TestCase):
    response = app.serve_layout()
    raw = response.data
    str = raw.decode()
    children = json.loads(str)['props']['children']

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_h1(self):
        self.assertEqual(self.children[0]['props']['children'], 'Hey, this is my first dash app!')
        self.assertEqual(self.children[0]['type'], 'H1')

    def test_p(self):
        self.assertEqual(self.children[1]['props']['children'], 'Still under construction... :)')
        self.assertEqual(self.children[1]['type'], 'P')

    def test_graph(self):
        self.assertEqual(self.children[2]['props']['id'], 'uber_pricing_graph')
        self.assertEqual(self.children[2]['props']['figure']['data'], data)
        self.assertEqual(self.children[2]['props']['figure']['layout']['title'], 'Uber Pricing in Brooklyn and Manhattan')
