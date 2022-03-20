# Ex1
# text=input()
# x=0
# for c in text:
#     if c in ['a','e','y','u','i','o']:
#         x+=1

# print("Le nbr de voyelles est",x)

# Ex2
# i=1
# s=0
# while i<=10 :
#     print("Saisir l'entier",i,end=' ')
#     x=int(input())
#     if(x<0) :
#         print("Erreur: Pas d'entiers negatifs !")
#         break
#     s+=x
#     i+=1
# else:
#     print("La somme est",s)

# Ex3
# l=eval(input("Donner une liste : "))
# l1=[x for x in l if x%2==1]#impair
# l2=[x for x in l if x%2==0]#pair
# print("Liste impair :",l1)
# print("Liste pair :",l2)

# Ex4
# l=eval(input("Donner une liste : "))
# l=[x for x in l if not(x.upper() in['A','E','Y','I','U','O'])]
# print("Nouvelle liste : ",l)

# Ex5
# l1=eval(input("Donner une liste de mois : "))
# l2=eval(input("Donner une liste de jours : "))
# print(list(zip(l1,l2)))

# Ex6
# l=[[1,2,3],[4,5,6],[7,8,9]]
# l1=[y for x in l for y in x]
# print("Nouvelle liste : ",l1)