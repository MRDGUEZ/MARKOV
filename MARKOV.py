import random
#hola
def markov_generate_sentences(dict_words: dict[tuple : list[str]],dict_sentences: dict[str: int] ,number_of_sentences: int,generated_state:tuple)->None:
    phrases_made={}
    phrase = list()
    state = generated_state
    count = 1
    attempts = 0
    while count < number_of_sentences+1 and attempts < 300 :
        word = random.choice(dict_words[state])
        phrase.append(word)
        state = update_state(state,word)

        if not state in dict_words:
            phrase_complete=" ".join(phrase)
            if (not phrase_complete in dict_sentences) and (not phrase_complete in phrases_made):
                print(f"{count}- "+ phrase_complete,'\n')
                phrases_made[phrase_complete]=count
                phrase.clear()
                state=generated_state
                count += 1
            else : 
                phrase.clear()
                state = generated_state
                attempts +=1

def enter_values_into_dict(state: tuple, word: str, dict_words: dict[tuple : list[str]]) -> dict[tuple: list[str]]:
    if state in dict_words:
        dict_words[state].append(word)
    else:
        dict_words[state] = [word]
    return dict_words

def remove_signs(line: str)->str:
    separators = [",", ";", ":", ".", "-","?","!","/","\\","[","]","{","}",'\n']
    for sep in separators:
        line= line.replace(sep, "")
    return line.lower()

def state_generator(num_de_estados:int=2)-> tuple: 
    state = ["START" for i in range(num_de_estados)]
    return tuple(state)

def update_state (state:tuple[str],word:str)->tuple:
    state=state[1:]
    state = state + (word,)
    return state

def create_dict(file:list[str],generated_state:tuple)-> tuple[dict,dict]:
    state= generated_state
    dict_words:dict[tuple : list[str]] = {}
    dict_sentences:dict[str : int] = {}
    for index,line in enumerate (file) :
        sentece:str = remove_signs(line)
        dict_sentences[sentece.strip()]=index   # Generating word dictionary
        list_words:list[str] = sentece.rsplit()
        for word in list_words:
            dict_words = enter_values_into_dict(state,word,dict_words) 
            state= update_state(state,word)
        state = generated_state
    return dict_words,dict_sentences      # Returns dictionary of states and dictionary of phrases as tuple

def read_file(path: str) -> list[str]:
    try:
        file:object= open(rf"{path}", "r")
    except:
        print("Upps!!, There has been a problem")
    else:
        lines = file.readlines()
        file.close()
        return lines

if __name__ == "__main__":
    #1 - Ask for number of sentences:
    number_of_sentences:int = int(input("Cuantas phrases quieres: "))
    print() 
    #1.1 - Ask for number of states:
    number_of_states: int = int(input("Cuantos estados desea analizar: "))
    print()

    #Generating state:
    generated_state:tuple = state_generator(number_of_states)

    #3 - Read the file
    file:list = read_file(r"/home/marcos/Downloads/prueba.txt")

    #4 - Generating diccionaries
    dict_words,dict_sentences = create_dict(file,generated_state)
    
    #5 - Generating chains
    markov_generate_sentences(dict_words, dict_sentences, number_of_sentences,generated_state)
