import requests


# Урок 6.4
"""Класс, в котором получаем одну рандомную шутку по каждой категории"""
class TestOneJokeFromEachCategory:
    url_categories = "https://api.chucknorris.io/jokes/categories"

    """Проверка получения рандомной шутки по каждой категории"""
    def test_get_one_joke_from_each_category(self):
        """Запрос всех категорий"""
        all_categories = requests.get(self.url_categories)

        """Запрос по одной шутке из каждой категории"""
        for category in all_categories.json():
            result = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")

            print(f"Статус код: {result.status_code}")
            assert result.status_code == 200, "Неудача! Запрос вернул ошибку."
            print(f"Ваша шутка: {result.json()}")
            print(f"Успех! Мы получили рандомную шутку по категории - {category}.")
            print("-----------")


randon_joke_in_category = TestOneJokeFromEachCategory()
randon_joke_in_category.test_get_one_joke_from_each_category()
