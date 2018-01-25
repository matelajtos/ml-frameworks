import requests
import json
import re
import time
import csv
from math import sqrt


class Git:
    def __init__(self, link, api_link=None, name=None, stars=None, watch=None, forks=None, contributors=None, lic=None, update_date=None):
        self.link = link.replace("\n", "")

        self.api_link = (self.get_api_link() if not api_link else api_link)
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
        contributors = ''
        f = requests.get(self.link).text.split("\n")
        for i, row in enumerate(f):
            if row.find('graphs/contributors') != -1: 
                contributors = f[i+3]

        contributors = contributors.replace(',', '')
        return int(contributors)

        
        
    def get_api_link(self):
        wo_http=self.link.split("//")
        pattern = re.compile("github.com/.*/.*")
        wo_http=(wo_http[0] if len(wo_http) == 1 else wo_http[1])
        if pattern.match(wo_http):
            s = wo_http.split("/")
            return "http://api.github.com/repos/" + s[-2] + "/" + s[-1]
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
    project_list = []
    with open('project_links', 'r')  as f:
        for line in f:
            project_list.append(Git(line))

    project_list = sorted(project_list, reverse=True)
    with open("sorted.json", "w") as f:
        f.write(json.dumps([x.toJSON() for x in project_list], indent=4))
        
    
