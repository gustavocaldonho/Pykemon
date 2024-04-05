class Player:
    """
    Propriedades:
        lista_pokemons, pngFrente, pngCostas: listas
    """
    def __init__(self): # Construtor
        
        self.__lista_pokemons = ['Pikachu', 'Charizard', 'Venusaur', 'Blastoise', 'Golem', 'Gengar', 'Dragonite', 'Mewtwo']

        self.__pngFrente = ['pikachufren.png', 'charizardfren.png', 'venusaurfren.png', 'blastoisefren.png', 'golemfren.png', 'gengarfren.png', 'dragonitefren.png', 'mewtwofren.png', 'pikachufrensh.png', 'charizardfrensh.png', 'venusaurfrensh.png', 'blastoisefrensh.png', 'golemfrensh.png', 'gengarfrensh.png', 'dragonitefrensh.png', 'mewtwofrensh.png']
        
        self.__pngCostas = ['pikachucost.png', 'charizardcost.png', 'venusaurcost.png', 'blastoisecost.png', 'golemcost.png', 'gengarcost.png', 'dragonitecost.png', 'mewtwocost.png', 'pikachucostsh.png', 'charizardcostsh.png', 'venusaurcostsh.png', 'blastoisecostsh.png', 'golemcostsh.png', 'gengarcostsh.png', 'dragonitecostsh.png', 'mewtwocostsh.png']

    @property
    def pokemon_information(self):
      return [self.__pngFrente, self.__pngCostas, self.__lista_pokemons]