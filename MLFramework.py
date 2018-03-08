import github
import ExtPaginatedList
import copy
import json
import DictVector


class MLFramework(github.Repository.Repository):
    def __new__(cls, other):
        if isinstance(other, github.Repository.Repository):
            other = copy.copy(other)
            other.__class__ = MLFramework
            return other
        return object.__new__(cls)

    def __init__(self, _):
        v = {
             "stars_count": self.stargazers_count,
             "watchers_count": self.subscribers_count,
             "forks_count": self.forks_count,
             "contributors_count": self.contributors_count
            }
        self.vector = DictVector.DictVector(v)

    @property
    def contributors_count(self, anon=1):
        assert anon in (0, 1), anon

        contributors_list = ExtPaginatedList.ExtPaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.contributors_url,
            {'per_page': 1, 'anon': anon})
        return contributors_list.last_page_number

    def to_dict(self):
        ml = dict(name=self.name,
                  full_name=self.full_name,
                  html_url=self.html_url,
                  api_url=self.url,
                  vectors=[self.vector.to_dict()]
                  )
        return ml
