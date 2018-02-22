import github
import ExtPaginatedList
import time
from math import sqrt


class MLFramework(github.Repository.Repository):
    @property
    def contributors_count(self, anon=1):
        assert anon in (0, 1), anon

        contributors_list = github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.contributors_url,
            {'per_page': 1, 'anon': anon})
        contributors_list.__class__ = ExtPaginatedList.ExtPaginatedList
        return contributors_list.last_page_number

    @property
    def score(self):
        vector_length = sqrt(self.stargazers_count**2
                             + self.subscribers_count**2
                             + self.forks_count**2
                             + self.contributors_count**2)
        return int(vector_length)

    def to_json(self):
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
