paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#print dictionary
dir= {}
for i in range(len(paternal_age)):
 dir[paternal_age[i]]= chd[i]
print (dir)

age= input ("paternal age: ") #input paternal age
print ("The risk of CHD in the offspring of a father of",age,"is",dir[int(age)])

#construct a scatter plot from the data
import matplotlib.pyplot as plt
plt.scatter(paternal_age,chd, marker='*', color= 'lightpink')
plt.title('parental age vs offspring health')
plt.xlabel('parental age')
plt.ylabel('offspring health')
plt.show()