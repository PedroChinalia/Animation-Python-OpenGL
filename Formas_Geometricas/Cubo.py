#Importes
from OpenGL.GL import *

#Criando a classe Cubo.
class Cubo:

    #Construtor da classe Cubo.
    def __init__(self):

        #Definindo vértices do Cubo.
        #Os vértices são definidos a partir de sua posição x,y,z em relação ao plano cartesiano.
        self.verticesCubo = (
            (1,-1,-1),
            (1,1,-1),
            (-1,1,-1),
            (-1,-1,-1),
            (1,-1,1),
            (1,1,1),
            (-1,-1,1),
            (-1,1,1), 
        )

        #Definindo arestas do Cubo.
        #As arestas são definidas a partir da ligação entre dois vértices.
        self.arestasCubo = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7),
        )

        #Definindo as faces do Cubo.
        #As faces são construídas a partir da ligação entre arestas.
        self.facesCubo = (
            (0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6),
        )

        #Definindo cores do Cubo.
        #Padrão de cor RGB.
        self.coresCubo = (
            (1,0,1),
            (0,1,1),
            (1,0,1),
            (0,0,1),
            (1,0,1),
            (0,1,0),
        )

    #Definindo o método CriaCubo.
    def CriaCubo(self) :
        #Construindo as faces.
        glBegin(GL_QUADS)
        for face in self.facesCubo:
            x = 0

            for vertice in face:
                x += 1
                #Definindo as cores.
                glColor3fv(self.coresCubo[x])
                #Função para especificar um vértice.
                glVertex3fv(self.verticesCubo[vertice])
        
        glEnd()

        #Construindo as arestas.
        glBegin(GL_LINES)
        for aresta in self.arestasCubo:
            for vertice in aresta:
                #Função para especificar um vértice.
                glVertex3fv(self.verticesCubo[vertice])
        glEnd()