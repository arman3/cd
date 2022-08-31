import math
import matplotlib.pyplot as show
a = True

while a == True:
    #Initial Height
    H1 = float(input('Enter initial height in m: '))
    if (H1<0):
        print('')
        print('YOU CANNOT THROW FROM UNDERGROUND!! Initial Height cannot be less than 0: ')
        continue
    #Initial Velocity
    V1 = float(input('Enter initial velocity in m/s: '))
    if (abs(V1)>299792458):
        print('')
        print('ITS BEYOND SPEED OF LIGHT!! You cant just break physics: ')
        continue
    #Firing Angle
    T1 = float(input('Enter firing angle less than 90 with respect to +x-axis in degrees: '))
    #Horizontal Acceleration
    aX = float(input('Enter horizontal acceleration in m/s^2: '))
    #Vertical Acceleration
    aY = float(input('Enter vertical acceleration in m/s^2 (-9.81 in Earth): '))
    if (aY>=0):
        print('')
        print('IN WHAT PLANET ARE YOU?! Y-acceleration cannot be greater or equal 0: ')
        continue
    else:
        break
    
v_x1 = math.cos(math.radians(T1)) * V1
v_y1 = math.sin(math.radians(T1)) * V1
x = [0]
y = [H1]
t = 0
while True:
    t = t + 0.1
    ex = v_x1*t + (1/2)*aX*t**2
    ey = v_y1*t + (1/2)*aY*t**2 + H1
    x.append(ex)
    y.append(ey)
    if ey <= 0:
        break
show.xlabel('Horizontal Distance')
show.ylabel('Vertical Distance')
show.plot(x,y,label='Path of Projectile')
show.grid()
show.legend()
if (T1>90):
    print('')
    print('You threw it backwards -.- ')
if (V1<0):
    print('')
    print('You threw it backwards -.- ')
