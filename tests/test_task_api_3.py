import requests


# Урок 6.9
class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # Базовый url
        key = "?key=qaclick123"  # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        post_url = base_url + post_resource + key  # URL создания локации
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
        with open("task_3_file.txt", "w") as f:
            for _ in range(5):
                result_post = requests.post(post_url, json=json_new_location)  # Создаем локацию
                check_response_post = result_post.json()
                place_id = check_response_post.get("place_id")  # Получаем place_id локации
                f.write(f"{place_id}\n")

        """Считываем сохраненные place_id из файла и проверяем, что локации с данными place_id существуют"""
        with open("task_3_file.txt", "r") as f_r:
            for place_id in f_r.readlines():
                new_place_id = place_id.replace("\n", "")  # Избавляемся от переноса строки в файле
                get_resource = "/maps/api/place/get/json"  # Ресурс метода Get
                get_url = base_url + get_resource + key + "&place_id=" + new_place_id  # URL получения локации
                print(get_url)
                result_get = requests.get(get_url)
                assert result_get.status_code == 200
                check_response_get = result_get.json()  # Содержимое локации
                print(check_response_get)
                address = check_response_get.get(
                    "address")  # Получаем адрес из локации, чтобы тем самым убедиться, что локация существует, как и place_id
                assert address == "29, side layout, cohen 09"
                print(f"Успех! Локация с place_id: {new_place_id} существует.")


new_place = TestNewLocation()
new_place.test_create_new_location()
