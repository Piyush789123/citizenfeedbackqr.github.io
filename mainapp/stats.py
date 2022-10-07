# from matplotlib.pyplot import figure 
import mpld3
import matplotlib.pyplot as plt  
import numpy as np
cities=["ahemdabad","surat","porbandar","rajkot","varodra"]
posfeed=[800,550,250,690,500]
negfeed=[890,600,200,900,100]
# fig = figure()
# ax = fig.gca()
x=np.arange(len(cities))
plt.bar(x -0.2,posfeed,0.4,color='y',edgecolor='black',label="postive feedbacks")
plt.bar(x +0.2,negfeed,0.4,color='b',edgecolor='black',label="negative feedbacks")
plt.xlabel("City")
plt.ylabel("Number of feedbacks")
plt.title("Type of feedback")
plt.legend()
plt.xticks(x, cities)
plt.show()