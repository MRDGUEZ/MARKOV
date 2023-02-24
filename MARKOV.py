import random
import string

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

        if  state in dict_words[('END',)]:
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

def read_file(path: str) -> dict[int:str]:
    try:
        with open(rf"{path}", "r") as file:
            lines ={ i:line for i,line in enumerate(file.readlines())}
            return lines
    except:
        print("Upps!!, There has been a problem")


def remove_signs(file : dict[int:str])->dict[str:int]:
    for line in file.keys() :
        file [line]=file[line].translate(str.maketrans('','',string.punctuation)).lower().strip()
    return file


def state_generator(num_de_estados:int=2)-> tuple: 
    return ("START",) * num_de_estados


def update_state (state:tuple[str],word:str)->tuple:
    return state[1:]+(word,)


def enter_values_into_dict(state: tuple, word: str, dict_words: dict[tuple : list[str]]) -> dict[tuple: list[str]]:
    dict_words.setdefault(state,[]).append(word)
    return dict_words

def create_dict(file:dict[int:str],generated_state:tuple)-> tuple[dict,dict]:
    state= generated_state
    dict_words:dict[tuple : list[str]] = {('END',):[]}
    for line in file.keys() :
        if file[line].strip():
            list_words:list[str] = file[line].rsplit()
            for word in list_words:
                dict_words = enter_values_into_dict(state,word,dict_words) 
                state= update_state(state,word)
            dict_words[('END',)].append(state)
            state = generated_state
    return dict_words      # Returns dictionary of states 


if __name__ == "__main__":
    #1 - Ask for number of sentences:
    number_of_sentences:int = int(input("Cuantas phrases quieres: "))
    print() 
    #1.1 - Ask for number of states:
    number_of_states: int = int(input("Cuantos estados desea analizar: "))
    print()

    #Generating state:
    generated_state:tuple = state_generator(number_of_states)

    #3 - Read the file and remove signs
    file:list = read_file(r"/home/marcos/Downloads/MARKOV/prueba.txt")
    file = remove_signs(file)

    #4 - Generating diccionaries
    dict_words = create_dict(file,generated_state)

    # #5 - Generating chains
    markov_generate_sentences(dict_words, file, number_of_sentences,generated_state)
