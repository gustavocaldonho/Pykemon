import pygame
from random import randrange
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cinza = (79, 79, 79)
prata = (192, 192, 192)
pygame.init()
largura = 800
altura = 600
placar = 40
fundo = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
tamanho = 20
pygame.display.set_caption('Pykemon')

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(snake):
    for xy in snake:
        pygame.draw.rect(fundo, red, [xy[0], xy[1], tamanho, tamanho], 0)

def apple(apple_x, apple_y):
    pygame.draw.rect(fundo, white, [apple_x, apple_y, tamanho, tamanho], 0)

def jogo():
    pos_x = randrange(0, 390, tamanho) #640/480
    pos_y = randrange(0, 290, tamanho)
    apple_x = randrange(0, 390, tamanho)
    apple_y = randrange(0, 290, tamanho)
    velocidade_x = 0
    velocidade_y = 0
    if apple_x == pos_x and apple_y == pos_y and velocidade_x == 0 and velocidade_y == 0:
        apple_x = randrange(0, 390, tamanho)
        apple_y = randrange(0, 290, tamanho)
    
    contagem = 10

    cobrapos = []
    cobracomp = 4

    pontos = 0

    sair = True
    fimdejogo = False
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pos_x = randrange(0, 310, tamanho)
                        pos_y = randrange(0, 230, tamanho)
                        apple_x = randrange(0, 310, tamanho)
                        apple_y = randrange(0, 230, tamanho)
                        velocidade_x = 0
                        velocidade_y = 0
                        if apple_x == pos_x and apple_y == pos_y and velocidade_x == 0 and velocidade_y == 0:
                            apple_x = randrange(0, 310, tamanho)
                            apple_y = randrange(0, 230, tamanho)

                        contagem = 10

                        cobrapos = []
                        cobracomp = 4

                        pontos = 0

                        sair = True
                        fimdejogo = False
                    elif event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    #pygame.draw.rect(fundo, white, [145, 170, 365, 47])
                    if x > 145 and y > 170 and x < (145 + 365) and y < (170 + 47):
                        pos_x = randrange(0, 310, tamanho)
                        pos_y = randrange(0, 230, tamanho)
                        apple_x = randrange(0, 310, tamanho)
                        apple_y = randrange(0, 230, tamanho)
                        velocidade_x = 0
                        velocidade_y = 0
                        if apple_x == pos_x and apple_y == pos_y and velocidade_x == 0 and velocidade_y == 0:
                            apple_x = randrange(0, 310, tamanho)
                            apple_y = randrange(0, 230, tamanho)

                        contagem = 10

                        cobrapos = []
                        cobracomp = 4

                        pontos = 0

                        sair = True
                        fimdejogo = False
                    
                    #pygame.draw.rect(fundo, white, [195, 270, 275, 54])
                    elif x > 195 and y > 270 and x < (195 + 275) and y < (290 + 54):
                        sair = False
                        fimdejogo = False

            fundo.fill(black)
            texto('Fim de jogo!', cinza, 80, 159, 29)
            texto('Fim de jogo!', white, 80, 160, 30)
            texto(f'Pontuação Final: {pontos}', cinza, 50, 169, 99)
            texto(f'Pontuação Final: {pontos}', red, 50, 170, 100)
            pygame.draw.rect(fundo, prata, [143, 168, 363, 45])
            pygame.draw.rect(fundo, white, [145, 170, 365, 47])
            texto('Reiniciar(R)', black, 70, 190, 173)
            pygame.draw.rect(fundo, prata, [193, 268, 273, 52])
            pygame.draw.rect(fundo, white, [195, 270, 275, 54])
            texto('Sair(S)', black, 70, 260, 273)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sair = False
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                elif event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                elif event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
                elif event.key == pygame.K_1:
                    cobracomp += 1
                elif event.key == pygame.K_2:
                    fimdejogo = True
        if sair:
            fundo.fill(black)
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x > 780:
                pos_x = 0
            if pos_x < 0:
                pos_x = 780
            if pos_y > (580 - placar):
                pos_y = 0
            if pos_y < 0:
                pos_y = (580 - placar)   #Sair = False em todos caso eu queira morte nas bordas

            if pos_x == apple_x and pos_y == apple_y:
                apple_x = randrange(0, 310, tamanho)
                apple_y = randrange(0, 230, tamanho)
                cobracomp += 1
                pontos += 1
                contagem += 0.2

            cobrahead = []
            cobrahead.append(pos_x)
            cobrahead.append(pos_y)
            cobrapos.append(cobrahead)
            if len(cobrapos) > cobracomp:
                del cobrapos[0]

            if len(cobrapos) > 4:
                if cobrapos.count(cobrapos[-1]) > 1:
                    fimdejogo = True


            pygame.draw.rect(fundo, blue, [0, altura-40, largura, 40], 0)
            texto(f'Pontuação: {pontos}', white, 40, 10, altura-30)
            cobra(cobrapos)
            apple(apple_x, apple_y)
            pygame.display.update()
            relogio.tick(contagem)