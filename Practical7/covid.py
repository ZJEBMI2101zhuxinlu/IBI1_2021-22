import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the .csv file works
os.chdir("C:/Users/86183/IBI1/IBI1_2021-22/Practical7") #the marker can change the path here:)
covid_data=pd.read_csv("full_data.csv")

#the first and third columns from rows 10-20
print(covid_data.iloc[9:20,0:3:2]) #or[10:21]. Rob said they are all right:)

#"total cases" for all rows corresponding to Afghanistan
my_columns = [False, False, False, False, True, False]
my_rows=[]
for i in range(0,len(covid_data)):
 if covid_data.loc[i,"location"] == "Afghanistan":
     my_rows.append(True)
 else:
     my_rows.append(False)
print(covid_data.loc[my_rows,my_columns])

# the mean number of new cases and new deaths in China
# the proportion of new cases that kill the infected person
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
print (china_new_data)
china_dates=china_new_data.iloc[:,0]
new_cases_mean=np.mean(china_new_data["new_cases"])
print('the mean number of new cases:',new_cases_mean)
new_deaths_mean=np.mean(china_new_data["new_deaths"])
print('the mean number of new death:',new_deaths_mean)
rate=new_deaths_mean/new_cases_mean
print ('the death rate:',rate)

#a boxplot of new cases and new deaths in China worldwide
x1=china_new_data["new_cases"]
x2=china_new_data["new_deaths"]
plt.boxplot([x1,x2],labels=['new_cases','new_deaths'])
plt.title("the boxplots of new cases and new deaths in China worldwide")
plt.ylabel('number')
plt.show()

plt.boxplot([x1,x2],labels=['new_cases','new_deaths'],showfliers=False) #here the outliers do not show to make the boxplots look more beautiful
plt.title("the boxplots of new cases and new deaths in China worldwide without outliers")
plt.ylabel('number')
plt.show()

# both new cases and new deaths in China over time
x=china_dates
y1=china_new_data["new_cases"]
y2=china_new_data["new_deaths"]
plt.plot(x,y1,'ro',x,y2,'bo')
plt.xticks(x.iloc[0:len(china_dates):4],rotation=-90)
plt.title('new cases and new deaths in China over time')
plt.xlabel('date')
plt.ylabel('number')
plt.legend(['new_cases','new_deaths'])
plt.show()

#Question: Are there places in the World where there have not yet been more than 10 total infections (as of 31 March)? If so, where are they?
last=covid_data.loc[covid_data['date']=='2020/3/31',['location','total_cases']]
print(last.loc[last['total_cases']<=10,'location'])
