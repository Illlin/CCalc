from math import cos, sqrt
from Units import Length,C

wavelength = Length()
wavelength.set_nm(640)

def RedshiftZ(v,theta):
    return ((1+v*cos(theta)/C)/(sqrt(1-pow(v,2)/pow(C,2))))

print(RedshiftZ(-C*0.999,0))