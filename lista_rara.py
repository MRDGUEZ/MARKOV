# l = 'START' * 10




# def list_update( lista,word):
#     lista=lista[1:]
#     lista+=" "+ word
#     return lista

# while True:
#     word = input ("PALABRA: ")
#     l=list_update(l,word)
#     print(l)

dict_b={ (2,3,4):"B"}
t=None
if (2,3,4) in dict_b:
    print("si")
    t=(2,3,4) + (2,)
    dict_b[t]= "C"
    if (2,3,4,2) in dict_b:
        print("funciona")
        t = t[1:]
        print(t)
        print(type (t))

    
