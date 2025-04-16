import requests

BASE_URL_1 = "http://127.0.0.1:8080/service/accidents"


def test_get_accidence():
    # Отправляем GET-запрос к конечной точке /api/result
    response = requests.get(BASE_URL_1)
    # Проверяем, что код статуса ответа равен 200 (ОК)
    assert response.status_code == 200
    # Проверяем, что тело ответа содержит список пользователей
    result = response.json()
    assert isinstance(result, list)
    assert len(result) > 0
    # Проверяем структуру первого пользователя в списке
    first_user = result[0]
    assert "damage_description" in first_user
    assert "date" in first_user
    assert "plate_num_cars" in first_user
    assert "id" in first_user
    assert "id_car" in first_user


BASE_URL_2 = "http://127.0.0.1:8080/service/cars"


def test_get_cars_and_accidence():
    # Отправляем GET-запрос к конечной точке /api/result
    response = requests.get(BASE_URL_2)
    # Проверяем, что код статуса ответа равен 200 (ОК)
    assert response.status_code == 200
    # Проверяем, что тело ответа содержит список пользователей
    results = response.json()
    assert isinstance(results, list)
    assert len(results) > 0
    # Проверяем структуру первого пользователя в списке
    for result in results:
        for first in result["accidents"]:
            assert "damage_description" in first
            assert "date" in first
            assert "plate_num_cars" in first
            assert "id" in first
            assert "id_car" in first

        second = result['car']
        assert "model" in second
        assert "year" in second
        assert "plate_number" in second
        assert "id" in second
        assert "car_type" in second
        assert "color" in second


id = 10
BASE_URL_3 = f"http://127.0.0.1:8080/service/cars/{id}"


def test_get_cars_and_accident_by_id():
    # Отправляем GET-запрос к конечной точке /api/results
    response = requests.get(BASE_URL_3)
    # Проверяем, что код статуса ответа равен 200 (ОК)
    assert response.status_code == 200
    # Проверяем, что тело ответа содержит список пользователей
    results = response.json()
    assert isinstance(results, dict)
    assert len(results) > 0
    # Проверяем структуру первого пользователя в списке
    for i in results["accidents"]:
        first = i
        assert "damage_description" in first
        assert "date" in first
        assert "plate_num_cars" in first
        assert "id" in first
        assert "id_car" in first

    second = results['car']
    assert "model" in second
    assert "year" in second
    assert "plate_number" in second
    assert "id" in second
    assert "car_type" in second
    assert "color" in second


id = 1
BASE_URL_4 = f"http://127.0.0.1:8080/service/accidents/{id}"


def test_get_accident_by_id():
    # Отправляем GET-запрос к конечной точке /api/results
    response = requests.get(BASE_URL_3)
    # Проверяем, что код статуса ответа равен 200 (ОК)
    assert response.status_code == 200
    # Проверяем, что тело ответа содержит список пользователей
    results = response.json()
    assert isinstance(results, dict)
    assert len(results) > 0
    # Проверяем структуру первого пользователя в списке
    for first in results["accidents"]:
        assert "damage_description" in first
        assert "date" in first
        assert "plate_num_cars" in first
        assert "id" in first
        assert "id_car" in first


BASE_URL5 = "http://127.0.0.1:8080/service/cars"
def test_post_add_car():
    # Корректные данные
    test_data = {
        "model": "Tesla Model S",
        "year": 2022,
        "color": "Red",
        "plate_number": "а123ск",
        "car_type": "Sedan"
    }

    # Отправка POST-запроса
    response = requests.post(BASE_URL5, json=test_data)

    # Проверка статус кода (200 OK)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    # Проверка текстового ответа
    assert response.text == "OK", f"Ожидался 'OK', получено: {response.text}"




BASE_URL6 = "http://127.0.0.1:8080/service/accident"
def test_post_add_accident():
    # Корректные данные
    test_data = {
        "damage_description": "Смяты бока, двигатель внутри салона",
        "date": "2022-10-05",
        "plate_num_cars": "а123ск",
        "plate_number": "х011ке"
    }

    # Отправка POST-запроса
    response = requests.post(BASE_URL6, json=test_data)

    # Проверка статус кода (200 OK)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    # Проверка текстового ответа
    assert response.text == "OK", f"Ожидался 'OK', получено: {response.text}"






