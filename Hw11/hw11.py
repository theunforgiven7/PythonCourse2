

class StudentRating:
    """
    Клас який представляє рейтинг групи студентів.
    """
    def __init__(self, student_ratings: list):
        """
        ініціалізує об'єкт класу зі списком рейтингів студентів
        param student_ratings: список з цілих чисел(int)
        """
        self.student_ratings = student_ratings()

    # Get method
    def get_ratings(self):
        """
        Метод повертає поточний список 
        """
        return self.student_ratings

    # Set method
    def set_ratings(self, student_new_ratings):
        """
        Метод повертає оновлений список
        """
        self.student_ratings = student_new_ratings

    # Add method
    def add_rating(self, student_rating):
        """_
        Метод для додавання нового рейтенгу до списку.
        Повертає список із новим значенням
        """
        self.student_ratings.append(student_rating)

    # максимальний рейтинг в групі
    def max_rating(self):
        """
        Метод повертає максимальний рейтинг зі списку
        """
        return max(self.student_ratings)

    # мінімальний рейтинг в групі
    def min_rating(self):
        """
        Метод повертає минимальний рейтинг зі списку
        """
        return min(self.student_ratings)

    # середній рейтинг групи
    def average_rating(self):
        """
        Метод повертає середний рейтинг зі списку
        """
        return sum(self.student_ratings) / len(self.student_ratings)

    # кількість студентів в яких рейтинг вищий за середній
    def high_avg_rating(self):
        """
        Метод повертає кількість студентів в яких рейтинг вищий за середній
        """
        avg = self.average_rating()
        return len([r for r in self.student_ratings if r > avg])

    # кількість студентів в яких рейтинг нижчий за середній
    def low_avg_rating(self):
        """
        Метод повертає кількість студентів в яких рейтинг нижчий за середній
        """
        avg = self.average_rating()
        return len([r for r in self.student_ratings if r < avg])

    # кількість студентів з рейтингом "excellent"
    def st_excellent_count(self):
        """
        Метод повертає кількість студентів з рейтингом "excellent"
        """
        return len([r for r in self.student_ratings if r > 90 or r == 100])

    # кількість студентів з рейтингом "very good"
    def st_verygood_count(self):
        """
        Метод повертає кількість студентів з рейтингом "very good"
        """
        return len([r for r in self.student_ratings if r > 70 and r < 91])

    # кількість студентів з рейтингом "good"
    def st_good_count(self):
        """
        Метод повертає кількість студентів з рейтингом "good"
        """
        return len([r for r in self.student_ratings if r > 59 and r < 71])

    # кількість студентів з рейтингом "satisfactory"
    def st_satisfactory_count(self):
        """
        Метод повертає кількість студентів з рейтингом "satisfactory"
        """
        return len([r for r in self.student_ratings if 0 <= r <= 59])
    
    def __str__(self):
        """
        Метод повертає рядки, рядки - це рейтинги студентів
        """
        return '\n'.join(str(r) for r in self.student_ratings)


