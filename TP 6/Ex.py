from Package.Point import Point

p = Point(5, 6)
p2 = Point(8, 9)
p.afficher()
p.deplacer(1, 1)
p.afficher()
print(p.distance(p2))
print(p == p2)
