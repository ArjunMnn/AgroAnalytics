import sys
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
rain = pd.read_excel("rainfalldata.xlsx")
temp = pd.read_excel("temperaturedata.xlsx")

# read the cleaned data
year=int(sys.argv[1])
crop  = sys.argv[2]
sum = 0
print(year)
for i in rain[year]:
    sum+=i
avgrain = (sum)//12
sum=0
for i in temp[year]:
    sum+=i
avgtemp = (sum)//12

crop = crop.lower()
if crop=="wheat":
    devtemp = abs(avgtemp-20)
    temper=50-((devtemp/avgtemp)*100)//2
    devrain = abs(avgrain-24)
    rainper = 50-((devrain/avgtemp)*100)//2
    #print(temper,rainper)
    sucess = temper+rainper
elif crop=="rice":
    devtemp = abs(avgtemp-30)
    temper=50-((devtemp/avgtemp)*100)//2
    devrain = abs(avgrain-100)
    rainper = 50-((devrain/avgtemp)*100)//2
    #print(temper,rainper)
    sucess = temper+rainper
elif crop=="bajra":
    devtemp = abs(avgtemp-25)
    temper=50-((devtemp/avgtemp)*100)//2
    devrain = abs(avgrain-20)
    rainper = 50-((devrain/avgtemp)*100)//2
    #print(temper,rainper)
    sucess = abs(temper+rainper)


output = "Success percentage = "+str(abs(sucess))+"%"

#print("i have got the input ",output)
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],rain[year],label = "rain(mm)",color="blue")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],temp[year],label = "temp(°C)",color="red")
plt.legend(loc="upper left")
plt.title(output)

plt.savefig(r"C:\python\button\static\images\test.jpg")