"""
Converts semi-major axis in period.
a: semimajor axis in au (astronomical unit)
p: period in a (year == annus)
""" 
from math import sqrt

def a2p(a):
    return sqrt(a**3)


def p2a(p):
    return (p**2)**(1/3)


def main():
    print("convert  a = 1.00000011")
    a = 1.00000011 # au
    print(a2p(a))

    print("convert  p = 1.0000001650000045")
    p = 1.0000001650000045 # a
    print(p2a(p))


if __name__ == '__main__':
    main()