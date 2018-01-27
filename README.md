# ML framework rating tool

This project's goal is to provide an objective way of comparing [GitHub](https://github.com/) machine learning libraries based on their community size.


### Main goals

  - Collect all of the most important machine learning libraries that are available on GitHub.
  - Calculate a score for each one based on the statistics (stars, watch, forks, contributors).
  - Display them descending order in a visually pleasing manner.
  - Keep track of tendencies and be able to predict future alterations in popularity.
  - Move the project to Microsoft Azure, where score updates would happen on some trigger.
  
Some more that we want to achieve later:
  - Finer scoring system.
  - Grouping by types of ML.


### The formula
The following formula gives the basis of comparison:

<p align="center">

<img src="https://raw.githubusercontent.com/maraid/md_test/master/formula.png"/>

</p>

Which basically represents the length of a vector in a 4 dimensional space, where the dimensions are the stats. This makes it easy to compare the different repositories.  
After having calculated all of the needed vector lengths, normalized score can be computed that gives more of a comprehensible rank.

### Tech

The tool uses a number of different projects to work properly:

  - [Python 3.6](https://www.python.org/) - Python programming language.
  - [GitHub API](https://developer.github.com/v3/) - GitHub's API. Used to access stats.
  - [Google Sheets API](https://developers.google.com/sheets/api/v3/) - Creating quick and easy Google spreadsheets. Temporary solution for display.
  - [D3.js](https://d3js.org/) - Other, more sustainable solution for data visualization.
  - [Azure serverless](https://azure.microsoft.com/en-in/overview/serverless-computing/) - Azure cloud where the script will be running.
  - [Some database](#) - Storing the values with dates on Azure servers. (Undecided so far)

### Python packages
  - Maybe list them. Unimportant.
  
### Architecture

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
	It is possible to use both _username:password_ and _username:token_ combinations. Out of the last two, token based authentication should be prioritized, because
	using that the access scope can be set precisely.
  - **Webhooks:** [Webhooks](https://developer.github.com/v3/repos/hooks/) are available through the API and they should be used as a trigger to the script running on the Azure servers. 
