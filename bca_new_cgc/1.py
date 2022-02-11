# Calculator
import math

print('''Operations List

1 : Add                     8 : Area Of Circle                14 : Volume Of Cube
2 : Subtract                9 : Area Of Rectangle             15 : Volume Of Cylinder
3 : Multiply                10 : Area Of Triangle             16 : Volume Of Sphere
4 : Division                11 : Area Of Square               17 : Volume Of Cone
5 : Modulus                 12 : Area Of Trapezoid            
6 : Square                  13 : Area Of Parallelogram        
7 : Cube                    


''')

ab = int(input('Select the Operation : '))

if ab == 1:
  i = int(input('Pick 1st Value : '))
  j = int(input('Pick 2nd Value : '))
  print(i+j)


elif ab == 2:
  i = int(input('Pick 1st Value : '))
  j = int(input('Pick 2nd Value : '))
  print(i-j)


elif ab == 3:
  i = int(input('Pick 1st Value : '))
  j = int(input('Pick 2nd Value : '))
  print(i*j)


elif ab == 4:
  i = int(input('Pick 1st Value : '))
  j = int(input('Pick 2nd Value : '))
  print(i/j)


elif ab == 5:
  i = int(input('Pick 1st Value : '))
  j = int(input('Pick 2nd Value : '))
  print(i%j)


elif ab == 6:
  i = int(input('Give the value : '))
  print('Square of',i,'=',i**2)


elif ab == 7:
  i = int(input('Give the value : '))
  print('Cube of',i,'=',i**3)


elif ab == 8:
  r = int(input('Radius of circle : '))
  print('Area Of Circle =',math.pi*r*r)


elif ab == 9:
  l = int(input('Size Of Length : '))
  b = int(input('Size Of Width :'))
  print('Area Of Rectangle =',l*b)


elif ab == 10:
  h = int(input('Size Of Height : '))
  b = int(input('Size Of Base :'))
  print('Area Of Triangle =',int(b*h/2))


elif ab == 11:
  s = int(input('Size Of Sides :'))
  print('Area Of Square =',s*s)


elif ab == 12:
  sb = int(input('Size Of Short Base :'))
  lb = int(input('Size Of Long Base :'))
  h = int(input('Size Of Altitude : '))
  print('Area Of Trapezoid =',((sb+lb)/2)*h)


elif ab == 13:
  h = int(input('Size Of Height : '))
  b = int(input('Size Of Base :'))
  print('Area Of Parallelogram =',b*h)


elif ab == 14:
  i = int(input('Give the Length of edge or side : '))
  print('Volume Of Cube =',i**3)


elif ab == 15:
  r = int(input('Give the Radius of the circular base :'))
  h = int(input('Give the Height :'))
  print('Volume Of Cylinder =',math.pi*r*r*h)


elif ab == 16:
  r = int(input('Give the Radius of the sphere'))
  print('Volume Of Sphere =',(4/3)*math.pi*r**3)


elif ab == 17:
  r = int(input('Give the radius of the cone :'))
  h = int(input('Give the height of the cone :'))
  print('Volume Of Cone =',(math.pi*r*r*h)/3)