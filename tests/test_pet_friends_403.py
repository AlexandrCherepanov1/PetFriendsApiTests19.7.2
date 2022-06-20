from api import PetFriends
from settings import *
import os
import pytest


pf = PetFriends()


def test_get_api_key_for_non_mail_and_pass(email='', password=''):
    """ Проверяем что запрос api ключа возвращает статус 403. Если нет email и password """

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert "This user wasn&#x27;t found in database" in result
# -----------------------------------------------------------------------------------------------------


def test_get_api_key_for_invalid_mail(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если email не верный """

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert "This user wasn&#x27;t found in database" in result
# -----------------------------------------------------------------------------------------------------


def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если password не верный"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert "This user wasn&#x27;t found in database" in result
# -----------------------------------------------------------------------------------------------------


def test_add_new_pet_with_valid_data_invalid_key(name=add_name, animal_type=add_animal_type, age=add_age,
                                                 pet_photo=add_pet_photo):
    """Тест добавления питомца с корректными данными и неверным auth_key"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = invalid_auth_key
    status, result = pf.add_new_pet_and_photo(auth_key, name, animal_type, age, pet_photo)  # Отправляем запрос
    assert status == 403
    assert 'Please provide &#x27;auth_key&#x27;' in result
# ----------------------------------------------------------------------------------------------------


def test_add_new_pet_with_valid_data_rotten_key(name=add_name, animal_type=add_animal_type, age=add_age,
                                                pet_photo=add_pet_photo):
    """Тест добавления питомца с корректными данными и auth_key с истекшим сроком"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = rotten_auth_key
    status, result = pf.add_new_pet_and_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 403
    assert 'Please provide &#x27;auth_key&#x27;' in result
# --------------------------------------------------------------------------------------------------


def test_get_all_pets_with_invalid_key(filter='my_pets'):
    """Тест на получение списка питомцев с неверным auth_key"""

    auth_key = invalid_auth_key
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403
    assert 'Please provide &#x27;auth_key&#x27;' in result
# --------------------------------------------------------------------------------------------------












