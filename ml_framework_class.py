import requests
import re
import time
from math import sqrt


class Git:
    def __init__(self, link):
        self.link = link.replace("\n", "")
        self.api_link = self.get_api_link()
        
        response = requests.get(self.api_link).json()
        
        self.name = response["name"]
        self.stars = response["stargazers_count"]
        self.watch = response["subscribers_count"]
        self.forks = response["forks_count"]
        self.contributors = self.get_contributors()        
        self.lic = response["license"]['name']
        self.update_date = time.asctime()

    @property
    def value(self):
        vector_length = sqrt(self.stars**2
                             + self.watch**2
                             + self.forks**2
                             + self.contributors**2)
        return int(vector_length)
    
    def get_contributors(self):
        contributor_link = self.api_link + "/contributors?per_page=1&anon=1"
        response = requests.get(contributor_link).headers["Link"]

        pattern = r'(\d+)>; rel="last"'
        contributors = re.search(pattern, response)

        if contributors:
            return int(contributors.group(1))
        else:
            raise RuntimeError("Contributors have not been found.")  

    def get_api_link(self):
        pattern = r'github.com/([^/]*/[^/]*)'
        user_repo = re.search(pattern, self.link)
        if user_repo:
            return "http://api.github.com/repos/" + user_repo.group(1)
        else:
            raise RuntimeError("Invalid Github link.")

    def __lt__(self, other):
        return (True if self.value < other.value else False)

    def __str__(self):
        return ("Name: " + self.name + "\n"
                "Link: " + self.link + "\n"
                "API link: " + self.api_link + "\n"
                "Stats: \t{\n"  + "\t  stars: " + str(self.stars) + "\n"
                                + "\t  watch: " + str(self.watch) + "\n"
                                + "\t  forks: " + str(self.forks) + "\n"
                                + "\t  contributors: " + str(self.contributors) + "\n\t}\n"
                "License: " + self.license + "\n"
                "\nVector length: " + str(self.value))

    def toJSON(self):
        return dict(self.__dict__, value=self.value)


if __name__ == "__main__":
    import json
    project_list = []
    with open('project_links', 'r')  as f:
        for line in f:
            project_list.append(Git(line))

    project_list = sorted(project_list, reverse=True)
    print(json.dumps([x.toJSON() for x in project_list], indent=4))
        
    
