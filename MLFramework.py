import github
import ExtPaginatedList
import copy
import json
from DictVector import DictVector


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
        self.vector = [DictVector(v)]

    @property
    def contributors_count(self, anon=1):
        assert anon in (0, 1), anon

        contributors_list = ExtPaginatedList.ExtPaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.contributors_url,
            {'per_page': 1, 'anon': anon})
        return contributors_list.last_page_number


class MLFrameworkEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MLFramework):
            ml = dict(name=o.name,
                      full_name=o.full_name,
                      html_url=o.html_url,
                      api_url=o.url,
                      vectors=[
                          dict(update_date=o.vector.update_date,
                               dict_vector=o.vector.dict_vector,
                               score=len(o.vector))
                               ]
                      )
            return ml
        else:
            return json.JSONEncoder.default(self, o)
