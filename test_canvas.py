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

        cls.pixel_set = [
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'X', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
            ]


    def test_create_new_canvas(self):
        canvas = Canvas(5, 6)
        self.assertEqual(self.new_canvas, canvas.canvas)

    def test_set_pixel_on_3_3(self):
        canvas = Canvas(5, 6)
        canvas.set_pixel(3, 3, 'X')
        self.assertEqual(self.pixel_set, canvas.canvas)

if __name__ == '__main__':
    unittest.main()
