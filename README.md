                                    
                                  Summary of the Iris Dataset


                                  Introduction

The Iris dataset is a well known dataset containing information on three different types of Iris flowers: the Irish Setosa, Iris 
Versicolor and Iris Virginica (Schutten, Wiering, 2016, 2). Ronald .A. Fisher is the principal architecture of this dataset. The British statistician and biologist published the dataset for the first time in 1936, in his work: The Use of multiple measurements in taxonomic problems. This study is published in The Annals of Human Genetics, 1925-54, p.2 (179-188). Since then, various versions of the dataset have been published. Dr. E. Anderson is also an architecture of the iris dataset, for collecting the data, to investigate the flowers and set measurements used by Fisher (Fisher, The Annals of Human Genetics, p. (2) 179). In the pattern recognition literature, iris dataset is possibly the best known database to be found. Until now, Fisher’s paper is the standard in the realm, and is cited recurrently (Scikit-learn, July 1988). However, biologist, botanist and statistical scientists have sometimes  a debate on the veracity of the iris dataset, particulary regarding the possession or not of sepal by Iris flowers, (Kozak, Lotocka, 2014, p.579.  is out of the scope of this project. The purpose of this project is to show how to investiagte a dataset, manipulate variables and their attributes, and outputs results using a programming language, as Python is used for the purpose of this project. Furhermore, the outputs are analysed according to quantitative data analysis methods, including univariable analysis, bivariate analysis, multivariate analysis (elaboration analysis), measures of association, regression analysis (linear regression analysis, multiples, partial and curvilinear)(Babbie, 2001, pp383-463). The overaching aim of analysis of data is finding relationships between different variables, the dataset contains, as this project does. This project uses the iris dataset version available at https:// git.github.com/csv. A converted into a text file version is uploaded into our git account under the repository project2020-for-programming at Github (URL address: https://github.com/Samjean2020/project2020-for-programming.git). A raw version is accessible at: "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv" this link is incorporated in the programme called "analysis.py" uploaded in this repository. 

                                  Dataset Characteristics

Dr E. Anderson found the iris flowers (Iris setosa and Iris versicolor), growing together in the same colony and measured them (Fisher, p.179, The Annals of Human Genetics). Dataset specifications comprise 150 as the number of instances, 50 in each of the three classes. The number of attributes is represented by 4 numeric, predictive attributes and the class. Attribute information is as follows: sepal length in cm, sepal width in cm, petal length, petal width in cm and class including Iris-Setosa, Irish Versicolor and Iris Virginica (Scikit-learn, July 1988). "WHEN two or more populations have been measured in several characters[] special interest attaches to certain linear functions of the measurements by which the populations are best discriminated" (Fisher 1936, p.179 (2)). Two first species are best discriminated through particular linear function( Fisher 1936,p.179(2)). 

 
                                      I. Prerequisites
                                      
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

   
                                          6. Iris dataset
                                          
See dataset as described above.

                                    
                                    
                                    II Analysis
                                    
                                    Problem statement
                                    
       This project is about Fisher’s Iris Dataset. Documentation and code are written in Python. 
       The outline includes: 
       (1) research and summary of the data in README, 
       (2) download the data set and add it to our repository, 
       (3) write a program called analysis.py that outputs:
        > a summary of each variable to a single text file, 
        > saves a histogram of each    variable to png files, 
        > and outputs a scatter plot       of each pair of variables.

                          (1) Research and summary of the data in README
                          
                                                                        
                          
                          

                          (2) Download the data set and add it to our repository




                          (3) Write a program called analysis.py
                          

                            •	a summary of each variable to a single text file



                            •	a histogram of each variable to png files



                            •	a scatter plot of each pair of variables
                             


                                    III Conclusion
                                    
                                    

                                    IV References

Babbie E. (2001) “The Practice of Social Research 9th edition (Belmont: Wadsworth/Thomson Learning) 

Fisher R.A (1936) “The Use of Multiples Measurements in Taxonomic Problems” in The Annals of Human Genetics, 1925-1954 (179-188) (PDF). Available at https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x(Accessed on 05/04/2020)


Python.org “About Python”. Available at https://www.python.org/about/  (Accessed on 05/04/2020)  

Real Python.org “Introducing the pandas dataframe” .Available at (https://realpython.com/pandas-dataframe/#introducing-the-pandas-dataframe (Accessed on 05/04/2020).

Real Python.org “Matplotlib.pyplot “. Available at (https://matplotlib.org/users/history.html) (Accessed on 05/04/2020).


Real Python.org "Working with labelled data like pandas” Available at (https://matplotlib.org/users/prev_whats_new/whats_new_1.5.html?highlight=pandas#id6 (Accessed on 05/04/2020).

Seaborn.pydata.org “Introduction to seaborn”. Available at http://seaborn.pydata.org/introduction.html (Accessed on 05/04/2020)

Schutten M, Wiering M. A.  (2016) “An Analysis on Better Testing than Training Performances on the Iris Dataset, available at https://www.researchgate.net/publication/310463971_An_Analysis_on_Better_Testing_than_Training_Performances_on_the_Iris_Dataset/link/582ec9f708ae138f1c031311/download(PDF) (Accessed on 05/04/2020) 











                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
