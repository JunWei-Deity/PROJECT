#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Lee Jun Wei>
#Group Name: <team-junwei-mikhail-travis>
#Class: <PN2004K>
#Date: <19/02/2021>
#Version: <Python Project>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
    df = pd.read_csv('MonthyVisitors.csv')




#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    print(df)

    #display a specific country (Australia) in column #33
    country_label = df.columns[33]
    print("\n\n" + country_label + "was selected.")

    #display a sorted dataframe based on selected country
    print(" The" + country_label + "was sorted in ascending order. \n")
    sorted_df =df.sort_values(country_label,ascending=[0])
    print(sorted_df)

    #Reading csv and adding to DataFrame(df) and putting into the code
    df = df.iloc[144:276 ,9:14]

    print(df)

    #Important variables.
    my_country_list = []
    my_visitor_list = []
    total_visitors = []

    #To get the countries and visitors I want from the DataFrame(df) in csv
    for countries in df.columns[0:5]:
      my_country_list.append(countries)
      for visitors in df[countries]:
        my_visitor_list.append(visitors)
    

    for x in range(0,len(my_visitor_list)):
      if x == " na ":
        my_visitor_list[x] = 0
      else:
        my_visitor_list[x] = int(my_visitor_list[x])

    country_first = (len(my_visitor_list))/(len(my_country_list))
    id1 = 0
    id2 = int(country_first)

    #Appending the total for 1 country to the total_visitors list
    for i in range(0,len(my_country_list)):
      total_visitors.append(sum(my_visitor_list[id1:id2]))
      id1 = id1 + int(country_first)
      id2 = id2 + int(country_first)
    
    Country_dict = { my_country_list[i]: total_visitors[i] for i in range(len(my_country_list))}
    
    #Sorting out the dictionary in a descending order
    sort_Country_dict = sorted(Country_dict.items(), key=lambda x: x[1], reverse=True)
    
    Country_dict  = dict(sort_Country_dict)
    
    k =Counter(Country_dict)

    #Getting the top 3 visitors
    Top_3_Visitors = k.most_common(3)
    
    #Getting information from DataFrame(df) and putting it in.    
    df = pd.DataFrame(Top_3_Visitors,columns = ["Country","Travellers"])
    print(df)



    labels = []
    sizes = []
    #Get data from Excel for countries
    for x in df["Country"]:
      labels.append(x)
    for y in df["Travellers"]:
      sizes.append(y)

    distance = 0.1
    seperate = []

    for i in range(0, len(df['Travellers'])):
      seperate.append(distance)

    #Creating Pie Chart
    plt.pie(sizes,labels=labels, explode=seperate, startangle=90, autopct='%1.2f%%',shadow=True)

    plt.axis('equal')

    plt.legend(loc="best")
 
    plt.show()
    
    

    

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################