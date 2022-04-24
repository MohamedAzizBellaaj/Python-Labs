# class voiture:
#     """Classe voiture 
#     """
#     nombre = 0
#     # __slots__ = ("numero", "marque")

#     def __init__(self, numero):
#         self.numero = numero
#         voiture.nombre += 1

#     def afficher(self):
#         print("une première méthode")

#     def setMarque(self, m):
#         self.marque = m

#     @staticmethod
#     def afficherNombre():
#         print(voiture.nombre)

#     def __del__(self):
#         print("Mort de l'objet")

#     def __str__(self):
#         return(str(self.numero))

#     def __eq__(self, other):
#         return self.numero == other.numero
#     def __ne__(self, other):
#         return not self.numero==other.numero
#     pass


# # v = voiture()
# # v.couleur = "rouge"
# # v2 = voiture()
# # v2.marque = "clio"
# # print(v.__dict__)
# # print(v2.__dict__)
# # print(v.__doc__)
# # print(v.__class__)
# # v.afficher()
# # v = voiture(12)
# # print(v.__dict__)
# # v.setMarque("Clio")
# # print(v.__dict__)

# # v = voiture(15)
# # print(v.numero)
# # v.marque = "Clio"
# # print(v.marque)
# # ! Error with __slots__ :
# # v.serie="190"
# # print(v.serie)

# # print(v.__slots__)

# v = voiture(15)
# v2 = voiture(158)
# v3 = voiture(160)
# print(v.nombre)
# print(voiture.nombre)

# v.nombre = 5
# print(v.nombre)
# # del(v)
# print(voiture.nombre)
# voiture.afficherNombre()
# print(str(v))
# print(v==v2)