import pandas as pd 
import numpy as np 
import sklearn as sk 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
data = pd.read_csv("RainfallData.csv") 
data1 = pd.read_csv("TemperatureData.csv") 
  
# the output or the label. 
Y = data['PrecipitationSumInches'] 
# reshaping it into a 2-D vector 
Y = Y.values.reshape(-1, 1) 
  

day_index = 798
days = [i for i in range(Y.size)] 
 
clf = LinearRegression() 

clf.fit(X, Y) 
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 

# estimating coefficients 
b = estimate_coef(x, y) 
'''print("Estimated coefficients:\nb_0 = {}  \ 
      \nb_1 = {}".format(b[0], b[1])) '''

# plotting regression line 
plot_regression_line(x, y, b) 
  
inp = np.array([[74], [60], [45], [67], [49], [43], [33], [45], 
                [57], [29.68], [10], [7], [2], [0], [20], [4], [31]]) 
inp = inp.reshape(1, -1) 
  

print('The precipitation in inches for the input is:', clf.predict(inp)) 
   
  class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c = 0
        for i in range(len(A)):
            if A[i] in 'aeiouAEIOU':
                c+=len(A)-i;
        return c%10003
  

  
print("Precipitation vs selected attributes graph: ") 
  
for i in range(x_vis.columns.size): 
    plt.subplot(3, 2, i + 1) 
    plt.scatter(days, x_vis[x_vis.columns.values[i][:100]], 
                                               color = 'g') 
  
    plt.scatter(days[day_index],  
                x_vis[x_vis.columns.values[i]][day_index], 
                color ='r') 
  
    plt.title(x_vis.columns.values[i]) 
  
plt.show() 
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_colwidth', -1)
labels=['1','2','3','4','5']
months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#months=['January','February','March','April','May','June','July','August','September','October','November','December']
temp=pd.cut(temp,5,right=False,labels=labels)
temp3=[]
j=0
for k in range(8):
  temp2=[]
  for i in range(16):
    temp2.append(temp[j:j+12])
    j+=12
  temp3.append(temp2)

tempnagpur=pd.DataFrame(temp3[0],columns=months)
writer = pd.ExcelWriter('TemperatureData.xlsx')
writer1 = pd.ExcelWriter('RainfallData.xlsx')
temp.to_excel(writer)
temp1.to_excel(writer)