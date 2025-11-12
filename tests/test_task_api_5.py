import requests


# Урок 8.10
def test_get_dart_friends():
    """Получаем 'друзей-коллег' Дарта Вейдера, которые снимались с ним в одних фильмах"""

    url = "https://swapi.dev/api/people/4/"

    response = requests.get(url) # Получаем информацию о Дарте Вейдере
    print(response.status_code)
    info_dart = response.json()
    print(info_dart)
    dart_films = info_dart.get("films") # Получаем фильмы, в которых снимался Дарт Вейдер
    print(dart_films)

    """Открываем файл на запись и записываем имена персонажей"""
    with open("task_5_file.txt", "w", encoding="utf-8") as f:
        characters_list = []
        for i in dart_films:
            response_film = requests.get(i) # Отправляем запрос по каждому фильму, в котором снимался Дарт Вейдер
            film_characters = response_film.json().get("characters") # Получаем всех персонажей фильмов, в которых снимался Дарт Вейдер
            for j in film_characters:
                response_name = requests.get(j) # Отправляем запрос по каждому персонажу из фильмов, в которых снимался Дарт Вейдер
                character_name = response_name.json().get("name") # Получаем имена персонажей, которые снимались в тех же фильмах, что и Дарт Вейдер
                characters_list.append(character_name)
                unique_names = set(characters_list) # Оставляем только уникальные значения имен

        for name in unique_names:
            f.write(f"{name}\n") # Записываем уникальные имена в файл

    """Открываем файл на чтение и выводим имена персонажей из файла""" # Если необходимо
    with open("task_5_file.txt", "r") as f_r:
        result_read = f_r.read()
        print(result_read)
