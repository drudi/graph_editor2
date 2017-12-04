# -*- coding: utf-8 -*-

class CanvasWriter(object):
    """This class is used to write a canvas object into a file"""

    def __init__(self, canvas):
        """Take a Canvas object as an argument"""
        self.canvas = canvas
        self.filename = ''

    def set_filename(self, filename):
        """Set the filename to write the canvas"""
        self.filename = filename

    def write(self):
        with open(self.filename, 'w') as output:
            for row in self.canvas.canvas:
                for column in row:
                    output.write(column)
                output.write("\n")
            output.close()

