import random 

def comeco():
    print('\n',('-'*30), "JOGO POKEMON",('-'*30))
    print(f"\nBem-vindo ao mundo de Pokémon!\n")
    print(f"\nMeu nome é Professor Carvalho.\n")
    print(f"\nEu vou ajudar-lo em sua jornada.\n")
    print(f"\nNesse mundo a sua tarefa é capturar todos os Pokemons.")
    
def OqueFazer():
    print("\nO que deseja fazer?\n\n1- Entrar na floresta\n2- Entrar na caverna\n3- Ver Pokedex\n4- Sair do Jogo")

def sorteioPokemonEncontrado(pokemon):
    pokemon_sorteado = random.randint(0,len(pokemon)-1)
    return pokemon[pokemon_sorteado]

def SorteioPokemon(pokemon):
    pokemon_sorteado = random.randint(0,len(pokemon)-1)
    return pokemon[pokemon_sorteado]

def CapturaFloresta():
    tentativa = random.randint(0,99)
    if 0<=tentativa>=49: 
        return 1
    else:
        return 2

def CapturaCaverna():
    tentativa = random.randint(0,99)
    if 0<=tentativa>=36: 
        return 1
    else: 
        return 2

pokedex = []
pokemonsFloresta = ['Pikachu', 'Ratata', 'Blastoide']
pokemonsCaverna = ['Bulbassaur', 'Ekans', 'Charizard']
pokebolas = 10
comeco()
nome = input("\n\nQual o seu nome?\n-> ")

while True:
    if len(pokedex) == 7:
        print('\n',('-'*30), "FIM DE JOGO",('-'*30))
        print(f"\nParabéns você capturou todos os pokémons!\n\n" + f"\nPokedéx: {pokedex}")
        break

    if pokebolas == 0:
        print("\nGAME OVER\n")
        print("\nSuas tentativas acabaram...\n")
        break

    print("\nO que deseja fazer?\n\n1- Entrar na floresta\n2- Entrar na caverna\n3- Ver Pokedéx\n4- Sair do Jogo")
    resposta = int(input("\n- "))

    if resposta == 1:  
        print('\n',('-'*30), "Você escolheu entrar na Floresta",('-'*30))

        while True:

            PokemonFloresta = SorteioPokemon(pokemonsFloresta)
            print(f"\nVocê encontrou o pokémon: {PokemonFloresta}\n")            

            if PokemonFloresta in pokedex:
                print("\nVocê já possui esse pokemon...")
                break

            opcaoCapturar = int(input("\nDeseja tentar capturá-lo?\n1- Sim\n2- Não\n\n-> "))
            captura = CapturaFloresta()
            if captura == 1:
                    print(f"\nPókemon {PokemonFloresta} Capturado\n")
                    pokedex.append(PokemonFloresta)
                    break
            elif captura == 2:
                    print(f"\nPókemon {PokemonFloresta} não capturado, tente novamente...")
                    pokebolas -= 1
                    print(f"\nPokebolas restantes: {pokebolas}")
                    break

    
            elif opcao_capturar == 2:
                print("\nSaindo da Floresta...")
                break
            else:
                print("\nErro, insira uma opção válida\n")
                continue

    elif resposta == 2:
        print('\n',('-'*30), " Você escolheu entrar na Caverna",('-'*30))

        while True:
             
            pokemonEncontradoCaverna = sorteioPokemonEncontrado(pokemonsCaverna)
            print(f"\nVocê encontrou o: {pokemonEncontradoCaverna}\n")
            
            if pokemonEncontradoCaverna in pokedex:
                print("\nVocê já possui esse pókemon...")
                break

            opcao_capturar = int(input("\nDeseja tentar capturá-lo?\n1- Sim\n2- Não\n\n-> "))
            if opcao_capturar == 1:
          
                captura = CapturaCaverna()
                if captura == 1:
                    print(f"\nPókemon {pokemonEncontradoCaverna} capturado\n")
                    pokedex.append(pokemonEncontradoCaverna)
                    break
                elif captura == 2:
                    print(f"\nPókemon {pokemonEncontradoCaverna} não capturado, tente novamente...")
                    pokebolas -= 1
                    print(f"\nPokebolas restantes: {pokebolas}")
                    break

            elif opcao_capturar == 2:
                print("\nSaindo da Caverna...")
                break

            else:
                print("\nErro, insira uma opção válida\n")
                continue     
    elif resposta == 3:
     print(f"Pokedéx: {pokedex}")
     continue
    elif resposta == 4:
        print("\n\nAté a Próxima!\n")
        break

    else:
        print("\nErro, Insira uma opção válida...")
        continue