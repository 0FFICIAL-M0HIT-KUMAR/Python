#Write a python function to display the sin cos tan sec  cosec cot values of the angle entered by user.
#user will enter the angle in degrees.

from fractions import Fraction
# import math
import numpy

def trignomatric(x):
    
    #VIA NUMPY LIBRARY 👇
    # sin_w_numpy= numpy.sin(numpy.deg2rad(x))
    # print(f"VIA NUMPY DECIAMAL --> {round(sin_w_numpy,2)}")
    # print(f"VIA NUMPY FRACTION --> {Fraction(sin_w_numpy).limit_denominator()}")

    #VIA MATH LIBRARY 👇
    # # sin_value=math.radians(x)
    # # sin_value=math.sin(sin_value)
    # # sin_value=round(sin_value, 2)
    # # sin_value=Fraction(sin_value).limit_denominator()
    # # print(sin_value)
    # sin_value = math.sin(math.radians(x))
    # print(f"VIA MATH DECIMAL   -->{round(sin_value, 2)}")
    # print(f"VIA MATH FRACTION  -->{Fraction(sin_value).limit_denominator()}")

    print(f"sin   {x}degree is --> {round(numpy.sin(numpy.deg2rad(x)), 2)}") #or {Fraction(numpy.sin(numpy.deg2rad(x))).limit_denominator()}
    print(f"cos   {x}degree is --> {round(numpy.cos(numpy.deg2rad(x)), 2)}")
    print(f"tan   {x}degree is --> {round(numpy.tan(numpy.deg2rad(x)), 2)}")
    print(f"cosec {x}degree is --> {round(1/(numpy.sin(numpy.deg2rad(x))), 2)}")
    print(f"sec   {x}degree is --> {round(1/(numpy.cos(numpy.deg2rad(x))), 2)}")
    print(f"cot   {x}degree is --> {round(1/(numpy.tan(numpy.deg2rad(x))), 2)}")


angle_in_degree=int(input("Enter the angle in degree : "))
trignomatric(angle_in_degree)