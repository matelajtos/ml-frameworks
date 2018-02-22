import json
import MLFramework
import github
import re

def get_full_name(html_url):
    pattern = r'github.com/([^/]*/[^/]*)'
    user_repo = re.search(pattern, html_url)
    if user_repo:
        return user_repo.group(1)
    else:
        raise RuntimeError("Invalid Github link: " + html_url)

project_url = "https://github.com/tensorflow/tensorflow"
project_fn = get_full_name(project_url)
repo = github.Github().get_repo(project_fn)
repo.__class__ = MLFramework.MLFramework
print(json.dumps(repo.to_json(), indent=4))