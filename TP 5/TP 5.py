# Ex 1
# def ouvrage(titre,*args,**kargs):
#     print("Titre =",titre)
#     print("Liste des auteurs :",args)
#     print("Info supplémentaires :",kargs)
# ouvrage("kteb","ali","salah","gssfdg",annee=1998,maison="dar")

# help(print)

# Ex 2 
# l=[{"note":5},{"note":4}]
# l.sort(key= lambda x :x["note"])
# print(l)

# Ex 3
# def afftuple(x1) :
#     for i in x1 :
#         yield i*i
# x=(1,2,5,4,5,848,545,5487,558,484,545,65,544,5,84,484,85,5454,54545,544545,12121,2121,21212,787878787,484845)
# for i in afftuple(x) :
#     print(i)

# import Modules 
# print(Modules.somme(5,2))

# import Modules as m
# print(m.somme(5,2))

# from Modules import somme 
# print(somme(5,2))


# from Modules import somme as sum
# print(sum(5,2))

# import Package.Module2 as k
# k.salut()