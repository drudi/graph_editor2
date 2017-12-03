# -*- coding: utf-8 -*-

class Canvas(object):
    """
    This class represents the canvas where the drawings will occur.
    It's implemented as a two-dimentional matrix using standar python data types.
    """

    def __init__(self, columns, rows):
        """Initialize the Matrix (Canvas)"""
        self.canvas = [['O' for j in range(columns)] for i in range(rows)]

    def set_pixel(self, column, row, color):
        """Set a singles pixel in the canvas"""
        self.canvas[row - 1][column - 1] = color

    def clear(self):
        """Reset the canvas, setting all pixels to 'O'"""
        for row in range(len(self.canvas)):
            for column in range(len(self.canvas[row])):
                self.canvas[row][column] = 'O'

    def draw_vertical_segment(self, column, upper_row, lower_row, color):
        """Draw a vertical segment on the canvas."""
        upper_row, lower_row = self._order_elements(upper_row, lower_row)
        for row in range(upper_row, lower_row + 1):
            self.canvas[row - 1][column - 1] = color

    def _order_elements(self, a, b):
        if a <= b:
            return (a, b)
        return (b, a)

    def draw_horizontal_segment(self, row, leftmost_column, rightmost_column, color):
        """Draw a horizontal segment on the canvas."""
        for column in range(leftmost_column, rightmost_column + 1):
            self.canvas[row - 1][column - 1] = color
