# -*- coding: utf-8 -*-

import unittest
from canvas import Canvas

class TestCanvas(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.new_canvas = [
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
            ]

    def test_create_new_canvas(self):
        canvas = Canvas(5, 6)
        self.assertEqual(self.new_canvas, canvas.canvas)

if __name__ == '__main__':
    unittest.main()
