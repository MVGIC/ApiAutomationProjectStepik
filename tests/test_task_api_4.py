import requests


# Урок 6.10
class TestNewLocation:
    """Работа с новой локацией"""
    base_url = "https://rahulshettyacademy.com"  # Базовый url
    key = "?key=qaclick123"  # Параметр для всех запросов

    def test_create_new_location(self):
        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        post_url = self.base_url + post_resource + self.key  # URL создания локации
        print(post_url)

        json_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        """Создаем файл, 5 локаций и записываем в файл 5 place_id от созданных локаций"""
        with open("task_4_file_all.txt", "w") as f:
            for _ in range(5):
                result_post = requests.post(post_url, json=json_new_location)  # Создаем локацию
                check_response_post = result_post.json()
                place_id = check_response_post.get("place_id")  # Получаем place_id локации
                f.write(f"{place_id}\n")

    def test_delete_new_location(self):
        """Удаление локации с place_id, относящихся к чётным строкам, из первого файла"""

        with open("task_4_file_all.txt", "r") as f_r:
            for i, place_id in enumerate(f_r, 1):
                if i % 2 == 0:
                    new_place_id = place_id.replace("\n", "")  # Избавляемся от переноса строки в файле
                    delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Delete

                    delete_url = self.base_url + delete_resource + self.key  # URL удаления локации
                    print(delete_url)

                    json_for_delete_new_location = {
                        "place_id": new_place_id
                    }

                    result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
                    print(result_delete.text)  # Тело ответа после удаления локации
                    print(f"Статус код: {result_delete.status_code}")
                    assert result_delete.status_code == 200, "Неудача! Запрос вернул ошибку."
                    print("Успешно! Удаление локации прошло успешно.")

        """Проверка удаления c place_id, относящихся к чётным строкам, из первого файла"""
        with open("task_4_file_all.txt", "r") as f_r, open("task_4_file_remaining.txt",
                                                "w") as new_f:  # Открываем первый файл на чтение и сразу создаем второй, в который записываем неудаленные локации
            for place_id in f_r.readlines():
                new_place_id = place_id.replace("\n", "")  # Избавляемся от переноса строки в файле
                get_resource = "/maps/api/place/get/json"  # Ресурс метода Get
                get_url = self.base_url + get_resource + self.key + "&place_id=" + new_place_id  # URL получения локации
                print(f"Проверка локации: {get_url}")

                result_get = requests.get(get_url)
                print(result_get.text)
                print(f"Статус код: {result_get.status_code}")
                if result_get.status_code == 200:  # Если локация существует, то запишем её в новый файл
                    new_f.write(f"{new_place_id}\n")
                    print("Локация существует")
                else:
                    print("Локация не существует")


new_place = TestNewLocation()
new_place.test_create_new_location()
new_place.test_delete_new_location()
