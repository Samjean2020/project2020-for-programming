                                    
                                  I. Summary of the Iris Dataset
The Iris dataset is a well known dataset containing information on three different types of Iris flowers: the Irish Setosa, Iris Versicolor and Iris Virginica (Schutten, Wiering, 2016, 2). Ronald .A. Fisher is the principal architecture of this dataset. The British statistician and biologist published the dataset for the first time in 1936, in his work: The Use of multiple measurements in taxonomic problems. This study is published in The Annals of Human Genetics, 1925-54, p.2 (179-188). Since then, various versions of the dataset have been published. Dr. E. Anderson is also an architecture of the iris dataset, for collecting the data, to investigate the flowers and set measurements used by Fisher (Fisher, The Annals of Human Genetics, p. (2) 179). In the pattern recognition literature, iris dataset is possibly the best known database to be found. Until now, Fisher’s paper is the standard in the realm, and is cited recurrently (Scikit-learn, July 1988). However, biologist, botanist and statistical scientists sometimes have a debate on the veracity of the iris dataset, particularly regarding the possession or not of sepal by Iris flowers, (Kozak, Lotocka, 2014, p.579.). This debate is out of the scope of this project. The purpose of this project is to show how to investigate a dataset, manipulate variables and their attributes, and output results using a programming language, as Python is used for the in this project. Furthermore, the outputs are analysed according to quantitative data analysis methods, including univariable analysis, bivariate analysis, multivariate analysis (elaboration analysis), measures of association, regression analysis (linear regression analysis, multiples, partial and curvilinear) (Babbie, 2001, pp383-463). The overarching aim of analysis of data is finding relationships between different variables, the dataset contains, as this project does. This project uses the iris dataset version available at https:// git.github.com/csv. A converted into a text file version is uploaded into our git account under the repository project2020-for-programming at Github (URL address: https://github.com/Samjean2020/project2020-for-programming.git). A raw version is accessible at: "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv" this link is incorporated in the programme called "analysis.py" uploaded in this repository.
                             
                                  * Dataset Characteristics

Dr E. Anderson found the iris flowers (Iris setosa and Iris versicolor), growing together in the same colony and measured them (Fisher, p.179, The Annals of Human Genetics). Dataset specifications comprise 150 as the number of instances, 50 in each of the three classes. The number of attributes is represented by 4 numeric, predictive attributes and the class. Attribute information is as follows: sepal length in cm, sepal width in cm, petal length, petal width in cm and class including Iris-Setosa, Irish Versicolor and Iris Virginica (Scikit-learn, July 1988). "WHEN two or more populations have been measured in several characters[] special interest attaches to certain linear functions of the measurements by which the populations are best discriminated" (Fisher 1936, p.179 (2)). Two first species are best discriminated through particular linear function( Fisher 1936,p.179(2)). 

 
                                      II. Prerequisites
                                      
  In order to run the analysis.py programme the following modules are needed: 
  
  1. Matplotlib.pyplot.
  2. Pandas 
  3. Seaborn
  4. Numpy
  5. Python
  6. Iris dataset


                                      1. Matplotlib.pyplot

"Matplotlib is a library for making 2D plots of arrays in Python. Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB, and can be used in a Pythonic, object oriented way. Although Matplotlib is written primarily in pure Python, it makes heavy use of NumPy and other extension code to provide good performance even for large arrays."(https://matplotlib.org/users/history.html)


                                      2. Pandas DataFrames
                                      
"Pandas DataFrames are data structures that contain data organized in two dimensions, rows and columns labels that correspond to the rows and columns". (https://realpython.com/pandas-dataframe/#introducing-the-pandas-dataframe). "Working with labeled data like pandas DataFrames. Plot methods which take arrays as inputs can now also work with labeled data and unpack such data."(https://matplotlib.org/users/prev_whats_new/whats_new_1.5.html?highlight=pandas#id6.   
This means that the following two examples produce the same plot:

Example 1 

df = pandas.DataFrame({"var1":[1,2,3,4,5,6], "var2":[1,2,3,4,5,6]})
plt.plot(df["var1"], df["var2"]). 

Example 2

plt.plot("var1", "var2", data=df).                          
                                                       
                                      3. Seaborn       
                                      
Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures.
Here is some of the functionality that seaborn offers:
•	A dataset-oriented API for examining relationships between multiple variables
•	Specialized support for using categorical variables to show observations or aggregate statistics
•	Options for visualizing univariate or bivariate distributions and for comparing them between subsets of data
•	Automatic estimation and plotting of linear regression models for different kinds dependent variables
•	Convenient views onto the overall structure of complex datasets
•	High-level abstractions for structuring multi-plot grids that let you easily build complex visualizations
•	Concise control over matplotlib figure styling with several built-in themes
•	Tools for choosing color palettes that faithfully reveal patterns in your data.

Seaborn aims to make visualization a central part of exploring and understanding data. Its dataset-oriented plotting functions operate on dataframes and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots.
Here’s an example of what this means:
import seaborn as sns
sns.set()
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
            data=tips);
  (http://seaborn.pydata.org/introduction.html)
  
                                         
                                         4. Numpy
  
NumPy is the fundamental package for scientific computing with Python. It contains among other things:
•	a powerful N-dimensional array object
•	sophisticated (broadcasting) functions
•	tools for integrating C/C++ and Fortran code
•	useful linear algebra, Fourier transform, and random number capabilities
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.NumPy is licensed under the BSD license, enabling reuse with few restrictions. (https://numpy.org/).


                                          5. Python

Python is a programming language that lets you work more quickly and integrate your systems more effectively. 
(https://www.python.org/about/). Applications for Python include but not limited web and internet development, scientific and numeric, education, desktop GUIS, software development and business application (https://www.python.org/about/apps/). 

                        III. Research of data and summary as above.

                        IV.  Dataset uploaded on the repository as above

                        V.   Data analysis as per the program analysis.py.                           
                             

                        1. Dataset Access

The function df = pd.read_csv gives access to the dataset online via the link provided, and outputs the iris dataset with all its attributes: 5 variables and 150 rows x 5 columns. 4 variables are numerical, except variety which is nominal. 

                        2. Summary of each variable

Using describe () function outputs a table containing four variables of the dataset including sepal.length, sepal.width, petal.length and petal.width. The describe () function also presents the following statistics features of the dataset (Mittapalli, 2018), such as count, mean, std, min,   25%, 50%, 75%. All values of variables (4) containing in the table are floating-points numbers. Count of 150 for each variable, mean or average is situated between 5.8 to 1.1(petal width the smallest amount), the std or standard deviation (a quantity expressing by how much the members of a group differ from the mean value for the group) is    between 0.4 to 1.7 with petal.length, the greater; min (the lowest observation) is situated between 0.1 to 4.3, with sepal width in the middle; 25%(lower or first quartile of value) (Liberto, May 15, 2019),  is situated between 0.3 to 5.1 with sepal.length on the top  ; 50% (median value) is between 1.3 to 5.8 with sepal.length higher and petal width the lowest; and finally, 75% (the fourth quartile of value) is between 1.8 to 6.4 sepal.length on the top and petal.width at the lowest level, petal.length and sepal.width are respectively at 2nd  and 3rd  levels. The difference between min (4.3), mean (5.8) and median (5.8) is not significant for sepal.length, but it is, somehow for petal.length.

                        3. Plotting Analysis
                        
This part includes univariate analysis and bivariate analysis. 

                      3.1 Univariate analysis

Univariate analysis is the analysis of a single variable at a time (Bryman, 2008, p.700). It is the analysis of a single variable for purposes of description; this includes frequency distribution, averages, and measures of dispersion (Barbbie, 2001, p. G11). Because Univariate analysis does not involve the relationships between two variables or more variables, its purpose is descriptive, rather than explanatory (Barbbie, 2001, p.414). All histogram plots will be analyse here. I have included a pairplot of the variable variety, as well as a plot of the same, because they are dealing with one variable. 

                      3.1.1 Histogram plots
                      
                3.1.1.1 Histogram sepal.length 
                
Use data frame function: plt.hist (df ["sepal.length"]), to get the output the above histogram. Its analysis is as follows: all values on x-axis (horizontal) have each a count on the y-axis (vertical). Value at almost 5.5 has greater count (>25), while less count (5) is observed at between values 7.0 to 7.5. The average is situated at value 5.0.

              3.1.1.2 Histogram sepal.width 

Use data frame function: plt.hist (df ["sepal.width"]), to get the output the above histogram. Its analysis is as follows: all values on x-axis (horizontal) have each a count on the y-axis (vertical). Value at 3.0 has greater count (>35), while less account (<2) is observed from value 4.0 to 4.5. The second position of count (30) is located between values 3.0 to 3.5. Values from 2.5 to 3.5, with 3.0 included, are above the average situated between count 15 to 20. There is a constant increase of count from value 2.0 reaching its pick of count 35 at the value 3.0; a decrease is observed after that point till value 4.5. 

              3.1.1.3 Histogram petal.length 

Use data frame function: plt.hist (df ["petal.length"]), to get the output the above histogram. Its analysis is as follows: all values on x-axis (horizontal) have each a count on the y-axis (vertical). Value 1 has greater count (>35), while the 3 value is the least (<5). There is a caveat between value 2 and 3, this may suggest a missing value. A regular tendency of count reduction is observed from value 5 to value 7. The average is situated at value 5 (5.5). There is a gradual increase of count from at almost value 3 (count 4), reaching a pick at almost value 5 and decreasing afterward till value 7.


              3.1.1.4 Histogram petal.width

Use data frame function: plt.hist (df ["petal.width"]) to get the output the above histogram. Its analysis is as follows: all values on x-axis (horizontal) have each a count on the y-axis (vertical). Value 0.0 has greater count (>40), while less count is observed at 0.5 plus (<2 count). Value at almost 1.5 comes in the second position with count between 30 to 35. The average is situated at almost value 2.0.

              3.1.1.5 Histogram variety: Setosa, Versicolor, Virginica
              
Use data frame function: plt.hist (df ["variety"]) to get the output the above histogram. Its analysis is as follows: all values on x-axis (horizontal) have measurements on the y-axis (vertical). These are comprised between 0.0 to 1.0; with an interval of 0.2 each. The measurement of each of the 3 iris (i) flowers: I. Setosa, I. Versicolor and I. Virginica is identical (1.0). A vertical format is observed.

              3.1.1.6 Pairplots of the variable “variety”
              
Use seaborn function: sns.pairplot (df, hue="variety") to get the output of the above histogram. Its analysis is as follows: a matrix of all variables, including histograms for univariate distributions and scatterplots for joint relationships (https://seaborn.pydata.org/generated/seaborn.pairplot.html).  Scatterplots will be examined next (bivariate analysis)
   
              3.1.1.7 Variable variety plot

Use dataframe function: plt.plot (df ["variety"] , "y.") to get outputs of the above plot. Its analysis is as follows: there is an apparent indication of equal proportion (50) of each iris flower. This corroborates with the dataset description as mentioned above. 
Next, is bivariate analysis.


              3. 2 Bivariate analysis
              
Bivariable analysis focuses on relationships between variables rather than comparisons of groups. Bivariate analysis explores the statistical association of between the independent variable and the dependant variable. Its purpose is usually explanatory rather than merely descriptive (Barbbie, 2001 p. 414). Bivariate analysis is the examination of the relationship between two variables, as in contingency tables or correlation (Bryman, 2008, p.693).

              3.2.1 Scatter plots

              3.2.2 Scatter: sepal.length vs petal.length

Use dataframe function: plt.plot (df ["sepal.length"], df["petal.length"], "g.") to get the above plot. Its analysis is as follows: sepal length values are on x-axis, numerical values are assigned from 4.5 to 8 (cm) with an interval of 0.5 cm. petal length values(cm) are placed on y-axis starting from 1 to 7 with an interval of 1 in between, them. There is a progression of green dots starting from 3 (y-axis) and 5.0 (x-axis) to 7(y-axis) and 8.0 (x-axis), clustering in the middle. There is also a bit of cluster at the very bottom left 1-2 (y-axis) and from 4.5 to 5.5 (x-axis). Top left is empty, while some dots are at the corner right. As sepal length increases there is also an increase on petal length of the flower (for example 8.0 (cm) sepal length is associated with 7 (cm) petal length, both big measurements. They have 1 cm of difference. This is to say that sepal length of the flowers is bigger than the petal length one’s. There is a correlation between the two variables.  

              3.2.3 Scatter: sepal.width vs petal.width

Use dataframe function: plt.plot (df["sepal.width"], df["petal.width"], "b.")  to get the above plot. Its analysis is as follows: sepal width values are on x-axis, numerical values are assigned from 2.0 to 4.5 (cm) with an interval of 0.5 cm. petal width values(cm) are placed on y-axis starting from 0.0 to 2.5  with an interval of 0.5 as well. Corner left is empty as well as is the corner right. A cluster of dots is observed from 1.0 (y-axis) to 2.5 and from 2.5 to almost 3.5 on the (x-axis). There is a discontinued vertical line made of dots starting at 3.0 (x-axis) ending to almost 2.5 at the opposed axis.  A bit of cluster of dots from the middle (3.0) on petal width side, ending to 4.0. Bottom left is almost clear. There is arguably a bit of relationship between the two variables.

              3.2.4 Scatter: sepal.length vs petal.width

Use dataframe function: plt.plot (df ["sepal.length"], df ["petal.width"], "r."), to get the above plot. Its analysis is as follows: sepal length values are on x-axis, numerical values are assigned from 4.5 to 8.0 (cm) with an interval of 0.5 cm. petal width(cm) are placed on y-axis starting from 0.0 to 2.5,  with an interval of 0.5. Corner left is empty, whereas corner right is not. There is an apparent clustering of dots all way long from the bottom left towards corner right occupying the body of the scatterplot. This leaves both corners left and bottom right clear. There is arguably a bit of relationship between the two variables.

              3.2.5 Scatter: sepal.width vs petal.length

Use dataframe function: plt.plot (df["sepal.width"], df["petal.length"], "c.")  to get the above plot. Its analysis is as follows: sepal width values are on x-axis, numerical values are assigned from 2.0 to 4.5 (cm) with an interval of 0.5 cm. petal length values(cm) are placed on y-axis starting from 1 to 7,  with an interval of 1. Corner left is empty, as well as is the corner right. An agglomeration of dots is at 3 level (y-axis) ending to 7 on the same axis. A discontinued vertical line starting from 3.0 (x-axis) and ending to almost 7 (y-axis). Bottom left is almost clear with 1 dot located between 2.0 to 2.5. A bit of dispersed dots from 3.0 to 4.5 on the bottom right (x-axis). There is arguably a bit of connection between the two variables.

              3.2.6 Scatter: petal.length vs sepal.length

Use dataframe function: plt.plot (df ["petal.length"], df ["sepal.length"], "m.") to get the above plot. Its analysis is as follows: petal length values are on x-axis, numerical values are assigned from 1-7(cm) with an interval of 1 cm. sepal length values (cm) are placed on y-axis starting from 4.5 to 8, with an interval of 0.5. Both variables have a difference of 1 cm: 7 for petal and 8 for sepal, which have greater measurements. There is a concomitant increase of both variables values starting mainly at 1 from x-axis with a brief caveat between 2-3 on the same axis till the corner right, at the same level of 8 on (y-axis). Corner left is clear, as well as is the bottom right. A cluster of dots between 1 and 2 (x-axis) till 6.0 (y-axis) is observed.  There is arguably a correlation between the two variables. 

              3.2.7 Scatter: petal.width vs sepal.width

Use dataframe function: plt.plot (df ["petal.width"], df ["sepal.width"], "y.") to get the above plot. Its analysis is as follows: petal width values are on x-axis, numerical values are assigned from 0.0 (cm) to 2.5 with an interval of 0.5 cm. sepal width values (cm) are placed on y-axis starting from 2.5 to 4.5, with an interval of 0.5. Two scatters of dots around 3 to 4.5 on y-axis, and 1 to 2.5 on the x-axis. The middle of the plot is clear. Agglutination of dots is on both extremes (y-axis) as well as (x-axis), leaving the middle of the plot clear. In terms of size, the width of the iris flower petal is bigger than its sepal one’s.

             3.2.8 Scatter: petal.length vs sepal.width

Use dataframe function: plt.plot (df["petal.length"], df["sepal.width"], "g.") to get the above plot. Its analysis is as follows: petal length values are on x-axis, numerical values are assigned from 1-7(cm) with an interval 1 cm. sepal width values (cm) are placed on y-axis starting from 2.0 to 4.5, with an interval of 0.5. Clusters of dots are on both axes, starting from 3 to 7 on the x-axis side and from 3.0 to 4.5 on y-axis. Clustering behave as separated entities, leaving a clear path in the middle of the scatterplot. 

             3.2.9 Scatter: petal.width vs sepal.length

Use dataframe function: plt.plot (df ["petal.width"], df ["sepal.length"], "k.") to get the above plot. Its analysis is as follows: petal width values are on x-axis, numerical values are assigned from 0.0 to 2.5 (cm) with an interval 0.5 cm. sepal length values(cm) are placed on y-axis starting from 4.5 to 8.0,  with an interval of 0.5.  Corner left is totally free, as well as is the bottom right. The body of the scatterplot is clustered with dots. The two variables go along, as there is an increase on their respective measurements. There is arguably a correlation between the two variables. 



                                          III Conclusion
                                    
 This project, on Iris dataset, ends here. It has taken into consideration all tasks, required by the examiner.
                                    
                                          IV References

Babbie E. (2001) “The Practice of Social Research 9th edition (Belmont: Wadsworth/Thomson Learning) 

Bryman, A. (2008) “Social Research Methods” (Oxford: Oxford University Press)

Fisher R.A (1936) “The Use of Multiples Measurements in Taxonomic Problems” in The Annals of Human Genetics, 1925-1954 (179-188) (PDF). Available at https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x(Accessed on 05/04/2020)

Kozak M. and Lotocka B (2014) " What should we know about the famous Iris data?  ". Available at: https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data


Liberto (D.)  (May 15, 2019) “Quartile”. Available at https://www.investopedia.com/terms/q/quartile.asp (Accessed on 25/04/2020)

Mittapalli H (Dec 24, 2018) “Exploratory Data Analysis: Iris DataSet”. Available at  
https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e (Accessed on 25/04/2020)

Python.org “About Python”. Available at https://www.python.org/about/  (Accessed on 05/04/2020)  

Real Python.org “Introducing the pandas dataframe” .Available at (https://realpython.com/pandas-dataframe/#introducing-the-pandas-dataframe (Accessed on 05/04/2020).

Real Python.org “Matplotlib.pyplot “. Available at (https://matplotlib.org/users/history.html) (Accessed on 05/04/2020).

Real Python.org "Working with labelled data like pandas” Available at (https://matplotlib.org/users/prev_whats_new/whats_new_1.5.html?highlight=pandas#id6 (Accessed on 05/04/2020).

Seaborn.pydata.org “Introduction to seaborn”. Available at http://seaborn.pydata.org/introduction.html (Accessed on 05/04/2020)
Seaborn.pydata.org“seaborn.pairplot” .Available at :(https://seaborn.pydata.org/generated/seaborn.pairplot.html). (Accessed on 25/04/2020) 

Scikit-learn, July 1988. Available at: https://scikit-learn.org/stable/datasets/index.html (Accessed on 25/04/2020)


Schutten M, Wiering M. A.  (2016) “An Analysis on Better Testing than Training Performances on the Iris Dataset, available at https://www.researchgate.net/publication/310463971_An_Analysis_on_Better_Testing_than_Training_Performances_on_the_Iris_Dataset/link/582ec9f708ae138f1c031311/download(PDF) (Accessed on 05/04/2020) 





                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
