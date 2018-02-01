import requests
import re
import time
from math import sqrt


def get_response(api_link):        
    return requests.get(api_link)
    
def get_contributor_count(api_link):
        contributor_link = api_link + "/contributors"
        payload = {"per_page": 1, "anon": 1}
        response = requests.get(contributor_link, params=payload).headers["Link"]

        pattern = r'(\d+)>; rel="last"'
        contributors = re.search(pattern, response)

        if contributors:
            return int(contributors.group(1))
        else:
            raise MLFramework.ContributorCountException("Contributor count has not been found. " 
                                                        "Link: " + contributor_link)

class MLFramework:
    def __init__(self, link):
        self.link = link.replace("\n", "")
        self.api_link = self.create_api_link()
        
        response = get_response(self.api_link)
        content = response.json()
        if response.headers["status"] == "404 Not Found":
            raise MLFramework.URLNotFoundException("URL: '" + self.api_link + "' was not found. (404)")
        elif response.headers["status"] == "403 Forbidden":
            raise MLFramework.RateLimitReachedException("GitHub didn't like that. Here's the error message: "
                                                        + content["message"])
        elif response.headers["status"] != "200 OK":
            raise MLFramework.GitHubException("There was a problem contacting github.com. Response status: "
                                              + response.headers["status"])

        self.name = content["name"]
        self.star_count = content["stargazers_count"]
        self.watch_count = content["subscribers_count"]
        self.fork_count = content["forks_count"]
        self.contributor_count = get_contributor_count(self.api_link)        
        self.lic = content["license"]['name']
        self.update_date = time.asctime()

    @property
    def score(self):
        vector_length = sqrt(self.star_count**2
                             + self.watch_count**2
                             + self.fork_count**2
                             + self.contributor_count**2)
        return int(vector_length)
    
    
    def create_api_link(self):
        pattern = r'github.com/([^/]*/[^/]*)'
        user_repo = re.search(pattern, self.link)
        if user_repo:
            return "http://api.github.com/repos/" + user_repo.group(1)
        else:
            raise MLFramework.InvalidLinkException("Invalid Github link: " + self.link)
        
    def __lt__(self, other):
        return True if self.score < other.score else False

    def __str__(self):
        return ("Name: " + self.name + "\n"
                "Link: " + self.link + "\n"
                "API link: " + self.api_link + "\n"
                "Stats: \t{\n"  + "\t  stars: " + str(self.star_count) + "\n"
                                + "\t  watch: " + str(self.watch_count) + "\n"
                                + "\t  forks: " + str(self.fork_count) + "\n"
                                + "\t  contributors: " + str(self.contributor_count) + "\n\t}\n"
                "License: " + self.lic + "\n"
                "\nVector length: " + str(self.score))

    def to_json(self):
        return dict(self.__dict__, score=self.score)

    class MLException(Exception):
        """Base class for exceptions in MLFramework class"""
        pass

    class URLNotFoundException(MLException):
        pass

    class RateLimitReachedException(MLException):
        pass

    class GitHubException(MLException):
        pass

    class InvalidLinkException(MLException):
        pass

    class ContributorCountException(MLException):
        pass


if __name__ == "__main__":
    import json
    project_list = []
    with open('project_links', 'r')  as f:
        for line in f:
            project_list.append(MLFramework(line))

    project_list = sorted(project_list, reverse=True)
    print(json.dumps([x.to_json() for x in project_list], indent=4))

