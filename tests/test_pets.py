import pytest
from api import Pets

pet = Pets()


def test_register_user():
    reg_token, reg_id, status = pet.register_user()
    assert reg_token
    assert reg_id
    assert status == 200


def test_delete_user():
    body, status = pet.delete_user()
    assert body
    if body == '{}':
        assert status == 200
    else:
        assert status == 500


def test_get_token():
    token, my_id, status = pet.get_token()
    assert token
    assert my_id
    assert status == 200


def test_list_users():
    status, my_id = pet.get_list_users()
    assert my_id
    assert status == 200


def test_create_pet():
    pet_id, status = pet.create_pet()
    assert pet_id
    assert status == 200


def test_add_pet_photo():
    status, link = pet.add_pet_photo()
    assert link is not None
    assert status == 200


def test_update_pet():
    pet_id, status = pet.update_pet()
    assert pet_id is not None
    assert status == 200


def test_get_pet_by_id():
    pet_name, status = pet.get_pet_by_id()
    assert pet_name
    assert status == 200


def test_add_comment():
    message_id, status = pet.add_comment()
    assert message_id
    assert status == 200


@pytest.mark.xfail
def test_add_like():
    body, status = pet.add_like()
    assert body
    if body is 'null':
        assert status == 200
    else:
        assert status == 403


def test_delete_pet():
    body, status = pet.delete_pet()
    assert body
    if body == '{}':
        assert status == 200
    else:
        assert status == 500

# Тест test_add_like с отметкой xfail, потому что во время выполнения теста
# возвращается некорректный статус-код при попытке поставить повторный "лайк" тому же питомцу
