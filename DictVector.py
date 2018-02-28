import time


class DictVector:
    def __init__(self, dict_vektor, update_date=time.asctime()):
        self.update_date = update_date
        self.dict_vector = dict_vektor

    def __len__(self):
        return int(sum([x ** 2 for x in self.dict_vector.values()]) ** 0.5)
