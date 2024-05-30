from datetime import datetime





class Train:
    def _init_(self, item: int, num_train: int, date_t: int):
        self.item = item
        self.num_train = num_train
        self.date_t = date_t
        if date_t < datetime.now():
            return ('date_t не може бути меньшим за поточний час')

    def sort_func_train(num_train):
        return sorted(num_train, key=lambda train: (train.destination, train.time))
