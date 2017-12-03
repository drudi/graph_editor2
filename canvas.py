# -*- coding: utf-8 -*-

class Canvas(object):
    """
    This class represents the canvas where the drawings will occur.
    It's implemented as a two-dimentional matrix using standar python data types.
    """

    def __init__(self, columns, rows):
        """Initialize the Matrix (Canvas)"""
        self.canvas = [['O' for j in range(columns)] for i in range(rows)]
