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