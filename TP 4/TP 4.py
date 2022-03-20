# Ex 1
# d={"mot":"word","fait":"do"}
# d1={d[e]:e for e in d}
# print(d1)

# Ex 2
# p=input("Phrase = ")
# l=p.split(" ")
# d={e:l.count(e) for e in l}
# print(d)

# Ex 3
# noms=[nom for nom in input("Liste des noms = ").split()]
# prenoms=[prenom for prenom in input("Liste des prenoms = ").split()]
# notes=[note for note in input("Liste des notes = ").split()]
# dic={ (e[0],e[1]): e[2] for e in zip(noms,prenoms,notes) }
# print(dic)

# x=2
# l=[1,2]
# s="salut"
# d={1:'mot'}
# def fct(x,l,s,d):
#     x+=1
#     l.append(4)
#     s="bonjour"
#     d[2]="phrase"
#     return s
# s=fct(x,l,s,d)
# print(x,l,s,d)

# x=2
# def fct2():
#     global x 
#     x=4  
# fct2()
# print(x)

# Ex
# def parler_enthousiasme(msg,nb=1,bool=False):
#     "!"*nb
#     if bool :
#         print(msg.upper(),"!"*nb)
#     else:
#         print(msg,"!"*nb)
# parler_enthousiasme("hello",5,True)
# parler_enthousiasme("hello",bool=True,nb=5)
# parler_enthousiasme("hello",8)
# parler_enthousiasme("hello")