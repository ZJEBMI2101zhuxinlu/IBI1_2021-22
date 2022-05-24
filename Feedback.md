The formative feedback found me lacking in two aspects:

1. in Week5, for File pizza_party.py, the marker thought pseudocode could have been a bit more detailed, e.g. what is the while loop doing?
   
   So I add some pseudocode:
      "
      
      p=1 #define the number of pieces and start with 1
      
      n=0 #define the number of cuts and start with 0
      
      while p<64: 
      
      #when the number of pizza pieces is less than 64, keep cutting the pizza until there is enough for each IBI student
      
      #after each while cycle, increase the number of cuts and count the number of pieces of the current pizza
      
      "

2. in Week6, for Parental age vs offspring health, the marker thought pseudocode could again be a bit more detailed.
  
   So I add some pseudocode:
      
      "
      dir= {} #first define an empty dictionary
      
      for i in range(len(paternal_age)): 
      
      #by for loop, make a one-to-one correspondence between parental age and rate and form a dictionary
      
      #make the paternal_age the key and make the chd the value
      
        dir[paternal_age[i]]= chd[i] #add a key-value pair in the dictionary
      
      print (dir) #print dictionary

      
      plt.scatter(paternal_age,chd, color= 'lightpink') #define the marker and color of this plot
      
      plt.title('parental age vs offspring health') #define the title
      
      plt.xlabel('parental age') #define the xlable
      
      plt.ylabel('offspring health') #define the ylable
      
      "

You can see my formative feedback in 1082_marks.xlsx and check my improvement in Practical5:pizza_party.py and Practical6:offspring_health.py.

In addition, I have added some pseudo-code and commit messages for some other files:)
