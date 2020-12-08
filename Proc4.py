import math
def TrianglePS(a):
    P=3*a
    S=(a**2*math.sqrt(3))/4
    return P,S
for i in range(1,4):
    a=float(input("Сторона а= "))
    print("Треугольник со стороной  ",a)
    P,S =TrianglePS(a)
    print("Периметр= ",P)
    print("Площадь= ",S)
TrianglePS(a)
