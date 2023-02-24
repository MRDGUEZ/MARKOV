## Markov Chain
A Markov chain or Markov process is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.
Informally, this may be thought of as, ```" What happens next depends only on the state of affairs now."```

Markov chains have many applications as statistical models of real-world processes,such as studying cruise control systems in motor vehicles, queues or lines of customers arriving at an airport, currency exchange rates and animal population dynamics.

In this case we use markov chain to generate phrases that there are not exist .

## Generate sentences:
```Python
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
```
We use the variable 'count' to know how many phrases we have generated and the variable 'attempts' to limit the number of attempts to find new requested phrases

We have three dictionaries:

One for the states and the words that precede them  ``` dict_words:dict[tuple : list[str]]```

The second where the original phrases of the document are stored without punctuation marks ```dict_sentences : dict[str : int]  ```

And finally a dictionary with the phrases that I have made ``` phrases_made : dict[str : int]  ```

### To update and create states :

I used tuples to get the result

```python
def state_generator(num_de_estados:int=2)-> tuple: 
    return ("START",) * num_de_estados

def update_state (state:tuple[str],word:str)->tuple:
    return state[1:]+(word,)
```
### To add values to the dictionary and remove punctuation marks:

```python
def enter_values_into_dict(state: tuple, word: str, dict_words: dict[tuple : list[str]]) -> dict[tuple: list[str]]:
    dict_words.setdefault(state,[]).append(word)
    return dict_words

def remove_signs(file : dict[int:str])->dict[str:int]:
    for line in file.keys() :
        file [line]=file[line].translate(str.maketrans('','',string.punctuation)).lower().strip()
    return file
```

### To generate state and word dictionary and phrase dictionary:

```python
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
```
### And finally to read a file and return a list of phrases
```python
def read_file(path: str) -> dict[int:str]:
    try:
        with open(rf"{path}", "r") as file:
            lines ={ i:line for i,line in enumerate(file.readlines())}
            return lines
    except:
        print("Upps!!, There has been a problem")
```
