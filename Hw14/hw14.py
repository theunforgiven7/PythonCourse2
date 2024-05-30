from datetime import datetime


def sort_func_train(trains_lst):
    return sorted(trains_lst, key=lambda t: (t.item, t.date_t))


class Train:
    def __init__(self, item: int, num_train: int, date_t: datetime):
        self.item = item
        self.num_train = num_train
        if date_t < datetime.now():
            print('date_t не може бути меньшим за поточний час')
            self.date_t = datetime.now()
        else:
            self.date_t = date_t
