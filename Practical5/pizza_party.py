p=1 #define the number of pieces and start with 1
n=0 #define the number of cuts and start with 0
while p<64: 
#when the number of pizza pieces is less than 64, keep cutting the pizza until there is enough for each IBI student
#after each while cycle, increase the number of cuts and count the number of pieces of the current pizza
 n=n+1
 p=(n**2+n+2)/2
 print ("with straight cuts",n,", the number of pieces of piazza is",p) #the total number of pieces of pizza that can be cut for an increasing number of straight cuts until there are enough pieces for each member of the class
str(n) #convert n into a string
print ("When the number of straight cuts of pizza reaches",n,", there are enough pieces of pizza for each IBI1 student.") #print the final number of cuts
