# import sys, os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'venv/Lib/site-packages')))

import MLFramework
import github
import re
import pymongo

import os
import json


def get_full_name(html_url):
    pattern = r'github.com/([^/]*/[^/]*)'
    user_repo = re.search(pattern, html_url)
    if user_repo:
        return user_repo.group(1)
    else:
        raise RuntimeError("Invalid Github link: " + html_url)

# postreqdata = json.loads(open(os.environ['req']).read())
# project_url = postreqdata['html_url']
# project_fn = get_full_name(project_url)

uri = "mongodb://mlframeworks:R9bKTpQslRY6ta795mcOxHGIbRJemptvERK4afd40Bux2XqSjlvUExjzcSHAdFSD0taVeSDNsUKAKnA6sFutRA==@mlframeworks.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

db = client['admin']
collection = db['test_new_format']

project_list = []

with open("project_links.json", "r") as f:
    project_links = json.load(f)
    for p in project_links:
        print(p)
        project_fn = get_full_name(p.replace("\n", ""))
        repo = github.Github().get_repo(project_fn)
        print(repo.__class__)
        repo = MLFramework.MLFramework(repo)
        print(repo.__class__)
        project_list.append(repo)
        #print(json.dumps(repo, cls=MLFramework.MLFrameworkEncoder, indent=4))

print(project_list)

for p in project_list:
    dct = json.loads(json.dumps(p, cls=MLFramework.MLFrameworkEncoder))
    post_id = collection.insert_one(dct).inserted_id
# #
# response = open(os.environ['res'], 'w')
# response.write(repo.to_json())
# response.close()
