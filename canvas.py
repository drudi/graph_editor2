# -*- coding: utf-8 -*-

class Canvas(object):
    """
    This class represents the canvas where the drawings will occur.
    It's implemented as a two-dimentional matrix using standard python data types.
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
        leftmost_column, rightmost_column = self._order_elements(leftmost_column, rightmost_column)
        for column in range(leftmost_column, rightmost_column + 1):
            self.canvas[row - 1][column - 1] = color

    def draw_rectangle(self, upper_row, upper_col, lower_row, lower_col, color):
        """Draw a rectangle"""
        upper_row, lower_row = self._order_elements(upper_row, lower_row)
        upper_col, lower_col = self._order_elements(upper_col, lower_col)
        for row in range(upper_row, lower_row + 1):
            for col in range(upper_col, lower_col + 1):
                self.canvas[row - 1][col -1] = color

    def paint_region(self, row, column, color):
        """
        Paint a region with color.
        A region is defined as the same color pixels adjacent
        to pixel in the parameter.
        """
        original_color = self.canvas[row - 1][column - 1] # store the original color

        # Define a recursive closure to search the region
        def fill(r, c):
            if r < 0 or r > len(self.canvas) - 1: # outside the canvas
                return None
            if c < 0 or c > len(self.canvas[0]) - 1: #outside the canvas
                return None

            # If the color is different, we are outside the region boundary
            if self.canvas[r][c] != original_color:
                return None    
        
            # Pixel is in the region. Paint it!
            self.canvas[r][c] = color

            # Recursively paint adjacent pixels (or not)
            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        # Call the closure
        fill(row, column)



