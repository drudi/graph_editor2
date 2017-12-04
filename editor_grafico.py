# !/usr/bin/python
# -*- coding: utf8 -*-

"""
Explicação
----------
Dada uma matriz de tamanho MxN na qual cada elemento represente um pixel, crie
um programa que leia uma sequência de comandos e os interprete manipulando a
matriz de acordo com a descrição abaixo de cada comando.

Comandos
--------
I M N
Cria uma nova matriz MxN. Todos os pixels são brancos (O).

C
Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos (O).

L X Y C
Colore um pixel de coordenadas (X,Y) na cor C.

V X Y1 Y2 C
Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
inclusivo) na cor C.

H X1 X2 Y C
Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
inclusivo) na cor C.

K X1 Y1 X2 Y2 C
Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (X2,Y2) o
canto inferior direito.

F X Y C
Preenche a região com a cor C. A região R é definida da seguinte forma:
O pixel (X,Y) pertence Ã  região. Outro pixel pertence Ã  região, se e somente se,
ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum com
um pixel pertencente Ã  região.

S name
Escreve a imagem em um arquivo de nome name.

X
Encerra o programa.

ConsideraÃ§Ãµes
-------------
Comandos diferentes de I, C, L, V, H, K, F, S e X devem ser ignorados

Testes
------

Entrada 01:

I 5 6
L 2 3 A
S one.bmp
G 2 3 J
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S two.bmp
X

Saida 01:

one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO

two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ

Entrada 02:

I 10 9
L 5 3 A
G 2 3 J
V 2 3 4 W
H 1 10 5 Z
F 3 3 J
K 2 7 8 8 E
F 9 9 R
S one.bmp
X

Saida 02:

one.bmp
JJJJJJJJJJ
JJJJJJJJJJ
JWJJAJJJJJ
JWJJJJJJJJ
ZZZZZZZZZZ
RRRRRRRRRR
REEEEEEERR
REEEEEEERR
RRRRRRRRRR
"""

import cmd
from canvas import Canvas
from input_validator import IndexValidator
from canvas_writer import CanvasWriter

class GraphicEditor(cmd.Cmd):
    """
    Class to handle commandline input and call the appropriate classes.
    Extends the Cmd class from the built-in module cmd.
    """

    prompt = "(editor)->"

    def do_I(self, input_line):
        """Initialize a new canvas (old canvas is discarded)"""
        M, N = input_line.split(' ')
        try:
            M = int(M)
            N = int(N)
        except:
            print("Only integers accepted.")
            return False
        if M < 0 or N < 0:
            print('Canvas dimensions must be positive.')
            return False
        self.canvas = Canvas(M, N)

    def do_X(self, input_line):
        """Exits the editor"""
        return True

    def do_C(self, input_line):
        """Clear the canvas"""
        self.canvas.clear()
        print("Canvas clear.")

    def do_L(self, input_line):
        """Draws a pixel on the current canvas"""
        X, Y, C = input_line.split(' ') 
        validator = IndexValidator(self.canvas)
        try:
            X = int(X)
            Y = int(Y)
            validator.v_validate(X)
            validator.v_validate(Y)
        except:
            print('Only integers accepted')
            return False
        self.canvas.set_pixel(X, Y, C)

    def do_V(self, input_line):
        """Command to draw a vertical line"""
        X, Y1, Y2, C = input_line.split(' ')
        validador = IndexValidator(self.canvas)
        try:
            X = int(X)
            Y1 = int(Y1)
            Y2 = int(Y2)
            validador.h_validate(X)
            validador.v_validate(Y1)
            validador.v_validate(Y2)
        except:
            print('Only integers accepted and must be inside limits.')
            return False
        self.canvas.draw_vertical_segment(X, Y1, Y2, C)

    def do_H(self, input_line):
        """Command to draw an horizontal line"""
        X1, X2, Y, C = input_line.split(' ')
        validator = IndexValidator(self.canvas)
        try:
            X1 = int(X1)
            X2 = int(X2)
            Y = int(Y)
            validator.h_validate(X1)
            validator.h_validate(X2)
            validator.v_validate(Y)
        except:
            print('Only integers accepted and must be inside limits.')
            return False
        self.canvas.draw_horizontal_segment(Y, X1, X2, C)

    def do_K(self, input_line):
        """Command to draw a rectangle"""
        X1, Y1, X2, Y2, C = input_line.split(' ')
        validator = IndexValidator(self.canvas)
        try:
            X1 = int(X1)
            Y1 = int(Y1)
            X2 = int(X2)
            Y2 = int(Y2)
            validator.h_validate(X1)
            validator.h_validate(X2)
            validator.v_validate(Y1)
            validator.v_validate(Y2)
        except:
            print('Only integers accepted and must be inside limits.')
            return False
        self.canvas.draw_rectangle(Y1, X1, Y2, X2, C)

    def do_F(self, input_line):
        """Command to paint a region"""
        X, Y, C = input_line.split(' ')
        validator = IndexValidator(self.canvas)
        try:
            X = int(X)
            Y = int(Y)
        except:
            print('Only integers accepted and must be inside limits.')
            return False
        self.canvas.paint_region(Y, X, C)
            
    def do_S(self, input_line):
        """Command to save the canvas in the path provided in the filename"""
        writer = CanvasWriter(self.canvas)
        writer.set_filename(input_line)
        writer.write()





def main():
    GraphicEditor().cmdloop()

if __name__ == '__main__':
    main()

