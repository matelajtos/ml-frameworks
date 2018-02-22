from github import Github
import time
from math import sqrt


class MLFramework:
    def __init__(self, full_name):
        repo = Github().get_repo(full_name)

        self.name = repo.name
        self.full_name = repo.full_name
        self.html_url = repo.html_url
        self.api_url = repo.url
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

    def to_json(self):
        return dict(self.__dict__, score=self.score)
