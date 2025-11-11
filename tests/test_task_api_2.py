import requests


# Урок 6.5
class TestOneJokeFromSelectedCategory:
    """Класс, в котором получаем одну рандомную шутку по выбранной категории"""

    url_categories = "https://api.chucknorris.io/jokes/categories"

    def test_get_one_joke_from_selected_category(self):
        """Проверка получения рандомной шутки по выбранной категории"""
        category = input("Введите желаемую категорию шутки: ")
        all_categories = requests.get(self.url_categories)
        while category not in all_categories.json():
            print("Выбранной категории не существует. Пожалуйста, укажите другую.")
            category = input("Введите желаемую категорию шутки: ")

        print("Успех! Указанная категория существует.")

        """Получаем рандомную шутку по выбранной категории"""
        result = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}").json()
        desired_joke = result["value"]
        print(f"Ваша шутка: {desired_joke}")


selected_category_joke = TestOneJokeFromSelectedCategory()
selected_category_joke.test_get_one_joke_from_selected_category()
