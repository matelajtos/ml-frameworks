# Machine Learning framework project documentation


### 1.Main goals of this project
#### 1.1 Implemented goals

  - Collect all of the most important machine learning libraries (tools, frameworks etc.) that are available on GitHub.
  - Calculate a score for each one based on the statistics (stars, watch, forks, contributors).
  - Keep track of tendencies and be able to predict future alterations in popularity.
  - Move the project to Microsoft Azure, where score updates would happen on some trigger.
  
#### 1.2 Opportunities for developing the project
  
  -Display frameworks descending order in a visually pleasing manner.
  -Finer scoring system.
  -ML grouping by types.
  
  
  


### Calculation of the score

The score is calculated from stars, watch, forks and contributor numbers. The result is the length of a vector in a 4-dimensional space. After having calculated all of the needed vector lengths, normalized score can be computed that gives more of a comprehensible rank.

The following formula gives the basis of comparison:

<p align="center">

<img src="https://raw.githubusercontent.com/maraid/md_test/master/formula.png"/>

</p>



### Tech

The project uses a number of different tools to work properly:

  - [Python 3.6](https://www.python.org/) - Python programming language.
  - [Bit Bucket] (https://bitbucket.org/miamanoteam/ml-frameworks/src/master/ and https://bitbucket.org/miamanoteam/framework-       collector/src/master/)-Version control system.  Every script and database is contained in a Bit Bucket repository. 
  - [GitHub API](https://developer.github.com/v3/) - Accessing stats.
  - [Google Sheets API](https://developers.google.com/sheets/api/v3/) - Creating quick and easy Google spreadsheets. 
  - [D3.js](https://d3js.org/) - Vizualization of data.  
  - [Azure functions](https://azure.microsoft.com/en-in/overview/serverless-computing/) - Azure cloud where the script will be running.
  - [Some database](#) - Storing the values with dates on Azure servers. 

### Python packages
  - Maybe list them. Unimportant.
  
### Architecture

There is a Python script **Collector** in our Azure account. It queries the current values and names of libraries from GitHub API once a week. It is unnecessary to query data every day, because it makes the downloading time longer and visualization works also properly on this way.  

_Framework-collector link:_ https://bitbucket.org/miamanoteam/framework-collector/src/master/

There is also a Web Application in Azure account which contains the **frontend**. Trends are visualized here.

_Frontend link_: http://ml-frmwks.azurewebsites.net

## Functions of frontend







#### GitHub API:
  - The API can be accessed by the following URL: [https://api.github.com/](https://api.github.com/).
  - For accessing the **name**, **star**, **watch**, **fork** and **license** information of a repository through the API, simple [GET requests](https://developer.github.com/v3/repos/#get) can be used without any parameters.  
    ```
    GET /repos/:owner/:repo
    ```
    The returned JSON formatted dictionary contains the project name as _'name'_ and also the stats under the names _'stargazers_count'_, _'subscribers_count'_, _'forks_count'_ respectively.
  - In order to access the number of **contributors** the same method cannot be applied, since the API doesn't have a functionality for it.
  To get the number [pagination](https://developer.github.com/v3/guides/traversing-with-pagination/) can be used as shown in [this](https://stackoverflow.com/a/44347632) StackOverflow answer:  
  > When we use pagination, we get some information in the Response Header about the total amount of pages according to how many items per page we are requesting (using the per_page parameter).
  >
  >So a trick could be requesting the list of contributors with one item per page:
  >
  >https://<i></i>api.github.com/repos/:owner/:repo/contributors?per_page=1
  >doing this in our Response Header there will be a Link property with the following content:
  >
  >Link:https://<i></i>api.github.com/repositories/ID/contributors?per_page=1&page=2; rel="next", https://<i></i>api.github.com/repositories/ID/contributors?per_page=1&page=XXXXXXXX; rel="last"
  >
  >the XXXXXXXX value, just before rel="last" will be the total amount of pages, but since we are requesting one item per page, it will be also the total amount of contributors.
  >
  >[~ShinDarth](https://stackoverflow.com/users/3497671/shindarth)
  
  - Using only this method, developers who committed anonymously will not be counted. For that the _anon_ parameter has to be set to 1.
  
    Full example with Tensorflow:  
    ```
    https://api.github.com/repos/tensorflow/tensorflow/contributors?per_page=1&anon=1
    ```

  - [API rate limit](https://developer.github.com/v3/#rate-limiting): Without authentication the API lets at most 60 requests through an hour. With authentication the limit is increased to
    5000 request/hour. While 60 is not necessarily enough, 5000 should do the trick. For this, a shared GitHub account is required.  
  - **Authentication**: The recommended way is using the [OAuth](https://developer.github.com/v3/oauth_authorizations/#oauth-authorizations-api) protocol. For the time being we are going to use
    some other [authentication method](https://developer.github.com/v3/auth/#other-authentication-methods) for testing purposes, since the app is not yet running.
	It is possible to use both _username:password_ and _username:token_ combinations. Out of the last two, token based authentication should be prioritized, because using that the access scope can be set precisely.  
    The [Requests](http://docs.python-requests.org/en/master/) package supports an _'auth'_ parameter in every kind of request which expects a tuple containing a _usnername_ and a _password_.
  - **Webhooks:** [Webhooks](https://developer.github.com/v3/repos/hooks/) are available through the API and they should be used as a trigger to the script running on the Azure servers to update the database containing the scores for the frameworks.  Authentication is mandatory when using webhooks. 
  	- [List hooks](https://developer.github.com/v3/repos/hooks/#list-hooks): ``` GET /repos/:owner/:repo/hooks```
  	- [Get single hook](https://developer.github.com/v3/repos/hooks/#get-single-hook): ``` GET /repos/:owner/:repo/hooks/:id```
  	- [Create hook](https://developer.github.com/v3/repos/hooks/#create-a-hook): ```POST /repos/:owner/:repo/hooks``` (check link for details)
