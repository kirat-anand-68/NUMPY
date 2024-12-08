#matplotlib-> seaborn is a library that uses the matplotlib underneath to plot the graph->
#Displot is distribution plot(curve plot same as histogram)

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot([0,1,2,3,4,5])
# plt.show()
#Plotting a distplot withou histogram
import matplotlib.pyplot as plt
import seaborn as sns
x=([0,1,2,3,4])
sns.distplot(x,hist=False)
plt.show()
