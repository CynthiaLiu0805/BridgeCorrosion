'''
This module provides the unit test for visualization module. A made up dataframe is used for better performance. Due to 
the nature of plotting, this module only tests if the result of drawing graph is a plotly div.
'''
import unittest
import visualization
class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.data = {
            'LAT': '40.7128',
            'LON': '-74.0060',
            '2006': '1',
            '2007': '2',
            '2008': '3',
            '2009': '4'
        }
        
    def test_generate_sub_keylist(self):
        result = visualization.generate_sub_keylist(self.data, 2)
        self.assertEqual(result, ['2006', '2007', '2008', '2009'])

    def test_generate_sub_valuelist(self):
        result = visualization.generate_sub_valuelist(self.data, 3)
        self.assertEqual(result, ['2', '3', '4'])

    def test_draw_graph(self):
        result = visualization.draw_graph(self.data)
        self.assertIn('<div id=', result)  # Check that the result is a Plotly div

if __name__ == '__main__':
    unittest.main()