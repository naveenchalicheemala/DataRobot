# DataRobot
Take Home project for Data Robot


Link for application: https://finddatatypeapp.herokuapp.com/


**Objective**:

The objective of findingdatatype application is to get the data type of each attribute or column of the given sheet. Input to the application is publicly available google sheet url and the sheet name for which we need to find the result. These are the data types that are categorized for this application result: **Boolean, Integer, Float, String, DateTime**


**Tools and Technologies used:**

1.	HTML, CSS using Bootstrap – For Client side
2.	HTML Forms using Django Framework
3.	Python – For server side
4.	Google sheets API – To process and retrieve the data from google sheets
5.	Git and GitHub – Version control system used to handle the project repository
6.	Heroku – Cloud platform used to deploy and maintain the application


**Project setup:**

1.	Install Python 3.9 
2.	Download all the dependencies mentioned in requirements.txt. It can be done using pip install on the terminal
3.	Install git on local machine 
4.	Create a git account and download the repository using git clone
5.	Download Python Editor to view and modify the code (PyCharm, Sublime Text, Visual studio code etc.)
6.	Open the project in the editor
7.	Run Python3 manage.py runserver to run the application in local
8.	Use http://127.0.0.1:8000/ or http://locahost:8000 to open application on browser


**How does it work:**


  The application is built on Django framework which is an open-source python web framework. 
  Basically, Django is implemented based on Model-View-Template architecture. 

  * The model layer is for structuring and manipulating the data of web application. For this application, database is not used as there is no need to store        the data to display the data type. 

  * The view layer is to encapsulate the logic responsible for processing user’s request and sending the response. This application has a home view which takes the      request as an input and do the necessary validations for sheet URL and sheet name before processing.
  
    Once the input field validations are done, URL is processed using Google sheets API to retrieve data from the sheet. The credentials JSON need to be created for      google sheets API to access the sheets. This JSON file is used in the project to authorize and retrieve data. URL is processed by retrieving the sheetID in URL      and the sheet name. The data retrieved is copied to the data frame using Pandas. 
  
    Iterate through each column in the sheet. For each column, iterate through all the values and find the data type using below methodology. Python type() method      is    used to find the data type of each value in the column. The result dictionary is used to store the result of each column. The data type of first value is       stored    and if next row has different value than earlier one, then compare the two types:

      1. If a column has only one type of values, then the data type of that column would be same type

      2. If a column has both Integer and Float, then the data type would be determined as Float

      3. If a column has mixed types, then the data type would be determined as String (which is considered as object in case of pandas)

  * In this project, Django forms are used to get input from the user which has three components (UrlField for Google sheet url, CharField for sheet name and            submit button). This form is used in the HTML template which also has other elements displaying the output dictionary using lists and bootstrap grid styling







