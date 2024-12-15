'''project id- #CC69855
project title-Exploratory data analysis(EDA) on Iris Dataset
project level-entry level
name-Mevania Alexander'''

#importing required libraries
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Loading the dataset
df=pd.read_csv('C:/Users/mevan/Desktop/codeclause/CodeClauseInternship/project_visualization/iris_dataset.csv')


fig_size=(6,5)

# 3D scatterplot
fig=plt.figure(figsize=fig_size)
ax=fig.add_subplot(111,projection='3d')
scatter=ax.scatter(df['PetalLengthCm'], df['PetalWidthCm'], df['SepalLengthCm'],c=df['Species'].astype('category').cat.codes,cmap='viridis',s=50)
ax.set_xlabel("Petal Length")
ax.set_ylabel("Petal Width")
ax.set_zlabel("Sepal Length")
plt.title("3D Scatter Plot of Iris Dataset",fontsize=14,fontweight='bold')
plt.colorbar(scatter,label="Species")
plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1)  
plt.show()

# Histogram
plt.figure(figsize=fig_size)
sns.histplot(df,x='SepalLengthCm',kde=True,color='blue',bins=20)
plt.title("Sepal Length in Iris Dataset",fontsize=14,fontweight='bold')
plt.xlabel("Sepal Length",fontsize=10)
plt.ylabel("Frequency",fontsize=10)
plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1)  
plt.show()

# Boxplot
plt.figure(figsize=fig_size)
sns.boxplot(data=df,x='Species',y='SepalLengthCm',palette='Set2',width=0.6,showfliers=False)
sns.swarmplot(data=df,x='Species',y='SepalLengthCm',color=".25",size=5)
plt.title("Sepal Length Distribution by Species",fontsize=14,fontweight='bold')
plt.xlabel("Species",fontsize=12)
plt.ylabel("Sepal Length",fontsize=12)
plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1)  
plt.show()

#bar chart
species_avg=df.groupby("Species").mean().reset_index()
species_avg_melted=species_avg.melt(id_vars="Species",var_name="Feature",value_name="Average")
sns.barplot(data=species_avg_melted,x="Feature",y="Average",hue="Species",palette="Set2")
plt.title("Average Feature Values by Species",fontsize=14,fontweight='bold')
plt.ylabel("Average Value",fontsize=12)
plt.xlabel("Features",fontsize=12)
plt.xticks(rotation=45)
plt.show()
