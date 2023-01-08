import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv('real_time_stock_data.csv') # read data from csv into variable df

x_val = [] # empty list for x axis (same for each plot)

y_val1 = [] # empty list to store y-axis data (prices) for each stock
y_val2 = []
y_val3 = []
y_val4 = []

for i in range(len(df)): 
    '''
    loop through the data 'n' times, 
    where n is the number of rows
    given by len(df) 
    '''
    x_val.append(i+1) # append x-axis values (number of rows) 

    y_val1.append(df.iloc[i,2]) # append price values of each stock to corresponding y value list
    y_val2.append(df.iloc[i,3])
    y_val3.append(df.iloc[i,4])
    y_val4.append(df.iloc[i,5])

# create subplots for each stock
fig = plt.figure() 
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

plt.style.use('fivethirtyeight') # set visual style of plot
axes1.set_title('Amazon', fontsize = 12) # title each plot with stock name
axes2.set_title('Google', fontsize = 12)
axes3.set_title('Tesla', fontsize = 12)
axes4.set_title('Meta', fontsize = 12)

# create empty list for each plot
x = [] 
y1 = []
y2 = []
y3 = []
y4 = []
'''
note: this is neccessary beacuse FuncAnimation calls the function 'animate'
each time. To animate graph, values from the original lists must be appended
to new lists so each point can be plotted step by step, creating moving line animation.
If original lists (y_val1, y_val2, etc.) are used, 
the graph would appear all at once (no animation)
'''

def animate(i):
    x.append(x_val[i]) # append each value from the 'x_val' list into new list 'x'

    y1.append(y_val1[i])  # append each value from the corresponding 'y_val' list into new 'y' list
    y2.append(y_val2[i])
    y3.append(y_val3[i])
    y4.append(y_val4[i])

    axes1.plot(x,y1,scalex=True,scaley=True) # plot each value in the 'x' list with corresponding 'y' value
    axes2.plot(x,y2,scalex=True,scaley=True)
    axes3.plot(x,y3,scalex=True,scaley=True)
    axes4.plot(x,y4,scalex=True,scaley=True)
    
ani = FuncAnimation(fig, animate, interval = 1000) # use FuncAnimation to plot each point step by step, creating animation
plt.tight_layout() # evenly space plots
plt.show()


