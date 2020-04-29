# Jean-Samuel Bonsenge-Bokanga

# This program (analysis.py) 
# outputs a summary of each variable to a single file text file,
# saves a histogram of each variable to png files, and
# outputs a scatter of each variable of each pair of variables.

# import the prerequisites modules below to execute this program in tandem with python.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# use dataframe function to access the iris dataset.

df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

# outputs a summary of each variable.
df.describe() 

# outputs a histogram of the variable sepal.length.
plt.hist(df["sepal.length"])
plt.title("histogram sepal.length in cm")
plt.xlabel("sepal.length in cm")
plt.ylabel("count")
plt.legend()
plt.savefig("histogram sepal.length.png")
plt.clf()

# outputs a histogram of the variable sepal.width.

plt.hist(df["sepal.width"])
plt.title("histogram sepal.width in cm")
plt.xlabel("sepal.width in cm")
plt.ylabel("count")
plt.legend()
plt.savefig("histogram sepal.width.png")
plt.clf()

# outputs a histogram of the variable petal.length.

plt.hist(df["petal.length"])
plt.title("histogram petal.length in cm")
plt.xlabel("petal.length in cm")
plt.ylabel("count")
plt.legend()
plt.savefig("histogram petal.length.png")
plt.clf()

# outputs a histogram of the variable petal.width.
plt.hist(df["petal.width"])
plt.title("histogram petal.width in cm")
plt.xlabel("petal.width in cm")
plt.ylabel("count")
plt.legend()
plt.savefig("histogram petal.width.png")
plt.clf()

# outputs a histogram of the variable variety.
plt.hist(df["variety"])
plt.title("histogram variety:Setosa, Versicolor, Virginica")
plt.xlabel("variety:")
plt.ylabel("variety measurements")
plt.legend()
plt.savefig("histogram variety iris flowers.png")
plt.clf()


# outputs a scatter plot of two variables:
# sepal.length vs petal.length.
plt.plot(df["sepal.length"], df["petal.length"], "g.")
plt.title(" sepal.length(cm) vs petal.length(cm)")
plt.xlabel("sepal.length (in cm)")
plt.ylabel("petal.length(in cm)")
plt.legend()
plt.savefig("scatter.sepal.length vs petal.length.png")
plt.clf()


# outputs a scatter plot of two variables:
# sepal.width vs petal.width.
plt.plot(df["sepal.width"], df["petal.width"], "b.")
plt.title("sepal.width vs petal.width(cm)")
plt.legend()
plt.xlabel("sepal.width(in cm)")
plt.ylabel("petal.width(in cm)")
plt.savefig("scatter.sepal.width vs petal.width.png")
plt.clf()


# outputs a scatter plot of two variables:
# sepal.length vs petal.width.
plt.plot(df["sepal.length"], df["petal.width"], "r.")
plt.title(" sepal.length vs petal.width(cm)")
plt.legend()
plt.xlabel("sepal.length(cm)")
plt.ylabel("petal.width(cm)")
plt.savefig("scatter.sepal.length vs petal.width.png")
plt.clf()



# outputs a scatter plot of two variables:
# sepal.width vs petal.length.
plt.plot(df["sepal.width"], df["petal.length"], "c.")
plt.title(" sepal.width vs petal.length(cm)")
plt.legend()
plt.xlabel("sepal.width(cm)")
plt.ylabel("petal.length(cm)")
plt.savefig("scatter.sepal.width vs petal.length.png")
plt.clf()


# outputs a scatter plot of two variables:
# petal.length vs sepal.length.
plt.plot(df["petal.length"], df["sepal.length"], "m.")
plt.title(" petal.length vs sepal.length(cm)")
plt.legend()
plt.xlabel("petal.length(cm)")
plt.ylabel("sepal.length(cm)")
plt.savefig("scatter.petal.length vs sepal.length.png")
plt.clf()

# outputs a scatter plot of two variables:
# petal.width vs sepal.width.
plt.plot(df["petal.width"], df["sepal.width"], "y.")
plt.title("petal.width vs sepal.width(cm)")
plt.legend()
plt.xlabel("petal.width(cm)")
plt.ylabel("sepal.width(cm)")
plt.savefig("scatter.petal.width vs sepal.width.png")
plt.clf()

# outputs a scatter plot of two variables:
# petal.length vs sepal.width.
plt.plot(df["petal.length"], df["sepal.width"], "g.")
plt.title("petal.length vs sepal.width(cm)")
plt.legend()
plt.xlabel("petal.length(cm)")
plt.ylabel("sepal.width(cm)")
plt.savefig("scatter.petal.length vs sepal.width.png")
plt.clf()


# outputs a scatter plot of two variables:
# petal.width vs sepal.length.
plt.plot(df["petal.width"], df["sepal.length"], "k.")
plt.title("petal.width vs sepal.length(cm) ")
plt.legend()
plt.xlabel("petal.width(cm)")
plt.ylabel("sepal.length(cm)")
plt.savefig("scatter.petal.width vs sepal.length.png")
plt.clf()

# outputs a pairplot of the variable variety.
sns.pairplot(df, hue="variety")
plt.title("scatter pairplots of variables")
plt.savefig("pairplotsvariety.png")


# outputs a plot of the variable variety,
# which indicates an equal proportion (50) of each iris flower.
plt.plot(df["variety"] , "y.")
plt.title("variety plot")
plt.xlabel("quantity measured")
plt.ylabel("type of iris flower")
plt.legend()
plt.savefig("varietyplot.png")
# this function (plt.show()) may be needed if the plot does not show up,
# and this applies to all plots above.
plt.show() 
plt.clf



