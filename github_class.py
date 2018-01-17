import urllib.request
import json
from math import sqrt


class Git:
    def __init__(self, name, link):
        self.name = name 
        self.link = link
        self.stats = {'stars': 0, 'forks': 0, 'watch': 0, 'conts': 0}
        self.license = None
        self.get_info()
        
    def get_info(self):
        # r = requests.get(link)
        with open('api.json', 'r') as f:
            respond = json.load(f)


        self.stats['stars'] = int(respond['stargazers_count'])
        self.stats['watch'] = int(respond['subscribers_count'])
        self.stats['forks'] = int(respond['forks_count'])

        conts = ''
        with open('tensorflow.html', 'r') as f:
            for i, row in enumerate(f):
                if row.find('graphs/contributors') != -1: 
                    f.seek(0)
                    conts = f.readlines()[i+3]
        self.stats['conts'] = int(conts.replace(',', ''))

        self.license = respond['license']['name']
        

    @property
    def value(self):
        vector_length = sqrt(self.stats['stars']**2
                             + self.stats['watch']**2
                             + self.stats['forks']**2
                             + self.stats['conts']**2)
        

        return int(vector_length)


    def __str__(self):
        return ("Name: " + self.name + "\n"
                "Link: " + self.link + "\n"
                "Stats: " + str(self.stats) + "\n"
                "License" + self.license + "\n")

    
if __name__ == "__main__":
    tensor = Git('Tensorflow', 'https://github.com/tensorflow/tensorflow')
    tensor.get_info()
    print(tensor.value)
    print(tensor)
