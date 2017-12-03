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

        cls.vertical_line = [
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'O'],
            ]

        cls.horizontal_line = [
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['X', 'X', 'X', 'X', 'O'],
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

    def test_clear_canvas(self):
        canvas = Canvas(5, 6)
        canvas.set_pixel(3, 3, 'X')
        canvas.clear()
        self.assertEqual(self.new_canvas, canvas.canvas)

    def test_draw_vertical_line(self):
        canvas = Canvas(5, 6)
        canvas.draw_vertical_segment(4, 2, 6, 'X')
        self.assertEqual(self.vertical_line, canvas.canvas)

    def test_draw_vertical_line_with_unordered_parameters(self):
        canvas = Canvas(5, 6)
        canvas.draw_vertical_segment(4, 6, 2, 'X')
        self.assertEqual(self.vertical_line, canvas.canvas)

    def test_draw_horizontal_line(self):
        canvas = Canvas(5, 6)
        canvas.draw_horizontal_segment(3, 1, 4, 'X')
        self.assertEqual(self.horizontal_line, canvas.canvas)


if __name__ == '__main__':
    unittest.main()
