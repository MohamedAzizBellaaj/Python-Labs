# Ex1
# ch=input("Chaine à tester = ")
# ch=ch.lower()
# c=True
# size=len(ch)
# i=0
# while c and (i<=(size//2)):
#     c=(ch[i]==ch[size-i-1])
#     i+=1
# else:
#     if(c):
#         print(ch+" est palindrome")
#     else:
#         print(ch+" n'est pas palindrome")
# Ex2
# ch1=input("Chaine1 = ")
# ch2=input("Chaine à cherecher dans Chaine1 = ")
# i=0
# l=[]
# while i!=-1:
#     i=ch1[i:].find(ch2)
#     if i==-1:
#         print("Pas d'occurence")
#         break
#     l.append(i)
#     i+=len(ch2)
# else:
#     print(l)

# Ex3
# phrase=input("Phrase = ")
# l=phrase.split()
# res=[(x,len(x)) for x in l]
# print(res)

# Ex4
# noms=[nom for nom in input("Entrer les noms ").split()]
# prenoms=[prenom for prenom in input("Entrer les prenoms ").split()]
# ages=[int(age) for age in input("Entrer les ages ").split()]
# res=zip(noms,prenoms,ages)
# i=0
# for i in res:
#     print("Le nom est",i[0].upper(),"Le prenom est",i[1].capitalize(),"L'age est",i[2])

# Ex5
# phrase={mot for mot in input("Phrase = ").split()}
# stopword={word for word in input("Stopwords = ").split()}
# res=phrase-stopword
# print(res)

# Ex5v2
# stopwords={word for word in input("Stopwords = ").split()}
# phrase={phrase for phrase in input("phrase = ").split() if not in stopwords}
# print(phrase)