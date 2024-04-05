import pygame
import os

from pygame.constants import K_RETURN
from poke_informações import Player
from golpes import Golpes, vantagem
from time import sleep
from jogodacobrinha import jogo
import random

pygame.init() # Iniciando o pygame

# Atribuindo as cores à variáveis
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
OUTRO_AZUL = (127,0,255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
ROXO = (159,95,159)
MARROM_CLARO = (233,194,166)
CINZA = (76, 76, 76)


class Window:
    __width = 0 #largura
    __height = 0 #altura
    __color = (0, 0, 0) #cor

    def __init__(self, largura, altura): #construtor
        self.__width = largura
        self.__height = altura

    def returnWinSize(self): #retorna tamanho da tela
        return (self.__width, self.__height)

    def returnColor(self): #retorna a cor da janela
        return self.__color


# Função para definir as coordenadas e o tamanho dos textos:
def Texto(texto, cor, coordenadas, tamanho, win):  
  font = pygame.font.Font('joystix_monospace.ttf', tamanho)
  texto1 = font.render(texto, False, cor)
  win.blit(texto1, coordenadas)

# Função para mudar a posição da seta na tela inicial:
def selecionar_Pokemon(cont, win): 
     # Selecionando o pokémon de acordo com o seu índice
    if cont == 0:
        pygame.draw.polygon(win, VERMELHO, ((285,115), (285,125), (290,120)), 0) #0 
    elif cont == 1: 
        pygame.draw.polygon(win, VERMELHO, ((285,145), (285,155), (290,150)), 0) #1
    elif cont == 2:
        pygame.draw.polygon(win, VERMELHO, ((285,175), (285,185), (290,180)), 0) #2
    elif cont == 3:
        pygame.draw.polygon(win, VERMELHO, ((285,205), (285,215), (290,210)), 0) #3
    elif cont == 4:
        pygame.draw.polygon(win, VERMELHO, ((285,235), (285,245), (290,240)), 0) #4
    elif cont == 5:
        pygame.draw.polygon(win, VERMELHO, ((285,265), (285,275), (290,270)), 0) #5
    elif cont == 6:
        pygame.draw.polygon(win, VERMELHO, ((285,295), (285,305), (290,300)), 0) #6  
    elif cont == 7:
        pygame.draw.polygon(win, VERMELHO, ((285,325), (285,335), (290,330)), 0) #7

# Função para mostrar o nome, o tipo e o pp dos golpes do respectivo pokémon: 
def nome_golpes(valor_pokemon1, valor_pokemon2, turno1, cont_golpes, classe = Golpes):
    nomes_golpes = classe().nome_golpe
    tipo = classe().tipo_golpe
    pp = classe().pp_golpe

    # Pps do pokémon 1  
    global Menos_pp1_0 
    global Menos_pp1_1 
    global Menos_pp1_2 
    global Menos_pp1_3 

    # Pps do pokémon 2  
    global Menos_pp2_0 
    global Menos_pp2_1 
    global Menos_pp2_2 
    global Menos_pp2_3 

    pp1 = pp[valor_pokemon1] # pp1 = lista de pps do pokémon 1 
    pp2 = pp[valor_pokemon2] # pp2 = lista de pps do pokémon 2

    if turno1: # Vez do player 1
        Texto(nomes_golpes[valor_pokemon1][0], PRETO, [31, 490], 23, win)
        Texto(nomes_golpes[valor_pokemon1][1], PRETO, [290, 490], 23, win)
        Texto(nomes_golpes[valor_pokemon1][2], PRETO, [31, 535], 23, win)
        Texto(nomes_golpes[valor_pokemon1][3], PRETO, [290, 535], 23, win)

        # Colocando na tela o pp e o tipo de cada golpe
        if cont_golpes == 0:
            Texto(tipo[valor_pokemon1][0], CINZA, [637, 543], 22, win)
            Texto(str(pp1[0]-Menos_pp1_0), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon1][0]), PRETO, [730, 485], 27, win)
        if cont_golpes == 1:
            Texto(tipo[valor_pokemon1][1], CINZA, [637, 543], 22, win)
            Texto(str(pp1[1]-Menos_pp1_1), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon1][1]), PRETO, [730, 485], 27, win)
        if cont_golpes == 2:
            Texto(tipo[valor_pokemon1][2], CINZA, [637, 543], 22, win)
            Texto(str(pp1[2]-Menos_pp1_2), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon1][2]), PRETO, [730, 485], 27, win)
        if cont_golpes == 3:
            Texto(tipo[valor_pokemon1][3], CINZA, [637, 543], 22, win)
            Texto(str(pp1[3]-Menos_pp1_3), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon1][3]), PRETO, [730, 485], 27, win)

    else: # Vez do player 2
        Texto(nomes_golpes[valor_pokemon2][0], PRETO, [31, 490], 23, win)
        Texto(nomes_golpes[valor_pokemon2][1], PRETO, [290, 490], 23, win)
        Texto(nomes_golpes[valor_pokemon2][2], PRETO, [31, 535], 23, win)
        Texto(nomes_golpes[valor_pokemon2][3], PRETO, [290, 535], 23, win)

        # Colocando na tela o pp e o tipo de cada golpe
        if cont_golpes == 0:
            Texto(tipo[valor_pokemon2][0], CINZA, [637, 543], 22, win)
            Texto(str(pp2[0]-Menos_pp2_0), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon2][0]), PRETO, [730, 485], 27, win)
        if cont_golpes == 1:
            Texto(tipo[valor_pokemon2][1], CINZA, [637, 543], 22, win)
            Texto(str(pp2[1]-Menos_pp2_1), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon2][1]), PRETO, [730, 485], 27, win)
        if cont_golpes == 2:
            Texto(tipo[valor_pokemon2][2], CINZA, [637, 543], 22, win)
            Texto(str(pp2[2]-Menos_pp2_2), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon2][2]), PRETO, [730, 485], 27, win)
        if cont_golpes == 3:
            Texto(tipo[valor_pokemon2][3], CINZA, [637, 543], 22, win)
            Texto(str(pp2[3]-Menos_pp2_3), PRETO, [660, 485], 27, win)
            Texto(str(pp[valor_pokemon2][3]), PRETO, [730, 485], 27, win)

# Função para selecionar os golpes:
def selecionador_golpes(cont_golpes, win): 
    if cont_golpes == 0:
        pygame.draw.rect(win, VERMELHO, ((27,485), (238,40)), 2)
    if cont_golpes == 2:
        pygame.draw.rect(win, VERMELHO, ((27,530), (238,40)), 2)
    if cont_golpes == 1:
        pygame.draw.rect(win, VERMELHO, ((285,485), (218,40)), 2)
    if cont_golpes == 3:
        pygame.draw.rect(win, VERMELHO, ((285,530), (218,40)), 2)

# Função para adicionar à tela de combate todos os "objetos" que não serão retirados durante a batalha, mas que podem sofrer alteração de posição:
def tela_combate(combate, barra_de_movimento, player):
    # Atriubuindo a lista com os nomes do pokemons a outra lista
    lista_pokemons = Player().pokemon_information[2]

    win.blit(fundo_novo,(0,0)) # Definindo a posição da imagem de fundo (x, y)
    
    if combate:
        win.blit(text_bar_novo, (0,450)) # Definindo a posição da barra de mensagens
        win.blit(fgt_options_novo,(480,450)) # Definindo a posição da barra de opções (x, y)

        if barra_de_movimento == 0:
            pygame.draw.rect(win, VERMELHO, ((520,485), (115,40)), 2) # Definindo o retângulo do botão "FIGHT"
        elif barra_de_movimento == 1:
            pygame.draw.rect(win, VERMELHO, ((669,485), (115,40)), 2) # Definindo o retângulo do botão "BAG"
        elif barra_de_movimento == 2:
            pygame.draw.rect(win, VERMELHO, ((520,535), (115,40)), 2) # Definindo o retângulo do botão "POKÉMON"
        elif barra_de_movimento == 3:
            pygame.draw.rect(win, VERMELHO, ((669,535), (115,40)), 2) # Definindo o retângulo do botão "RUN"
   
    win.blit(barra_2_novo,(439,305)) # Definindo a posição da barra 2
    win.blit(barra_1_novo,(80,60)) # Definindo a posição da barra 1
    
    global Xinferior
    global Xsuperior
    global vida_player1
    global vida_player2
    global vez_player1

    # Alternando a posição da barra de vida conforme o pokémon que ataca (vez_player1)
    posicao_vida(Xinferior, Xsuperior, vida_player1, vida_player2, barra_amarela1, barra_amarela2, barra_vermelha1, barra_vermelha2, vez_player1)

    Texto('80', CINZA, [325, 73], 25, win)
    Texto('80', CINZA, [707, 332], 25, win)

    # Mostrando a mensagem na tela de combate (ao lado esquerdo dos botões "FIGHT", "RUN"...):
    Texto("What should", BRANCO, [50, 485], 30, win)
    Texto(lista_pokemons[player] + " do?", BRANCO, [50, 530], 30, win)
  
# Função para adicionar o fundo da parte onde se mostra o nome dos golpes, pp e tipo (depois de entrar no menu FIGHT):
def fundo_fight():
    tela = pygame.image.load(os.path.join('SpritesInterface', 'pp_bar.png'))
    tela = pygame.transform.scale(tela, (800, 150))
    win.blit(tela, (0, 450))

# Função para definir as posições dos pokémons de frente e de costas, as mensagens ("pouco efetivo", "super efetivo") e o highlight no que sofreu golpe:
def posicoes(x1, y1, x2, y2, contador1, contador2, highlight = False, informacoes = Player):
    Jogador = informacoes()
    global vez_player1

    # Mostrando na tela o pokémon de costas
    if vez_player1 == False and contador1 == contador2:
        # Shiny ativado
        pokecost1 = pygame.image.load(os.path.join('Trás', Jogador.pokemon_information[1][contador1+8]))
    else:
        pokecost1 = pygame.image.load(os.path.join('Trás', Jogador.pokemon_information[1][contador1]))
    pokecost1 = pygame.transform.scale(pokecost1, (200, 200)) # Definindo o tamanho
    
    if highlight == False:
        win.blit(pokecost1, (x1, y1)) # Definindo a posição

    # Colocando o nome do pokémon na respectiva barra de vida
    Texto((Jogador.pokemon_information[2][contador1]), PRETO, [495, 335], 22, win)

    # Mostrando na tela o pokémon de frente
    if vez_player1 == True and contador1 == contador2:
        #Shiny ativado
        pokefren2 = pygame.image.load(os.path.join('Frente', Jogador.pokemon_information[0][contador2+8]))
    else:
        pokefren2 = pygame.image.load(os.path.join('Frente', Jogador.pokemon_information[0][contador2]))
    pokefren2 = pygame.transform.scale(pokefren2, (200, 200)) # Definindo o tamanho
    
    if highlight == False:
        win.blit(pokefren2, (x2, y2)) # Definindo a posição
    
    # Colocando o nome do pokémon na respectiva barra de vida
    Texto((Jogador.pokemon_information[2][contador2]), PRETO, [100, 75], 22, win)

    if highlight:
        global cont_golpes

        global barra_sem_vida
        global barra_amarela
        global barra_vermelha

        global danoNoP2
        global vida_player2
        global barra_amarela2
        global barra_vermelha2

        global danoNoP1
        global vida_player1
        global barra_amarela1
        global barra_vermelha1

        if vez_player1:
            # Calculando o dano com ajuda da função "dano _golpe"
            danoNoP2 += dano_golpe(contador1, contador2, cont_golpes, vez_player1)
            if danoNoP2 >= 157:
                danoNoP2 = 157

            # Modificando a barra de vida do player 2
            vida_player2 = pygame.transform.scale(barra_sem_vida, (danoNoP2,10))

            if danoNoP2 >= 80: # Modificando a cor da vida do pokémon para amarelo
                barra_amarela2 = pygame.transform.scale(barra_amarela, (80-(danoNoP2-77),10))
            if danoNoP2 >= 115: # Modificando a cor da vida do pokémon para vermelho
                barra_vermelha2 = pygame.transform.scale(barra_vermelha, (42-(danoNoP2-115),10))

            for c in range(8):
                tela_combate(combate, cursor, player1) # Mostrando os "objetos" secundários da tela de combate
                fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                nome_golpes(player1, player2, vez_player1, cont_golpes)  # Mostrando as opções de golpes
                win.blit(pokecost1, (x1, y1)) # Definindo a posição

                if c % 2 != 0:
                    win.blit(pokefren2, (x2, y2)) # Definindo a posição

                #Mostrar o nome dos pokémons durante o highlight
                Texto((Jogador.pokemon_information[2][contador1]), PRETO, [495, 335], 22, win)
                Texto((Jogador.pokemon_information[2][contador2]), PRETO, [100, 75], 22, win)

                # Calculando a vantagem do pokémon de acordo com seu tipo e o seu adversário, e mostrando uma mensagem
                if vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) != 1:
                    win.blit(barra_texto_novo, (0, 450))    #Super Efetivo
                    if vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) >= 2:
                        Texto("It's super effective!", BRANCO, [30, 480], 25, win)

                    elif vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) == 0:
                        Texto("It doesn't affect", BRANCO, [30, 480], 25, win)  #Golpe não afeta o oponente
                        Texto(Jogador.pokemon_information[2][contador2], BRANCO, [30, 520], 25, win)
                    
                    elif vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) < 1:
                        Texto("It's not very effective...", BRANCO, [30, 480], 25, win)  #Inefetivo
                
                pygame.display.update()
                sleep(0.1)
        
        else: # Se for a vez do player 2
            danoNoP1 += dano_golpe(contador1, contador2, cont_golpes, vez_player1)
            if danoNoP1 >= 157:
                danoNoP1 = 157

            # Modificando a barra de vida do player 1
            vida_player1 = pygame.transform.scale(barra_sem_vida, (danoNoP1,10))
            
            if danoNoP1 >= 80: # Modificando a barra de vida para amarelo
                barra_amarela1 = pygame.transform.scale(barra_amarela, (80-(danoNoP1-77), 10)) # Definindo a posição na tela - Barra inferior
            if danoNoP1 >= 115: # Modificando a barra de vida para vermelho
                barra_vermelha1 = pygame.transform.scale(barra_vermelha, (42-(danoNoP1-115), 10)) # Definindo a posição na tela - Barra inferior

            for c in range(8):
                tela_combate(combate, cursor, player2) # Mostrando os "objetos" secundários da tela de combate
                fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes
                win.blit(pokecost1, (x1, y1)) # Definindo a posição
                
                if c % 2 != 0:
                    win.blit(pokefren2, (x2, y2)) # Definindo a posição
                
                #Mostrar o nome dos pokémons durante o highlight
                Texto((Jogador.pokemon_information[2][contador1]), PRETO, [495, 335], 22, win)
                Texto((Jogador.pokemon_information[2][contador2]), PRETO, [100, 75], 22, win)

                # Calculando a vantagem do pokémon de acordo com seu tipo e o seu adversário, e mostrando uma mensagem
                if vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) != 1:
                    win.blit(barra_texto_novo, (0, 450))
                    
                    if vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) >= 2:
                        Texto("It's super effective!", BRANCO, [30, 480], 25, win)  #Super efetivo

                    elif vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) == 0:
                        Texto("It doesn't affect", BRANCO, [30, 480], 25, win)  #Golpe não surte efeito no oponente
                        Texto(Jogador.pokemon_information[2][contador2], BRANCO, [30, 520], 25, win)

                    elif vantagem(Golpes().tipo_golpe[contador1][cont_golpes], contador2) < 1:
                        Texto("It's not very effective...", BRANCO, [30, 480], 25, win)   #Inefetivo

                pygame.display.update()
                sleep(0.1)

# Função para exibir os sprites dos pokémons na tela (player 1 e 2)
def mostrar_pokemon(pokemon_player1, pokemon_player2, vez_player1, x1, x2, highlight = False):
   # Vez do player 1
  if vez_player1 == True: 
    if pokemon_player1 == 0: # Se for o Pikachu
        # Chamando a função que mostra os pokémons na tela
        posicoes(x1, 271, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 1: # Se for o Charizard
        posicoes(x1, 262, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 2: # Se for o Venusaur
        posicoes(x1, 281, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 3: # Se for o Blastoise
        posicoes(x1, 281, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 4: # Se for o Golem
        posicoes(x1, 300, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 5: # Se for o Gengar
        posicoes(x1, 281, x2, 100, pokemon_player1, pokemon_player2, highlight)
    elif pokemon_player1 == 6: # Se for o Dragonite
        posicoes(x1, 268, x2, 100, pokemon_player1, pokemon_player2, highlight)
    else: # Se for o Mewtwo
        posicoes(x1, 253, x2, 100, pokemon_player1,pokemon_player2, highlight)

  # Vez do player 2
  else:
      # Configurando a posição de cada pokémon de costas para que não fique sobreposto a barra de mensagens    
      # Chamando a função que mostra os pokémons na tela
      if pokemon_player2 == 0: # Se for o Pikachu      
          posicoes(x1, 271, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 1: # Se for o Charizard
          posicoes(x1, 262, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 2: # Se for o Venusaur
          posicoes(x1, 281, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 3: # Se for o Blastoise
          posicoes(x1, 281, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 4: # Se for o Golem
          posicoes(x1, 300, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 5: # Se for o Gengar
          posicoes(x1, 281, x2, 100, pokemon_player2, pokemon_player1, highlight)
      elif pokemon_player2 == 6: # Se for o Dragonite
          posicoes(x1, 268, x2, 100, pokemon_player2, pokemon_player1, highlight)
      else: # Se for o Mewtwo
          posicoes(x1, 253, x2, 100, pokemon_player2, pokemon_player1, highlight)
   
# Função para modificar o tamanho das barra de vida dos pokémons
def posicao_vida(Xinferior, Xsuperior, vida_player1, vida_player2, barra_amarela1, barra_amarela2, barra_vermelha1, barra_vermelha2, vez_player1, classe = Golpes):
    hp = classe().hp

    global danoNoP1
    global danoNoP2

    # Definindo a vida númerica fixa dos pokémons (hp-dano/hp_fixo)
    hp1_fixo = hp[player1][0] # Vida numérica à direita da barra (hp_alterável/hp_fixo) - Player 1
    hp2_fixo = hp[player2][0] # Vida numérica à direita da barra (hp_alterável/hp_fixo) - Player 2

    # Calculando o dano no pokémon em relação a sua vida numérica
    hp1 = int(hp1_fixo - (danoNoP1*hp1_fixo/157)) # hp1 = hp_alterável (player 1)
    hp2 = int(hp2_fixo - (danoNoP2*hp2_fixo/157)) # hp2 = hp_alterável (player 2)

    if vez_player1: # Se o player 1 atacar
        win.blit(vida_player2, (Xsuperior-danoNoP2, 116)) # Definindo a posição na tela - Barra superior
        win.blit(vida_player1, (Xinferior-danoNoP1, 374)) # Definindo a posição na tela - Barra inferior

        # Mostrando na tela a vida numérica do pokémon do player 1
        Texto(str(hp1)+"/"+str(hp1_fixo), CINZA, [615, 394], 22, win) # Definindo o HP numérico na tela (player 1)

        # Condições para mudar as cores da barra de vida para amerelo e vermelho (dano sofrido pelo player 2)
        if danoNoP2 >= 80:
            win.blit(barra_amarela2, (211, 116))
        if danoNoP2 >= 115:
            win.blit(barra_vermelha2, (211, 116))
        
        if danoNoP1 >= 80:
            win.blit(barra_amarela1, (597, 374))
        if danoNoP1 >= 115:
            win.blit(barra_vermelha1, (597, 374))
    
    else: # Se o player 2 atacar
        win.blit(vida_player1, (Xsuperior-danoNoP1, 116)) # Definindo a posição na tela - Barra superior
        win.blit(vida_player2, (Xinferior-danoNoP2, 374)) # Definindo a posição na tela - Barra inferior

        # Mostrando na tela a vida numérica do pokémon do player 2
        Texto(str(hp2) +"/"+ str(hp2_fixo), CINZA, [615, 394], 22, win) # Definindo o HP numérico na tela (player 2)

        # Condições para mudar as cores da barra de vida para amerelo e vermelho (dano sofrido pelo player 1)
        if danoNoP1 >= 80:
            win.blit(barra_amarela1, (211, 116))
        if danoNoP1 >= 115:
            win.blit(barra_vermelha1, (211, 116))

        if danoNoP2 >= 80:
            win.blit(barra_amarela2, (597, 374))
        if danoNoP2 >= 115:
            win.blit(barra_vermelha2, (597, 374))

# Função para calcular o dano parcial do golpe deferido
def dano_golpe(pokémon1, pokémon2, cursor, vez_player1 = True, classe=Golpes):
    if vez_player1:
        if classe().pp_golpe[pokémon1][cursor] == 5:
            dano_parcial = 40
        elif classe().pp_golpe[pokémon1][cursor] == 10:
            dano_parcial = 35
        elif classe().pp_golpe[pokémon1][cursor] == 15:
            dano_parcial = 30
        elif classe().pp_golpe[pokémon1][cursor] == 20:
            dano_parcial = 25
        elif classe().pp_golpe[pokémon1][cursor] == 25:
            dano_parcial = 20
        dano_parcial *= vantagem(Golpes().tipo_golpe[pokémon1][cursor], pokémon2)
        
    else:
        if classe().pp_golpe[pokémon1][cursor] == 5:
            dano_parcial = 40
        elif classe().pp_golpe[pokémon1][cursor] == 10:
            dano_parcial = 35
        elif classe().pp_golpe[pokémon1][cursor] == 15:
            dano_parcial = 30
        elif classe().pp_golpe[pokémon1][cursor] == 20:
            dano_parcial = 25
        elif classe().pp_golpe[pokémon1][cursor] == 25:
            dano_parcial = 20
        dano_parcial *= vantagem(Golpes().tipo_golpe[pokémon1][cursor], pokémon2)
    
    return int(dano_parcial)

# Função para verificar se o golpe referido pode ser usado, uma vez que o seu pp o limita:
def executa_golpe(player, menospp0, menospp1, menospp2, menospp3, contador):
    if contador == 0 and Golpes().pp_golpe[player][contador] > menospp0 or contador == 1 and Golpes().pp_golpe[player][contador] > menospp1 or contador == 2 and Golpes().pp_golpe[player][contador] > menospp2 or contador == 3 and Golpes().pp_golpe[player][contador] > menospp3:
        return True
    else:
        global barra_texto_novo
        win.blit(barra_texto_novo, (0, 450))
        Texto("There's no PP left for", BRANCO, [30, 480], 25, win)
        Texto("this move!", BRANCO, [30, 520], 25, win)
        pygame.display.update()
        sleep(2.5)
        return False

# Função para exibir uma mensagem de Easter Egg no final do combate
def meme_seletor():
    return random.choice([['E aí carinha que mora logo ali,', 'passa 1 dólar.'], ['Já acabou Jéssica?', ''], ['Eu só queria dar alegria pro meu povo.', ''], ['Marco, temos o seu número de telefone!', 'O número é: (27)4002-8922'], ['Não acho que quem ganhar ou quem perder,', 'vai ganhar ou perder. Vai todo mundo perder'], ['Nada se leva.', 'A não ser a vida levada que a gente leva.'], ['Ao infinito e além!', ''], ['Palmeiras não tem mundial.', ''], ['Aeee Kasinãooo!', ''], ['Desliga o freezer a notche?', ''], ['O IntroBot faz parte da Skynet', 'Cuidado!']])

# Função para randomizar as telas de combate:
def randomizar_telas():
    fundo_randomizer = random.choice(['FundoPokemon.png','FundoPokemon-Caverna.png','FundoPokemon-Grama.png', 'fundo água.png', 'fundo azul-verde.png', 'fundo marrom claro.png', 'fundo roxo claro.png', 'fundo verde.png'])
    return fundo_randomizer

# Definindo o quadro de opções do Pokémon
fgt_options = pygame.image.load(os.path.join('SpritesInterface', 'fgt_options.png')) #carregando a imagem da pasta
fgt_options_novo = pygame.transform.scale(fgt_options,(320,150)) #definindo o tamanho da barra de opções

# Definindo a barra de mensagens
text_bar = pygame.image.load(os.path.join('SpritesInterface', 'text_bar.png'))
text_bar_novo = pygame.transform.scale(text_bar,(800,150))

# Definindo a barra_2
barra_2 = pygame.image.load(os.path.join('SpritesInterface', 'barra_2.png'))
barra_2_novo = pygame.transform.scale(barra_2,(341,140))

# Definindo a barra_1
barra_1 = pygame.image.load(os.path.join('SpritesInterface', 'barra_1.png'))
barra_1_novo = pygame.transform.scale(barra_1,(330,100))

# Barra de mensagens do momento em que o pokémon foge
barra_texto = pygame.image.load(os.path.join('SpritesInterface', 'text_bar.png'))
barra_texto_novo = pygame.transform.scale(barra_texto,(800,150))

# Definindo a barra de vida vazia
barra_sem_vida = pygame.image.load(os.path.join('SpritesInterface', 'barra_sem_vida.png'))

# Definindo a barra de vida amarela
barra_amarela = pygame.image.load(os.path.join('SpritesInterface', 'vida_amarela.png'))

# Definindo a barra de vida vermelha
barra_vermelha = pygame.image.load(os.path.join('SpritesInterface', 'vida_vermelha.png'))

# Definindo o player 1, player 2 e a pokebola (sprites da tela inicial)
sprite_player1 = pygame.image.load(os.path.join('SpritesInterface', 'player1.png'))
sprite_player1_novo = pygame.transform.scale(sprite_player1, (120,200))

sprite_player2 = pygame.image.load(os.path.join('SpritesInterface', 'player2.png'))
sprite_player2_novo = pygame.transform.scale(sprite_player2, (200,200))

pokebola = pygame.image.load(os.path.join('SpritesInterface', 'pokeball.png'))
pokebola_novo = pygame.transform.scale(pokebola, (20,20))

# Dano Máximo = 157
danoNoP1 = 0 # Dano no player 1
danoNoP2 = 0 # Dano no player 2

x1 = 110 # X do pokémon de costas
x2 = 500 # X do pokémon de frente

Xsuperior = 368 # Posição no eixo X da barra de vida superior
Xinferior = 754 # Posição no eixo X da barra de vida inferior

# Definindo o tamanhos das barras de vida (barra_sem_vida, amarela e vermelha) dos players 1 e 2
vida_player1 = pygame.transform.scale(barra_sem_vida, (danoNoP1,10))
barra_amarela1 = pygame.transform.scale(barra_amarela, (80,10))
barra_vermelha1 = pygame.transform.scale(barra_vermelha, (42,10))

vida_player2 = pygame.transform.scale(barra_sem_vida, (danoNoP2,10))
barra_amarela2 = pygame.transform.scale(barra_amarela, (80,10))
barra_vermelha2 = pygame.transform.scale(barra_vermelha, (42,10))

cont = 0 # Definindo um contador como 0 (para fazer a seleção dos pokémons na tela inicial)
cont_enter = 0 # O botão do enter só poderá ser pressionado 2 vezes
cursor = 0 # Cursor para escolher as opções FIGHT, RUN...
cont_golpes = 0 # Para selecionar os golpes
combate = False # A tela de combate se inicia como false
tela_golpes = False # A tela onde são exibidos os golpes também se inicia como false
tela_inicial = True # A tela inicial começa ativada
vez_player1 = True # O player1 começa jogando
escolha_player1 = True # O player 1 também começa escolhendo seu pokémon

# Iniciando a música de abertura
pygame.mixer.music.load(os.path.join('SonsPokemon', 'fireRedAbertura.wav'))
pygame.mixer.music.play()

while True:
    if cont_enter == 0:
        # Definindo o fundo da tela de combate
        fundo = pygame.image.load(os.path.join('SpritesInterface', randomizar_telas()))
        fundo_novo = pygame.transform.scale(fundo,(800,450)) #definindo o tamanho da imagem de fundo

        #Easter egg
        meme_texto = meme_seletor()
        
        player1 = 0  #Pokemon jogador 1
        player2 = 0  #Pokemon jogador 2
    
    #aqui iniciamos nosso game loop

    mouse_pos = pygame.mouse.get_pos() #pega a posição do mouse
    w = Window(800, 600) #cria objeto janela com dimensões 800x600
    win = pygame.display.set_mode(w.returnWinSize()) #inicializa a janela do jogo
    pygame.display.set_caption('Pokémon') #definindo o nome da janela

    if tela_inicial == True:
        
        # Resetando a vida dos pokémons que sofreram ataques
        vida_player1 = pygame.transform.scale(barra_sem_vida, (0,10))
        vida_player2 = pygame.transform.scale(barra_sem_vida, (0,10))
        danoNoP1 = 0
        danoNoP2 = 0

        # Resetando os pps
        
        # Pps do pokémon 1  
        Menos_pp1_0 = 0
        Menos_pp1_1 = 0
        Menos_pp1_2 = 0
        Menos_pp1_3 = 0

        # Pps do pokémon 2  
        Menos_pp2_0 = 0
        Menos_pp2_1 = 0
        Menos_pp2_2 = 0
        Menos_pp2_3 = 0

        # Definindo o "retângulo branco" da tela inicial
        pygame.draw.rect(win, (255,255,255), ((270,100), (250,250)),4)

        win.fill((0, 0, 0)) #definindo a coloração da tela

        # Definindo o "retângulo branco" da tela inicial
        pygame.draw.rect(win, (255,255,255), ((270,100), (250,250)),4)
        Texto('Choose your Pokémon', BRANCO, [230, 50], 20, win)
        Texto('Pikachu', AMARELO, [340, 110], 20, win)
        Texto('Charizard', VERMELHO, [320, 140], 20, win)
        Texto('Venusaur', VERDE, [330, 170], 20, win)
        Texto('Blastoise', AZUL, [320, 200], 20, win)
        Texto('Golem', MARROM_CLARO, [352, 230], 20, win)
        Texto('Gengar', OUTRO_AZUL, [343, 260], 20, win)
        Texto('Dragonite', BRANCO, [320, 290], 20, win)
        Texto('Mewtwo', ROXO, [343, 320], 20, win)

    #selecionando o pokémon de acordo com o valor do cont
    selecionar_Pokemon(cont, win)
    
    # Mostrando na tela os treinadores 1 e 2, respectivamente
    win.blit(sprite_player1_novo, (100, 150))
    win.blit(sprite_player2_novo, (530, 160))

    if escolha_player1: # O Player 1 escolhe seu pokémon
      Texto('Player 1', VERMELHO, [105, 120], 15, win)
      Texto('Player 2', BRANCO, [585, 125], 15, win)
    
    else: # O player 2 escolhe seu pokémon
      win.blit(pokebola_novo, (95, 175)) # player 1
      Texto('Player 1', BRANCO, [105, 120], 15, win)
      Texto('Player 2', VERMELHO, [585, 125], 15, win)

    if cont_enter >= 2: # Se o enter for pressionado seis vezes, muda para a tela de combate
        
        tela_inicial = False # Tela inicial desativada
        
        if tela_golpes == False:
            combate = True # Combate ativado!
        else:
            combate = False 
        
        if vez_player1:
            # Chamando a função que mudará para a tela de combate
            tela_combate(combate, cursor, player1)
        else:
            tela_combate(combate, cursor, player2)

        # Configurando a posição de cada pokémon de costas para que não fique sobreposto a barra de mensagens
        mostrar_pokemon(player1, player2, vez_player1, x1, x2)
    
    for event in pygame.event.get(): # Pega os eventos numa fila de eventos
        
        if event.type == pygame.QUIT: # Caso o "x" da janela seja pressionado
            pygame.quit() # Fechando a janela
        
        if event.type == pygame.KEYDOWN: # Verifica se uma tecla foi pressionada
            sounds = []  # Lista de sons

            # Loop para adicionar um som ao mesmo tempo em que se toca a música de fundo (quando as setas direcionais são pressionadas)
            for i in range(2): 
                sound = pygame.mixer.Sound(os.path.join('SonsPokemon', 'firered_0005.wav')) 
                sound.play() 
                sounds.append(sound)


            # Seleção dos botões "FIGHT", "RUN"...
            if combate == True:
                if event.key == pygame.K_RIGHT: # Seta para a direita
                    if cursor >= 3:
                        cursor = 0
                    else:
                        cursor += 1
                if event.key == pygame.K_LEFT:  # Seta para esquerda
                    if cursor <= 0:
                        cursor = 3
                    else:
                        cursor -= 1
                if event.key == pygame.K_DOWN: # Seta para baixo
                    if cursor == 2 or cursor == 3:
                        cursor -= 2
                    else:
                        cursor += 2 
                if event.key == pygame.K_UP: # Seta para cima
                    if cursor == 0 or cursor == 1:
                        cursor += 2
                    else:
                        cursor -= 2 
                if event.key == pygame.K_RETURN: # Enter
                    if cursor == 0:
                        tela_golpes = True
                        combate = False
                        cursor = 0
                        cont_golpes = 0
                    
                    # Se o pokémon fugir do combate
                    if cursor == 3:
                        tela_inicial = True
                        combate = False
                        cont_enter = 0
                        cont = 0
                        cursor = 0
                        pygame.mixer.music.pause() # Pausando a música de combate

                        # Iniciando a música de fuga 
                        pygame.mixer.music.load(os.path.join('SonsPokemon', 'derrota.wav'))
                        pygame.mixer.music.play()

                        # Animação do pokémon fugindo do combate
                        for s in range(20):
                            pygame.display.update()
                            # Chamando a função que mudará para a tela de combate
                            tela_combate(combate, cursor, player1)
                            # Mostrando a mensagem logo depois do pokémon fugir do combate
                            win.blit(barra_texto_novo, (0, 450))
                            Texto('Got away safely!', BRANCO, [30, 480], 30, win)
                            Texto("Press enter >>>", VERMELHO, [515, 550], 20, win)
                            x1 -= 30
                            mostrar_pokemon(player1, player2, vez_player1, x1, x2)
                        
                        # Loop para esperar o Enter ser pressionado. Se pressionado, volta-se para a tela inicial
                        looping = True
                        while looping:
                            for e in pygame.event.get(): # Capturando os eventos
                                if e.type == pygame.QUIT:
                                    pygame.quit()

                                if e.type == pygame.KEYDOWN:
                                    if e.key == K_RETURN:
                                        looping = False

                        x1 = 110 # Resetando o X do pokémon de costas (o que fugiu) para aparecer na tela de combate com o X certo
                        escolha_player1 = True # O player 1 começa escolhendo
                        
                        # Iniciando a música de abertura
                        pygame.mixer.music.load(os.path.join('SonsPokemon', 'fireRedAbertura.wav'))
                        pygame.mixer.music.play()

                    continue # Voltando para a tela inicial
            
            # Seleção dos pokémons na tela inicial
            else:
                if event.key == pygame.K_DOWN: #se a seta para BAIXO for pressionada
                    cont += 1
                    if cont == 8: # Se chegar na última opção e pressionar para baixo, a seleção volta para a primeira opção
                        cont = 0
                            
                if event.key == pygame.K_UP: # Se a seta para CIMA for pressionada
                    cont -= 1
                    if cont == -1: # Se chegar na primeira opção e pressionar para cima, a seleção vai para a última opção
                        cont = 7
                    
                if event.key == pygame.K_RETURN: # Se o enter for pressionado
                    cont_enter += 1
                    if cont_enter < 2:
                        player1 = cont # Atribuindo a uma variável o pokémon escolhido pelo player 1
                    elif 2 <= cont_enter < 3:
                        player2 = cont # Atribuindo a uma variável o pokémon escolhido pelo player 2
                        win.blit(pokebola_novo, (582, 167)) # player 2
                        
                        pygame.mixer.music.pause() # Parando a música de abertura
                        pygame.mixer.music.load(os.path.join('SonsPokemon', 'batalha.wav'))
                        pygame.mixer.music.play() # Iniciando a música de batalha
                    
                    escolha_player1 = False

        # Chamando a função que exibirá o quadro de ataques dos pokémons
        if tela_golpes == True:
            fundo_fight() # Mostrando o fundo do menu "FIGHT" 
            nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes
            selecionador_golpes(cont_golpes, win) # Função para selecionar os ataques
            
            # Mudando o valor de cont_golpe, a fim de mudar a seleção dos ataques
            if event.type == pygame.KEYDOWN: # Verifica se uma tecla foi pressionada
                # Seleção do golpe
                if event.key == pygame.K_RIGHT: # Seta para a direita
                    if cont_golpes >= 3:
                        cont_golpes = 0
                    else:
                        cont_golpes += 1
                if event.key == pygame.K_LEFT: # Seta para wsquerda
                    if cont_golpes <= 0:
                        cont_golpes = 3
                    else:
                        cont_golpes -= 1
                if event.key == pygame.K_DOWN: # Seta para baixo
                    if cont_golpes == 2 or cont_golpes == 3:
                        cont_golpes -= 2
                    else:
                        cont_golpes += 2 
                if event.key == pygame.K_UP: # Seta para cima
                    if cont_golpes == 0 or cont_golpes == 1:
                        cont_golpes += 2
                    else:
                        cont_golpes -= 2
                
                if event.key == pygame.K_ESCAPE: # Esc
                    tela_golpes = False # Voltando para a tela de seleção dos menús FIGHT, RUN...
                    
                if event.key == pygame.K_RETURN: # Enter (Se algum golpe for deferido)

                    # Diminuindo o valor do pp do player 1
                    if vez_player1 and executa_golpe(player1, Menos_pp1_0, Menos_pp1_1, Menos_pp1_2, Menos_pp1_3, cont_golpes):
                        if cont_golpes == 0:
                            Menos_pp1_0 += 1
                        if cont_golpes == 1:
                            Menos_pp1_1 += 1
                        if cont_golpes == 2:
                            Menos_pp1_2 += 1
                        if cont_golpes == 3:
                            Menos_pp1_3 += 1
                        golpep1 = cont_golpes
                        vez_player1 = False

                    # Diminuindo o valor do pp do player 2
                    elif vez_player1 == False and executa_golpe(player2, Menos_pp2_0, Menos_pp2_1, Menos_pp2_2, Menos_pp2_3, cont_golpes):
                        if cont_golpes == 0:
                            Menos_pp2_0 += 1
                        if cont_golpes == 1:
                            Menos_pp2_1 += 1
                        if cont_golpes == 2:
                            Menos_pp2_2 += 1
                        if cont_golpes == 3:
                            Menos_pp2_3 += 1
                        golpep2 = cont_golpes

                        for c in range(2):
                            if c == 0:
                                dano_player1 = dano_golpe(player1, player2, golpep1, True)
                                dano_player2 = dano_golpe(player2, player1, golpep2, False)
                                
                                if Golpes().hp[player1][1] >= Golpes().hp[player2][1]:
                                    vez_player1 = True
                                    cont_golpes = golpep1
                                else:
                                    vez_player1 = False
                                    cont_golpes = golpep2
                            elif c == 1:
                                if Golpes().hp[player1][1] >= Golpes().hp[player2][1]:
                                    vez_player1 = False
                                    cont_golpes = golpep2
                                else:
                                    vez_player1 = True
                                    cont_golpes = golpep1
                            
                            pygame.display.update()
                            #chamando a função que mudará para a tela de combate
                            tela_combate(combate, cursor, player1)
                            fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                            nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes

                            # Movendo o pokémon que ataca (de costas)
                            x1 += 30
                            mostrar_pokemon(player1, player2, vez_player1, x1, x2)
                            sleep(0.5)

                            pygame.display.update()
                            #chamando a função que mudará para a tela de combate
                            tela_combate(combate, cursor, player1)
                            fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                            nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes

                            x1 = 110
                            mostrar_pokemon(player1, player2, vez_player1, x1, x2)
                            sleep(0.1) # "velocidade do golpe"

                            pygame.display.update()
                            #chamando a função que mudará para a tela de combate
                            tela_combate(combate, cursor, player2)
                            fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                            nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes
                            sleep(0.2)

                            # Movendo o pokémon que sofre dano (de frente)
                            x2 += 30
                            mostrar_pokemon(player1, player2, vez_player1, x1, x2)
                            pygame.display.update()

                            mostrar_pokemon(player1, player2, vez_player1, x1, x2, True)
                            pygame.display.update()

                            #chamando a função que mudará para a tela de combate
                            tela_combate(combate, cursor, player1)
                            fundo_fight() # Mostrando o fundo do menu "FIGHT" 
                            nome_golpes(player1, player2, vez_player1, cont_golpes) # Mostrando as opções de golpes

                            sleep(0.2)
                            x2 = 500
                            mostrar_pokemon(player1, player2, vez_player1, x1, x2)
                            sleep(0.25)

                            vez_player1 = True # Para a próxima jogada ser do player 1

                            if danoNoP1 == 157 or danoNoP2 == 157:
                                pygame.mixer.music.pause() # Parando a música de batalha
                                break

                    tela_golpes = False

        if danoNoP1 == 157 or danoNoP2 == 157:
            pygame.mixer.music.pause() # Pausando alguma música que ainda possa estar tocando
            pygame.mixer.music.load(os.path.join('SonsPokemon', 'vitoria.wav'))
            pygame.mixer.music.play() # Iniciando a música de vitória
            looping = True

            #Easter Egg
            meme = parte2 = parte3 = parte4 = False

            # Tela de fim
            while looping:
                tela_inicial = True
                combate = False
                cont_enter = 0
                cont = 0
                cursor = 0
                escolha_player1 = True # O player 1 começa escolhendo
                
                # Exibindo a mensagem no final do combate
                if danoNoP2 == 157 and meme == False:
                    win.blit(barra_texto_novo, (0, 450))
                    Texto("Red defeated", BRANCO, [30, 480], 30, win)
                    Texto("Rival Gary!", BRANCO, [30, 520], 30, win)

                elif danoNoP1 == 157 and meme == False:
                    win.blit(barra_texto_novo, (0, 450))
                    Texto("Gary defeated", BRANCO, [30, 480], 30, win)
                    Texto("Rival Red!", BRANCO, [30, 520], 30, win)
                
                elif meme == True:
                    win.blit(barra_texto_novo, (0, 450))
                    if parte2:
                        Texto('Ops... O "easter egg" já acabou', BRANCO, [30, 480], 20, win)
                        Texto('Pode clicar enter :)', BRANCO, [30, 520], 20, win)
                    elif parte3:
                        Texto('Sério, não há easter eggs...', BRANCO, [30, 480], 20, win)
                        Texto('Então seja uma boa pessoa', BRANCO, [30, 515], 20, win)
                        Texto('E clique no enter →', BRANCO, [50, 550], 20, win)
                    elif parte4:
                        Texto('Certo, já que você quer tanto um ovo de páscoa', BRANCO, [30, 480], 16, win)
                        Texto('Clique no enter, que irei rodar um código aleatório...', BRANCO, [30, 520], 16, win)

                    else:
                        Texto(meme_texto[0], BRANCO, [30, 480], 20, win)
                        Texto(meme_texto[1], BRANCO, [30, 520], 20, win)
                Texto("Press enter >>>", VERMELHO, [515, 550], 20, win)
                    
                
                for e in pygame.event.get(): # Capturando os eventos
                    if e.type == pygame.QUIT:
                        pygame.quit()

                    if e.type == pygame.KEYDOWN:
                        if e.key == K_RETURN:
                            if parte4 == True:
                                pygame.mixer.music.pause()
                                jogo()
                            looping = False
                        
                        # Se o "espaço" for pressionado, aparece uma mensagem diferente (Easter Egg)
                        if e.key == pygame.K_SPACE:
                            if meme == False:
                                meme = True
                            elif parte2 == False and parte3 == False and parte4 == False and meme:
                                parte2 = True
                            elif parte2 and parte3 == False and parte4 == False:
                                parte2 = False
                                parte3 = True
                            elif parte2 == False and parte3 and parte4 == False: 
                                parte3 = False
                                parte4 = True

                pygame.display.update()

            # Iniciando a música de abertura logo antes de voltar para a tela inicial
            pygame.mixer.music.load(os.path.join('SonsPokemon', 'fireRedAbertura.wav'))
            pygame.mixer.music.play() 
            
        #Atualiza a tela
        pygame.display.update()