paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#print dictionary
dir= {}
for i in range(len(paternal_age)): #make a one-to-one correspondence between parental age and rate and form a dictionary
 dir[paternal_age[i]]= chd[i]
print (dir)

age= input ("paternal age: ") #input paternal age
print ("The risk of CHD in the offspring of a father of",age,"is",dir[int(age)]) #the relative rate for a given input paternal age 

#construct a scatter plot from the data
import matplotlib.pyplot as plt
plt.scatter(paternal_age,chd, marker='*', color= 'lightpink') #define the marker and color of this plot
plt.title('parental age vs offspring health') #define the title
plt.xlabel('parental age') #define the xlable
plt.ylabel('offspring health') #define the ylable
plt.show()