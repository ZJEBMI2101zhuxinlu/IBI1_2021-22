#3.1 some simple math
a= 19245301
b= 4218520
c= 271
d= b-c
e= a-b
print ("the difference between the numbers of cases in 2020 and 2021 is",d)
print ("the difference between the numbers of cases in 2021 and 2022 is",e)
if d<e:
 print ("e is greater")
else:
 print ("d is greater")
#e is greater. So 2021 has the greatest number of new COVID-19 cases.

#3.2 booleans
X= True
Y= True
W= X and Y
print (W)

X= True
Y= False
W= X and Y
print (W)

X= False
Y= True
W= X and Y
print (W)

X= False
Y= False
W= X and Y
print (W)

X="x"
Y=""
W= X and Y
print (W)

X="x"
Y="y"
W= X and Y
print (W)
