from math import sqrt

def equation(a, b, c):
    D = b*b-4*a*c
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    return x1, x2

print('корни уравнения: ', equation(1, 10, -39))