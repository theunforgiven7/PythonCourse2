from datetime import datetime

def sort_func_train():
    



class Train:
    def _init_(self, item, num_train, date_t):
        self.item = item
        self.num_train = num_train
        self.date_t = date_t
        if date_t < datetime.now():
            return ('date_t не може бути меньшим за поточний час')
