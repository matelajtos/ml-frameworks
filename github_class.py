import requests
import json
import re
import time
import csv
from math import sqrt


class Git:
    def __init__(self, name, link):
        self.name = name 
        self.link = link
        self.api_link = self.get_api_link()
        self.stars = 0
        self.watch = 0
        self.forks = 0
        self.conts = 0
        self.license = None
        
        self.get_info()
        
    def get_info(self):
        r = requests.get(self.api_link).text
        respond = json.loads(r)
	
        self.stars = int(respond['stargazers_count'])
        self.watch = int(respond['subscribers_count'])
        self.forks = int(respond['forks_count'])


        # külön függvény
        conts = ''
        
        f = requests.get(self.link).text.split("\n")
        for i, row in enumerate(f):
            if row.find('graphs/contributors') != -1: 
                conts = f[i+3]
        self.conts = int(conts.replace(',', ''))

        self.license = respond['license']['name']

        
        
    def get_api_link(self):
        wo_http=self.link.split("//")
        
        pattern = re.compile("github.com/.*/.*")
        wo_http=wo_http[0] if len(wo_http) == 1 else wo_http[1]
        if pattern.match(wo_http):
            s = wo_http.split("/")
            return "http://api.github.com/repos/" + s[-2] + "/" + s[-1]
        else:
            raise RuntimeError("Invalid Github link.")

        return -1
        
    
    @property
    def value(self):
        vector_length = sqrt(self.stars**2
                             + self.watch**2
                             + self.forks**2
                             + self.conts**2)
        return int(vector_length)


    def __str__(self):
        return ("Name: " + self.name + "\n"
                "Link: " + self.link + "\n"
                "Stats: \t{\n"  + "\t  stars: " + str(self.stars) + "\n"
                                + "\t  watch: " + str(self.watch) + "\n"
                                + "\t  forks: " + str(self.forks) + "\n"
                                + "\t  contributors: " + str(self.conts) + "\n\t}\n"
                "License: " + self.license + "\n"
                "\nVector length: " + str(self.value))

    
if __name__ == "__main__":
    tensor = Git('Tensorflow', 'http://github.com/tensorflow/tensorflow')
    
    print(tensor)
