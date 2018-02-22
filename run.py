# import sys, os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'venv/Lib/site-packages')))

import MLFramework
import github
import re

import os
import json


def get_full_name(html_url):
    pattern = r'github.com/([^/]*/[^/]*)'
    user_repo = re.search(pattern, html_url)
    if user_repo:
        return user_repo.group(1)
    else:
        raise RuntimeError("Invalid Github link: " + html_url)

postreqdata = json.loads(open(os.environ['req']).read())
project_url = postreqdata['html_url']
project_fn = get_full_name(project_url)
# project_fn = get_full_name('https://github.com/tensorflow/tensorflow')
repo = github.Github().get_repo(project_fn)
repo = MLFramework.MLFramework(repo)

response = open(os.environ['res'], 'w')
response.write(repo.to_json())
response.close()