# from Package.Point import Point


# class Polygon:
#     def __init__(self, *args):
#         self.points = [x for x in args]

#     def perimetre(self):
#         s = 0
#         for i in range(len(self.points)-1):
#             s += self.points[i].distance(self.points[i+1])
#         s += self.points[len(self.points)-1].distance(self.points[0])
#         return s


# x1 = Point(5, 5)
# x2 = Point(10, 6)
# x3 = Point(7, 5)
# obj = Polygon(x1, x2, x3)
# print(obj.points[0])
# print(obj.perimetre())
