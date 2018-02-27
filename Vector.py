import time


class DictVector:
    def __init__(self, kwargs, update_date=time.asctime()):
        self.update_date = update_date
        self.dict_vector = kwargs

    def __len__(self):
        return int(sum([x ** 2 for x in self.dict_vector.values()]) ** 0.5)
