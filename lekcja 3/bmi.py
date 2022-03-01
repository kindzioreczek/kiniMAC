'''
skrypt obliczajacy bmi

BMI = waga (kg)/ wzrost (m^2)
uwaga wzrost podajemy w cm

'''
weight = input("Podaj wagę w kg: ")
height = input("Podaj wzrost w cm: ")

#print(weight, hight)
weight = int(weight) #konwertujemy z napisu na int
height = int(height)

# liczenie formuły
# BMI = weight /pow (height/100, 2) #do potęgi to pow jest
# print(BMI)

BMI = weight / (height/100)**2
#print(BMI)

import math
# BMI = weight / math.pow(height/100, 2)
# print(BMI)

# usuniecie kodu to command + "?"

BMI = weight / (height/100)**2
#print("Twoje BMI = " + str( round(BMI, 2)))
print(f"Twoje BMI = {BMI:.2f}") #. + ile liczb po przecinku +f (fload)

"""
<18,5 -zjedz cos
>=18.5 i <25 - jest ok
> 25 - ogranicz kebaby
"""

if BMI>= 25:
    print("ogranicz kebaby")
    print("ogranicz peri peri")
elif BMI<18.5:
    print("Zjedz cos")
else:
    print("jest supcio")