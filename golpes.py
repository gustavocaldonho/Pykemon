from random import randint

class Golpes:
  """
  Propriedades:
    lista_stats, nome, pp, tipo : listas
  """

  def __init__(self):
    # HP / VELOCIDADE
    self.__lista_stats = [[274, 306], [360, 328], [364, 284], [362, 280], [364, 207], [324, 350], [386, 285], [416, 394]]

    self.__nome = [['Thunder', 'Slam', 'Thunderbolt', 'Iron Tail'], ['Flamethrower', 'Air Slash', 'Dragon Claw', 'Fire Blast'], ['Solar Beam', 'Earthquake', 'Sludge Bomb', 'X-Scissor'], ['Hydro Pump', 'Surf', 'Skull Bash', 'Ice Beam'], ['Double Edge', 'Earthquake', 'Rock Throw', 'Brick Break'], ['Sludge Bomb', 'Psychic', 'Shadow Ball', 'Dark Pulse'], ['Flamethrower', 'Ice Beam', 'Dragon Claw', 'Wing Attack'], ['Shadow Ball', 'Psystrike', 'Swift', 'Earthquake']]

    self.__pp = [[10, 20, 15, 15], [15, 15, 15, 5], [5, 10, 10, 25], [5, 15, 10, 10], [15, 10, 15, 15], [10, 10, 15, 15], [10, 10, 15, 25], [15, 10, 20, 10]]
    
    self.__tipo = [['Electric', 'Normal', 'Electric', 'Steel'], ['Fire', 'Flying', 'Dragon', 'Fire'], ['Grass', 'Ground', 'Poison', 'Bug'], ['Water', 'Water', 'Normal', 'Ice'], ['Normal', 'Ground', 'Rock', 'Fight'], ['Poison', 'Psychic', 'Ghost', 'Dark'], ['Fire', 'Ice', 'Dragon', 'Flying'], ['Ghost', 'Psychic', 'Normal', 'Ground']]

  @property 
  def nome_golpe(self):  
    return self.__nome

  @property
  def dano_golpe(self, indice):
    self.__chance = randint(1, 100)
    return self.__dano[indice] * 2 if self.__chance > 80 else self.___dano[indice]

  @property
  def pp_golpe(self):
    return self.__pp

  @property
  def tipo_golpe(self):
    return self.__tipo

  @property
  def hp(self):
    return self.__lista_stats

def vantagem(tipo_golpe, valor_pokemon):
  multiplicador = 1

  if valor_pokemon == 0:
    if tipo_golpe == "Ground":
      multiplicador = 2
    
    elif tipo_golpe == "Electric" or tipo_golpe == "Flying" or tipo_golpe == "Steel":
      multiplicador = 0.5

  
  elif valor_pokemon == 1:

    if tipo_golpe == "Rock":
      multiplicador = 4

    elif tipo_golpe == "Water" or tipo_golpe == "Electric":
      multiplicador = 2

    elif tipo_golpe == "Steel" or tipo_golpe == "Fire" or tipo_golpe == "Fight":
      multiplicador = 0.5
    
    elif tipo_golpe == "Bug" or tipo_golpe == "Grass":
      multiplicador = 0.25

    elif tipo_golpe == "Ground":
      multiplicador = 0
  
  elif valor_pokemon == 2:

    if tipo_golpe == "Fire" or tipo_golpe == "Ice" or tipo_golpe == "Flying" or tipo_golpe == "Psychic":
      multiplicador = 2
  
    elif tipo_golpe == "Water" or tipo_golpe == "Electric" or tipo_golpe == "Fight":
      multiplicador = 0.5
    
    elif tipo_golpe == "Grass":
      multiplicador = 0.25
  
  
  elif valor_pokemon == 3:
    if tipo_golpe == "Electric" or tipo_golpe == "Grass":
      multiplicador = 2
      
    elif tipo_golpe == "Fire" or tipo_golpe == "Water" or tipo_golpe == "Ice" or tipo_golpe == "Steel":
      multiplicador = 0.5
  

  elif valor_pokemon == 4:
    if tipo_golpe == "Water" or tipo_golpe == "Grass":
      multiplicador = 4

    elif tipo_golpe == "Fight" or tipo_golpe == "Ground" or tipo_golpe == "Steel" or tipo_golpe == "Ice":
      multiplicador = 2

    elif tipo_golpe == "Normal" or tipo_golpe == "Flying" or tipo_golpe == "Rock" or tipo_golpe == "Fire":
      multiplicador = 0.5
    
    elif tipo_golpe == "Poison":
      multiplicador = 0.25
    
    elif tipo_golpe == "Electric":
      multiplicador = 0
    
    
  elif valor_pokemon == 5:
  #GENGAR(Fantasma/Veneno):
    #Resistencias(1/2): Grama , Veneno(1/4!) , Inseto(1/4!)
    #Fraquezas(2x): Terra , Fantasma , Pisíquico , Sombrio .
    #Imunidade: Normal , Lutador .
    if tipo_golpe == "Ground" or tipo_golpe == "Ghost" or tipo_golpe == "Psychic" or tipo_golpe == "Dark":
      multiplicador = 2
    
    elif tipo_golpe == "Grass":
      multiplicador = 0.5

    elif tipo_golpe == "Poison" or tipo_golpe == "Bug":
      multiplicador = 0.25  

    elif tipo_golpe == "Normal" or tipo_golpe == "Fight":
      multiplicador = 0  
  
  
  elif valor_pokemon == 6:
  #:DRAGONITE(Dragao/Voador):
    #Resistencias(1/2): Lutador , Inseto , Fogo , Agua , Grama(1/4!)
    #Fraquezas(2x): Pedra , Dragao , Gelo(4x!)
    #Imunidade: Terra
    if tipo_golpe == "Ice":
      multiplicador = 4
    
    elif tipo_golpe == "Rock" or tipo_golpe == "Dragon":
      multiplicador = 2
    
    elif tipo_golpe == "Fight" or tipo_golpe == "Bug" or tipo_golpe == "Fire" or tipo_golpe == "Water":
      multiplicador = 0.5

    elif tipo_golpe == "Grass":
      multiplicador = 0.25

    elif tipo_golpe == "Ground":
      multiplicador = 0   
  
  
  elif valor_pokemon == 7:
     #:MEWTWO(Pisíquico):
    #Resistencias(1/2): Lutador , Pisciquico
    #Fraquezas(2x): Inseto, Fantasma , Dark(ou sombrio).
    if tipo_golpe == "Bug" or tipo_golpe == "Ghost" or tipo_golpe == "Dark":
      multiplicador = 2    
    
    elif tipo_golpe == "Fight" or tipo_golpe == "Psychic":
      multiplicador = 0.5


  return multiplicador 
  
    
    



 #      NAME         ||PODER ||PRECISAO||  PP  || TIPO
    #==PIKACHU==
    #s)   Thunder    || 110  ||  70%   ||  10  || Electro
    #f)     Slam     ||  80  ||  75%   ||  20  || Normal
    #s) Thunderbolt  ||  90  ||  100%  ||  15  || Electro
    #f)  Iron Tail   || 100  ||  75%   ||  15  || Aço
    #==CHARIZARD==
    #s)  Flametrower ||  90  ||  100%  ||  15  || Fogo
    #f)  Air Slash   ||  75  ||  95%   ||  15  || Ar
    #f)  Dragon Claw ||  80  ||  100%  ||  15  || Dragao
    #s)  Fire Blast  || 110  ||  85%   ||  5   || Fogo
    #==VENUSAUR==
    #s)  Energy Ball ||  90  ||  100%  ||  10  || Grama
    #f)  Earthquake  || 100  ||  100%  ||  10  || Terra
    #f)  Razor Leaf  ||  55  ||  95%   ||  25  || Grama
    #s)  Sludge Bomb ||  90  ||  100%  ||  10  || Veneno
    #==BLASTOISE==
    #s)  Hydro Pump  || 110  ||  80%   ||  5   || Agua
    #s)  Surf        ||  90  ||  100%  ||  15  || Agua
    #f)  Skull Bash  || 130  ||  100%  ||  10  || Normal
    #s)  Ice Beam    ||  90  ||  100%  ||  10  || Gelo
    #==GOLEM==
    #f)  Double Edge || 120  ||  100%  ||  15  || Normal
    #f)  Earthquake  || 100  ||  100%  ||  10  || Terra
    #f)  Rock Trow   ||  50  ||  90%   ||  15  || Pedra
    #f)  Brick Break ||  75  ||  100%  ||  15  || Lutador
    #==GENGAR==
    #s)  Sludge Bomb ||  90  ||  100%  ||  10  || Veneno
    #s)   Psychic    ||  90  ||  100%  ||  10  || pisychic
    #s)  Shadow Ball ||  80  ||  100%  ||  15  || Ghost
    #s)  Dark Pulse  ||  80  ||  100%  ||  15  || Dark
    #==DRAGONITE==  
    #s) Flamethrower ||  90  ||  100%  ||  15  || Fogo
    #s)  Ice Beam    ||  90  ||  100%  ||  10  || Gelo
    #f)  Dragon Claw ||  80  ||  100%  ||  15  || Dragao
    #f)  Wing Atack  ||  60  ||  100%  ||  35  || Voador
    #==MEWTWO==
    #s)  Shadow Ball ||  80  ||  100%  ||  15  || Fantasma
    #s)  Psystrike   || 100  ||  100%  ||  10  || pisychic 
    #s)  Swift       ||  60  ||  ---%  ||  20  || Normal
    #f)  Earthquake  || 100  ||  100%  ||  10  || Terra

    #==GLOSSÁRIO==   
    # f) = Físico
    # s) = Especial
    #---% = Sempre acerta!

    #==COISAS A SABER==
    #Thunder - 30% chance de paralisia(adversario)
    #Thunderbolt - 10% chance de paralisia(adversario)
    #Iron Tail - 30% chance de reduzir Defesa(adversario)
    #Flamethrower - 10% chance de queimar(adversario)
    #Air Slash - 30% chance de stunar[ou finch](adversario)
    #Fire Blast - 10% chance de queimar(adversario)
    #Energy Ball - 10% chance de reduzir S.Defesa
    #Sludge Bomb - 30% chance de envenenar(adversario)
    #Skull Bash - ataca sempre depois
    #Ice Beam - 10% de congelar(adversario)
    #Double Edge - Toma dano (1/3 ou 1/4 do dano causado)
    #Psychic - 10% chance de reduzir S.Defesa(adversario)
    #Shadow Ball - 20% de reduzir S.Defesa(adversario)
    #Dark Pulse - 20% chance de stunar[ou finch](adversario)
    #Psystrike - mesmo sendo Special,dá dando de acordo com a Defesa inimiga

  #====== VANTAGENS E DESVANTAGENS DE CADA POKEMON ======
    #PIKACHU(Elétrico):
    
    #:CHARIZARD(Fogo/Voador): 
    #Resistencias(1/2): Lutador , Inseto , Aço , Fogo , Grama , Fada .
    #Fraquezas(2x): Agua , Elétrico , Pedra(4x!) .
    #Imunidade: Terra .

    #:VENUSAUR(Grama/Veneno):
    #Resistencias(1/2): Lutador , Agua , Grama , Elétrico , Fada .
    #Fraquezas(2x): Fogo , Voador , Pisiquico , Gelo

    #:BLASTOISE(Agua):
    #Resistencias(1/2): Ferro , Fogo , Agua , Gelo .
    #Fraquezas(2x): Grama , Elétrico . 

    #GOLEM(Pedra,Terra):
    #Resistencias(1/2): Normal , Voador , Pedra , Fogo , Veneno(1/4!)
    #Fraquezas(2x): Lutador , Terra , Aço , Gelo , Agua(4x!), Grama(4x!) .
    #Imunidade: Elétrico .

    #GENGAR(Fantasma/Veneno):
    #Resistencias(1/2): Grama , Veneno(1/4!) , Inseto(1/4!)
    #Fraquezas(2x): Terra , Fantasma , Pisíquico , Sombrio .
    #Imunidade: Normal , Lutador . 

    #:DRAGONITE(Dragao/Voador):
    #Resistencias(1/2): Lutador , Inseto , Fogo , Agua , Grama(1/4!)
    #Fraquezas(2x): Pedra , Dragao , Fada , Gelo(4x!)
    #Imunidade: Terra

    #:MEWTWO(Pisíquico):
    #Resistencias(1/2): Lutador , Pisciquico
    #Fraquezas(2x): Inseto, Fantasma , Dark(ou sombrio).