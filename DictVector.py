import time
import json


class DictVector:
    def __init__(self, dict_vector, update_date=time.asctime()):
        self.update_date = update_date
        self.dict_vector = dict_vector

    def __len__(self):
        return int(sum([x ** 2 for x in self.dict_vector.values()]) ** 0.5)

    def to_dict(self):
        return dict(update_date=self.update_date, score=len(self), dict_vector=self.dict_vector)
