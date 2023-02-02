import random

def markov_generate_sentences(dict_words: dict[str : list[str]],dict_frases: dict[str: int] ,num_frases: int):
    frases_hechas={}
    frase = list()
    state = "START", "START" # ESTO TENDRIA QUE CAMBIAR
    count = 1
    attemps = 0
    while count < num_frases+1 and attemps < 300 :
        word = random.choice(dict_words[state])
        frase.append(word)
        state = state[1], word

        if not state in dict_words:
            frase_complete=" ".join(frase)
            if (not frase_complete in dict_frases) and (not frase_complete in frases_hechas):
                print(f"{count}- "+ frase_complete,'\n')
                frases_hechas[frase_complete]=count
                frase.clear()
                state="START","START"   # ESTO TENDRIA QUE CAMBIAR
                count += 1
            else : 
                frase.clear()
                state = "START","START"  # ESTO TENDRIA QUE CAMBIAR
                attemps +=1

def introducir_clave_valor(anteriores: tuple, siguiente: str, dict_words: dict[str : list[str]]) -> dict[str : list[str]]:
    if anteriores in dict_words:
        dict_words[anteriores].append(siguiente)
    else:
        dict_words[anteriores] = [siguiente]
    return dict_words

def eliminar_signos(line: str):
    separators = [",", ";", ":", ".", "-","?","!","/","\\","[","]","{","}",'\n']
    for sep in separators:
        line= line.replace(sep, " ")
    return line.lower()

def state_generator(num_de_estados:int=2)-> tuple: 
    state = ["START" for i in range(num_de_estados)]
    return tuple(state)
def update_state (state:list[str],word:str):
    state=state[1:]
    state = state + (word,)
    return state

def create_dict(file:list[str],state_generated:tuple)-> dict[str : list[str]]:
    state= state_generated
    dict_words:dict[str : list[str]] = {}
    dict_frases:dict[str : int] = {}
    for j,line in enumerate (file) :
        sentece:str = eliminar_signos(line)
        dict_frases[sentece.strip()]=j   # generando diccionario de frases
        list_words:list[str] = sentece.rsplit()
        for word in list_words:
            dict_words = introducir_clave_valor(state,word,dict_words) 
            state= update_state(state,word)
        state = state_generated
    return dict_words,dict_frases      # DEVUELVE EL DICCIONARIO DE ESTADOS  CON LA LISTA DE PALABRAS Y ****UN DICCIONARIO CON LAS FRASES

def read_file(ruta: str) -> list[str]:
    try:
        file:object= open(rf"{ruta}", "r")
    except:
        print("Upps!!, ha habido un problema")
    else:
        lines = file.readlines()
        file.close()
        return lines

if __name__ == "__main__":
    #1 - Pedir numero de frases:
    numero_de_veces:int = int(input("Cuantas frases quieres: "))
    print() 
    #1.1 - Pedir estados:
    numero_de_estados: int = int(input("Cuantos estados desea analizar: "))
    print()

    #Generar estado:
    state_generated = state_generator(numero_de_estados)

    #3 - Leer archivo
    file = read_file(r"/home/marcos/Downloads/prueba.txt")

    #4 - Genero diccionario con las frases de mi archivo y otro diccionario con los {stados:[words]}
    dict_words,dict_frases = create_dict(file,state_generated)
    
    #5 - Genero cadenas
    markov_generate_sentences(dict_words, dict_frases, numero_de_veces)
    