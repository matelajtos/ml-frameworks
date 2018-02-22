import github

class ExtPaginatedList(github.PaginatedList.PaginatedList):
    @property
    def last_page_number(self):
        last_url = self._getLastPageUrl()
        page = last_url.find('&page=')
        return int(last_url[page + 6:])