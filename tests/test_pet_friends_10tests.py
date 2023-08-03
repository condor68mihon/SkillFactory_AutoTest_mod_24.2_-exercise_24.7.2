from api import PetFriends
from settings import valid_password, valid_email
import os

pf = PetFriends()

#10 позитивных и негативных тестов

def test_get_api_key_for_invalid_user(email=valid_email.capitalize(), password=valid_password.capitalize()):
    """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""
    status, result = pf.get_key(email, password)
    assert status != 200
    assert 'key' not in result


def test_get_api_key_for_incorrect_login_user(email=valid_email.upper(), password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""
    """баг, позволяет зайти"""
    status, result = pf.get_key(email, password)
    assert status != 200
    assert 'key' not in result


def test_get_api_key_for_incorrect_password_user(email=valid_email, password=valid_password.upper()):
    """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""
    status, result = pf.get_key(email, password)
    assert status != 200
    assert 'key' not in result


def test_get_pets_with_empty_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает ошибку 403.
         Используя пустой ключ запрашиваем список всех питомцев.
        Доступное значение параметра filter - 'my_pets' либо '' """
    auth_key = {"key": ""}
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200


def test_successful_add_pet_without_photo_RUS(name="Гав", animal_type="котенок", age=1):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    _, auth_key = pf.get_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_successful_add_pet_without_photo_ENG(name="Jim", animal_type="hamster", age=4):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    _, auth_key = pf.get_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_unsuccessful_add_pet_without_photo(name="", animal_type="", age=None):
    """Проверяем что нельзя добавить питомца с пустыми данными без фото"""

    _, auth_key = pf.get_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status != 200


def test_successful_add_photo_for_pet(pet_photo = 'images/dog.jpg'):
    """Проверяем что можно добавить фото для существующего питомца"""

    _, auth_key = pf.get_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']

    if len(my_pets['pets']) > 0:

        status, result = pf.add_photo_for_pet(auth_key, pet_id, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_unsuccessful_delete_someones_pet():
    """Проверяем возможность удаления питомца чужого питомца из всех питомцев"""
    """Баг удаляется чужой питомец"""
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(all_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Superdog", "dog", "4", "images/dog.jpg")
        _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = all_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status != 200
    assert pet_id not in all_pets.values()


def test_unsuccessful_update_someone_else_pet_info(name='Каштанка', animal_type='лошадь', age=9):
    """Проверяем возможность обновления информации о чужом питомце"""
    """Баг, меняются данные питомцев дргих пользователей"""
        # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(all_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)

            # Проверяем что статус ответа = 400 и имя питомца соответствует заданному
        assert status != 200
    else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no  pets")
