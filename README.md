# Machine Learning framework project documentation


## 1.Main goals of this project
### 1.1 Implemented goals

  - Collect all of the most important machine learning libraries (tools, frameworks etc.) that are available on GitHub.
  - Calculate a score for each one based on the statistics (stars, watch, forks, contributors).
  - Keep track of tendencies and be able to predict future alterations in popularity.
  - Move the project to Microsoft Azure, where score updates would happen on some trigger.
  
### 1.2 Opportunities for developing the project
  
  - Display frameworks descending order in a visually pleasing manner.
  - Finer scoring system. 
  - ML grouping by types.
  
  
  


## 2.Calculation of the score



The score is calculated from stars, watch, forks and contributor numbers. The result is the length of a vector in a 4-dimensional space. After having calculated all of the needed vector lengths, normalized score can be computed that gives more of a comprehensible rank. 


The following formula gives the basis of comparison:

<p align="center">

<img src="https://raw.githubusercontent.com/maraid/md_test/master/formula.png"/>

</p>



## 3.Tech

The project uses a number of different tools to work properly:

  - [Python 3.6](https://www.python.org/) - Python programming language.
  - [Bit Bucket] (https://bitbucket.org/miamanoteam/ml-frameworks/src/master/ and https://bitbucket.org/miamanoteam/framework-       collector/src/master/)-Version control system.  Every script and database is contained in a Bit Bucket repository. 
  - [Google Sheets API](https://developers.google.com/sheets/api/v3/) - Creating quick and easy Google spreadsheets. 
  - [D3.js](https://d3js.org/) - Vizualization of data.  
  - [Azure functions](https://azure.microsoft.com/en-in/overview/serverless-computing/) - Azure cloud where the script will be running.
  - [Some database](#) - Storing the values with dates on Azure servers. 

## 4.Python packages
  - Maybe list them. Unimportant.
  
## 5.Architecture

The project has two major parts both running on **Microsoft Azure**.

- The first one, called the **“collector”** is in charge of gathering the information that is needed for calculating the scores for each framework in the given moment. 

- The second part is a **web app**, that consist of a database with all the previously recorded data, an API providing access for the database and the frontend, that visualizes the findings.

### 5.1Collector

The **collector** is a Python script, running on an Azure function app. Every time it runs, it records the data needed for calculating the scores and uploads it to the database. The process goes as follows:

- The fuction app containing the script of the collector is triggered by another function app, which had to be put in place because in Azure Python function apps not yet come with the feature enabling them to be scheduled in a cron-like way.

- The script accesses a list consisting all the names of the **GitHub** repositories that we gather data about.

Code snippet:

[
```
https://github.com/BVLC/caffe,

https://github.com/opencv/opencv,

https://github.com/tensorflow/tensorflow,

https://github.com/scikit-learn/scikit-learn,

https://github.com/keras-team/keras,

...
```
]

- Using a **GitHub** module for Python the script gets the data about the certain repository. **GitHub** has its own API, although working directly with it provided good enough results, later we started using the github module for Python as a “middleware”, because it had proven to be easier and more stable.

	Code snippet:
	pip install github
	
- The data is then structured, so that it could be sent via a post request to the following access point of the API: 

Code snippet:

```https://ml-frmwks.azurewebsites.net/api/insert```

About authentication details could be found under the part concerning the API.	

### 5.2Web App

- **Database:** The project uses a MySql database that is included into the Azure web app, the project does not have its own SQL server, that has its pros and cons. The database has the following table structures:

Code snippet:

```CREATE TABLE frameworks (
 id varchar(255) NOT NULL,
 url varchar(255) DEFAULT NULL,
 name varchar(255) DEFAULT NULL,
 repo_desc text
 );

CREATE TABLE snapshots (
 id int(11) NOT NULL,
 timestamp date DEFAULT NULL,
 framework_id varchar(255) DEFAULT NULL,
 stars_count int(11) DEFAULT NULL,
 contributors_count int(11) DEFAULT NULL,
 forks_count int(11) DEFAULT NULL,
 watchers_count int(11) DEFAULT NULL
 );
CREATE TABLE timestamps (
timestamp date NOT NULL
 );
```


- **API and backend:** The API written in Node.js in the framework “Express”. It is responsible for writing and retracting data from the database.  It uses the packet “mysql” to communicate with the database. The usage of this npm packet comes in handy for numerous reasons, like security, since the queries processed with it are checked for SQL injections.

The endpoints and features of the API are documented in a standalone documentation on Swagger, that is specialized for API documentation and endpoint testing. Check it out on www.ml-frmwks.azurewebsites.net/api

The site has a lightweight backend also written in node.js, yet somewhat separated from the API parts. Other than handling the requests towards the site, some settings for the site improving security is implemented in the backend.

- **Frontend:** The frontend of the web app is written in html and javascript. Graphs and charts are made with D3.js, a javascript library for data visualization.


_Frontend link_: http://ml-frmwks.azurewebsites.net


