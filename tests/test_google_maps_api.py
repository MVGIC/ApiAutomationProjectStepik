import allure

from utils.api import GoogleMapsApi
from utils.checking import Checking

@allure.epic("Класс создает новую локацию")
class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""

    @allure.description("Создание, изменение и удаление новой локации")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # Вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # Получение place_id для метода GET
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_values(result_post, "status", "OK")

        print("Метод GET для проверки создания")
        result_get = GoogleMapsApi.get_new_place(place_id)  # Отправка метода GET
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_values(result_get, "address", "29, side layout, cohen 09")

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # Изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ["msg"])
        Checking.check_json_values(result_put, "msg", "Address successfully updated")

        print("Метод GET для проверки изменения")
        result_get = GoogleMapsApi.get_new_place(place_id)  # Отправка метода GET
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_values(result_get, "address", "100 Lenina street, RU")

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # Удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ["status"])
        Checking.check_json_values(result_delete, "status", "OK")

        print("Метод GET для проверки удаления локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # Отправка метода GET
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ["msg"])
        Checking.check_json_search_word_in_values(result_get, "msg", "failed")

        print("Тестирование создания, изменения и удаления новой локации прошло успешно")
