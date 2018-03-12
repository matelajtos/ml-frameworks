# import sys, os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'venv/Lib/site-packages')))

import MLFramework
import github
import re
import pymongo
import DictVector
import os
import json


def get_full_name(html_url):
    pattern = r'github.com/([^/]*/[^/]*)'
    user_repo = re.search(pattern, html_url)
    if user_repo:
        return user_repo.group(1)
    else:
        raise RuntimeError("Invalid Github link: " + html_url)
#
# postreqdata = json.loads(open(os.environ['req']).read())
# project_url = postreqdata['html_url']
# project_fn = get_full_name(project_url)

uri = "mongodb://mlframeworks:R9bKTpQslRY6ta795mcOxHGIbRJemptvERK4afd40Bux2XqSjlvUExjzcSHAdFSD0taVeSDNsUKAKnA6sFutRA==@mlframeworks.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

db = client['admin']
collection = db['asd']

project_list = []
g = github.Github()
with open("project_links.json", "r") as f:
    project_links = json.load(f)
    for p in project_links:
        project_fn = get_full_name(p)
        repo = g.get_repo(project_fn)
        repo = MLFramework.MLFramework(repo)
        project_list.append(repo)
        break

print(project_list)

for p in project_list:
    result = collection.update_one({"full_name": p.full_name}, {"$push": {"vectors": p.vector.to_dict()}})
    if result.modified_count == 0:
        post_id = collection.insert_one(p.to_dict()).inserted_id

    break

# response = open(os.environ['res'], 'w')
# response.close()
