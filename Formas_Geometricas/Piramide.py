#Importes
from OpenGL.GL import *

#Criando a classe Piramide.
class Piramide:

    #Construtor da classe Piramide.
    def __init__(self):

        #Definindo vértices da Pirâmide.
        #Os vértices são definidos a partir de sua posição x,y,z em relação ao plano cartesiano.
        self.verticesPiramide = (
            (1,0,0),
            (-1,-1,-1),
            (-1,1,-1),
            (-1,1,1),
            (-1,-1,1),
        )

        #Definindo arestas da Pirâmide.
        #As arestas são definidas a partir da ligação entre dois vértices.
        self.arestasPiramide = (
            (0,1),
            (0,2),
            (0,3),
            (0,4),
            (1,2),
            (2,3),
            (3,4),
            (4,1),
        )

        #Definindo faces da Pirâmide.
        #As faces são construídas a partir da ligação entre arestas.
        self.facesPiramide = (
            (0,1,4),
            (1,2,4),
            (2,3,4),
            (3,0,4),
            (0,1,2,3),
        )

        #Definindo cores da Pirâmide.
        #Padrão de cor RGB.
        self.coresPiramide = (
            (0,0,0),
            (1,1,0),
            (1,0,1),
            (1,0,0),
            (1,1,1),
            (1,1,0),
        ) 

    #Definindo o método CriaPiramide.
    def CriaPiramide(self) :
        #Construindo as faces.
        glBegin(GL_QUADS)
        for face in self.facesPiramide:
            x = 0

            for vertice in face:
                x += 1
                #Definindo as cores.
                glColor3fv(self.coresPiramide[x])
                #Função para especificar um vértice.
                glVertex3fv(self.verticesPiramide[vertice])
        
        glEnd()

        #Construindo as arestas.
        glBegin(GL_LINES)
        for aresta in self.arestasPiramide:
            for vertice in aresta:
                #Função para especificar um vértice.
                glVertex3fv(self.verticesPiramide[vertice])
        glEnd()