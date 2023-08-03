# SkillFactory_AutoTest_mod_24.2_-exercise_24.7.2
Модуль 24. Тестовый фреймворк Pytest и автотесты для REST API

Библиотека с реализацией основных методов находится в файле api.py
Посмотреть документацию к имеющимся API-методам можно на сайте:
https://petfriends.skillfactory.ru/apidocs/#/.

- В директории /tests располагается файл с тестами
- В директории /tests/images лежат картинки для теста добавления питомца и теста добавления картинки
- В корневой директории лежит файл settings.py - содержит информацию о валидном логине и пароле
- В корневой директории лежит файл api.py, который является библиотекой к REST api сервису веб приложения Pet Friends

Тесты проверяют работу методов используя api библиотеку.

Для работы приложения нужно установить библиотеки: requests, pytest, os, dotenv:

- pip install requests
- pip install pytest
- pip install dotenv

Также необходимо создать в корневой папке проекта файл .env со следущим содержимым:

- valid_email = "Ваш email"
- valid_pass = "Ваш пароль"

В рамках домашней работы были разработаны методы:

- add_new_pet_without_photo
- add_photo_for_pet

а также 10 тестов:

1. test_get_api_key_for_invalid_user
2. test_get_api_key_for_incorrect_login_user
3. test_get_api_key_for_incorrect_password_user
4. test_get_pets_with_empty_key
5. test_successful_add_pet_without_photo_RUS
6. test_successful_add_pet_without_photo_ENG
7. test_unsuccessful_add_pet_without_photo
8. test_successful_add_photo_for_pet
9. test_unsuccessful_delete_someones_pet
10. test_unsuccessful_update_someone_else_pet_info

