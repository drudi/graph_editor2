# -*- coding: utf-8 -*-

class IndexValidator(object):
    """
    Class responsible to validate user input for pixel and shape
    coordinates.
    """

    def __init__(self, canvas):
        """
        This class is initialized with the canvas for which the
        input will be valitated.
        """
        self.canvas = canvas

    def h_validate(self, value):
        """
        Check if the input value is inside the canvas regarding
        horizontal coordinates (columns).
        Returns True on success or False on error.
        """
        if (not isinstance(value, int) or value < 0):
            raise ValueError("Value must be positive integer.")
        if value < 0 or value > len(self.canvas.canvas[0]):
            raise IndexError("Value must be inside the canvas")
        return True

    def v_validate(self, value):
        """
        Check if the inpute value is inside the canvas regarding
        vertical coordinates (rows).
        Returns True on success or False on error.
        """
        if (not isinstance(value, int) or value < 0):
            raise ValueError("Value must be positive integer.")
        if value < 0 or value > len(self.canvas.canvas):
            raise IndexError("Value must be inside the canvas")
        return True
