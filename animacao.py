#Importes
#Pygame
import pygame
from pygame import mixer 
from pygame.locals import *
#OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#Classes
from Formas_Geometricas.Piramide import *
from Formas_Geometricas.Cubo import *

#Criando uma pirâmide.
piramide = Piramide()

#Criando um cubo.
cubo = Cubo()     

#Definindo a funçao main.
def main() :
    #Iniciando PyGame.
    pygame.init()

    #Definindo tamanho do display.
    display = (1200,800)
    #Configuração de display em relação a buffer de vídeo.
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #Música de fundo.
    #A função 'mixer.music.load()' carrega a música passada como parâmetro.
    #A extensão de música ou efeito sonoro suportada pelo PyGame é a '.wav'.
    mixer.music.load('theme.wav')
    #A função 'mixer.music.play()' toca a música.
    #O parâmetro dessa função indica o número de vezes que a música será tocada.
    #Caso o parâmetro seja '-1', a função irá tocar a música infinitas vezes.
    mixer.music.play(-1)

    #Volume da música.
    #A variável 'volume' define o volume inicial da música.
    volume = 0.2
    #A função 'pygame.mixer.music.set_volume()' define o volume da música.
    #O parâmetro recebido pela função varia entre 0.0 à 1.0, sendo 0.0 o volume mínimo e 1.0 o volume máximo.
    pygame.mixer.music.set_volume(volume)

    #Perspectiva do objeto em relação ao display.
    gluPerspective(470, (display[0]/display[1]), 0.1, 50.0)
    #Posição do objeto em relação ao display.
    glTranslatef(0.0, 0.0, -5)
    #Rotação do objeto.
    glRotatef(0,0,0,0) 

    #Variáveis utilizadas como contadores.
    #A variável 'contador' irá definir qual forma geométrica irá aparecer na tela.
    contador = 0
    #A variável 'movimentacao' irá definir o fluxo pelo qual os objtos irão se movimentar.
    movimentacao = 1
    
    #Iniciando a condicional 'while' para criar um loop infinito.
    while True:        
        contador +=1
        movimentacao += 1

        #Condicional para controlar a variável 'movimentacao'.
        if (movimentacao > 520):
            movimentacao = -520
        
        #Adicionando interação com o volume da música.
        #A função 'pygame.key.get_pressed()' irá realizar uma ação quando alguma tecla do teclado for pressionada.
        #A tecla definida fica entre [].
        #Caso a tecla direcional para cima do teclado seja pressionada, o volume irá aumentar.
        if pygame.key.get_pressed()[pygame.K_UP]:
            pygame.mixer.music.set_volume((volume + 0.2))
        
        #Caso a tecla direcional para baixo do teclado seja pressionada, o volume irá diminuir.
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            pygame.mixer.music.set_volume((volume - 0.2))

        #Definindo as condições para as formas geométricas serem exibidas.
        #Enquanto a variável 'contador' for menor ou igual a 200, será exibido uma pirâmide.
        if (contador<=200):

            #Mudando os parâmetro de rotação.
            glRotatef(1,2,2,1) 
            #Configuração de buffer enquanto o objeto é exibido na tela.
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            #Definindo a posição do objeto.
            #Uma vez que a variável 'movimentacao' for mudando seu valor, a posição do objeto irá mudar.
            glTranslatef(movimentacao/(10**5), movimentacao/(10**5), movimentacao/(10**5))
            #Chama a função da classe Piramide para criar uma pirâmide.
            piramide.CriaPiramide()
            #Configurações de display enquanto o objeto é exibido na tela.
            pygame.display.flip()
            pygame.time.wait(10)   

            #Adicionando interação com o mouse.
            #A função 'pygame.mouse.get_pressed()' irá realizar uma ação quando algum botão do mouse for pressionado.
            #O botão do mouse definido fica entre [].
            #Caso o botão esquerdo do mouse seja pressionado, os parâmetros de rotação do objeto serão alterados.
            if pygame.mouse.get_pressed()[0]:   
                glRotatef(2,4,4,2)      

        #Definindo as condições para as formas geométricas serem exibidas.
        #Enquanto a variável 'contador' for menor ou igual a 400, será exibido um cubo.
        elif (contador <=400):

            #Mudando os parâmetro de rotação.
            glRotatef(1,3,1,1) 
            #Configuração de buffer enquanto o objeto é exibido na tela.
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            #Definindo a posição do objeto.
            #Uma vez que a variável 'movimentacao' for mudando seu valor, a posição do objeto irá mudar.
            glTranslatef(movimentacao/(10**5), movimentacao/(10**5), movimentacao/(10**5))
            #Chama a função da classe Cubo para criar um cubo.
            cubo.CriaCubo()
            #Configurações de display enquanto o objeto é exibido na tela.
            pygame.display.flip()
            pygame.time.wait(10)

            #Adicionando interação com o mouse.
            #A função 'pygame.mouse.get_pressed()' irá realizar uma ação quando algum botão do mouse for pressionado.
            #O botão do mouse definido fica entre [].
            #Caso o botão esquerdo do mouse seja pressionado, os parâmetros de rotação do objeto serão alterados.
            if pygame.mouse.get_pressed()[0]:   
                 glRotatef(2,6,2,2)

        #Definindo as condições para as formas geométricas serem exibidas.
        #Caso a variável 'contador' não atender as condicionais 'if' e 'elif', a variável 'contador' é resetada.
        else:
            contador = 0

        #Evento para encerrar o programa.
        for event in pygame.event.get (): 
            if event.type == pygame.QUIT:
                pygame.quit()    
                quit()

main()