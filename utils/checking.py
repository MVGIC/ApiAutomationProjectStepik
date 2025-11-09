

class Checking:
    """Методы для проверки ответов наших запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""

        assert result.status_code == status_code, "Ошибка! Статус код отличается от ожидаемого."

    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""

        fields = result.json()
        assert list(fields) == expected_value, "Ошибка!  Список полей не совпадает"
        print(list(fields))
        print("Все поля присутствуют")

    @staticmethod
    def check_json_values(result, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Ошибка, значение поля не совпадает"
        print(f"{field_name} верно!")

    @staticmethod
    def check_json_search_word_in_values(result, field_name, searched_word):
        """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert searched_word in check_info
        print(f"Слово {searched_word} присутствует!")
