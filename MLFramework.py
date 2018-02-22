import github
import ExtPaginatedList
import time
import copy
import json


class MLFramework(github.Repository.Repository):
    def __new__(cls, other):
        if isinstance(other, github.Repository.Repository):
            other = copy.copy(other)
            other.__class__ = MLFramework
            return other
        return object.__new__(cls)

    def __init__(self, other):
        pass

    @property
    def contributors_count(self, anon=1):
        assert anon in (0, 1), anon

        contributors_list = ExtPaginatedList.ExtPaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.contributors_url,
            {'per_page': 1, 'anon': anon})
        return contributors_list.last_page_number

    @property
    def score(self):
        vector = [self.stargazers_count, self.subscribers_count, self.forks_count, self.contributors_count]
        return int(sum((x**2 for x in vector))**0.5)

    def to_dict(self):
        return dict(name = self.name,
                    full_name = self.full_name,
                    html_url = self.html_url,
                    api_url = self.url,
                    stars_count = self.stargazers_count,
                    watchers_count = self.subscribers_count,
                    forks_count = self.forks_count,
                    contributors_count = self.contributors_count,
                    update_date = time.asctime(),
                    score=self.score
                    )

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)