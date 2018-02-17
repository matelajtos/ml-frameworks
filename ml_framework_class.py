from github import Github
import time
import re
from math import sqrt


class MLFramework:
    def __init__(self, link):
        self.html_url = link.replace("\n", "")
        self.full_name = self.get_full_name()
        
        gh = Github()
        repo = gh.get_repo(self.full_name)

        self.api_url = repo.url
        self.name = repo.name
        self.stars_count = repo.stargazers_count
        self.watchers_count = repo.subscribers_count
        self.forks_count = repo.forks_count
        self.contributors_count = repo.get_contributors_count()
        self.update_date = time.asctime()

    @property
    def score(self):
        vector_length = sqrt(self.stars_count**2
                             + self.watchers_count**2
                             + self.forks_count**2
                             + self.contributors_count**2)
        return int(vector_length)

    def get_full_name(self):
        pattern = r'github.com/([^/]*/[^/]*)'
        user_repo = re.search(pattern, self.html_url)
        if user_repo:
            return user_repo.group(1)
        else:
            raise MLFramework.InvalidLinkException("Invalid Github link: " + self.html_url)

    def __lt__(self, other):
        return True if self.score < other.score else False

    def to_json(self):
        return dict(self.__dict__, score=self.score)

    class MLException(Exception):
        """Base class for exceptions in MLFramework class"""
        pass

    class InvalidLinkException(MLException):
        pass


if __name__ == "__main__":
    import json
    project_list = []
    with open('project_links', 'r')  as f:
        for line in f:
            project_list.append(MLFramework(line))

    project_list = sorted(project_list, reverse=True)
    print(json.dumps([x.to_json() for x in project_list], indent=4))

