from math import*
number1=input("enter your square number1")
sqrt = (float(number1))**0.5
rem1 = sqrt % 1
if rem1 == 0:
    perfect_sqr=[number1]
else: 0
#square= round(sqrt)**2

number2=input("enter your square number2")
sqrt = (float(number2))**0.5
rem2= sqrt % 1
#square= round(sqrt)**2
if rem2==0:
    perfect_sqr.append(number2)
else:0

number3=input("enter your square number3")
sqrt = (float(number3))**0.5
rem3= sqrt % 1
#square= round(sqrt)**2
if rem3==0:
    perfect_sqr.append(number3)
    print(perfect_sqr)
else:
    print("perfect square are",perfect_sqr)

