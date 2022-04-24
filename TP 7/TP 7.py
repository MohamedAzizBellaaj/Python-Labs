# def afficher(cls):
#     print("Hello")


# class personne:
#     # greetings = classmethod(afficher)
#     pass


# personne.greetings = classmethod(afficher)
# p = personne()
# p.greetings()

# class MaClasse:
#     def __init__(self):
#         self.__num = 1

#     def _get_num(self):
#         return self.__num


# obj = MaClasse()
# print(obj.__dict__)

# class Citron:
#     def __init__(self, masse):
#         self._masse = masse

#     def get_masse(self):
#         print("Coucou je suis dans le get")
#         return self._masse

#     def set_masse(self, value):
#         print("Coucou je suis dans le set")
#         if value < 0:
#             raise ValueError("Pas de masse négatif")
#         self._masse = value

#     def del_masse(self):
#         del self._masse
#     masse = property(fget=get_masse, fset=set_masse, fdel=del_masse)


# obj = Citron(5)
# # x = obj.masse
# # obj.masse = -9
# del(obj.masse)
# print(obj.__dict__)
