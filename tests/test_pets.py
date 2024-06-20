from api import Pets

pet = Pets()


def test_get_token():
    token, my_id, status = pet.get_token()
    assert token
    assert my_id
    assert status == 200


def test_list_users():
    my_id = pet.get_list_users()[1]
    status = pet.get_list_users()[0]
    assert my_id
    assert status == 200


def test_create_pet():
    pet_id, status = pet.create_pet()
    assert pet_id
    assert status == 200


def test_add_pet_photo():
    link = pet.add_pet_photo()[1]
    status = pet.add_pet_photo()[0]
    assert link is not None
    assert status == 200


def test_update_pet():
    pet_id = pet.update_pet()[0]
    status = pet.update_pet()[1]
    assert pet_id is not None
    assert status == 200


def test_get_pet_by_id():
    pet_name = pet.get_pet_by_id()[0]
    status = pet.get_pet_by_id()[1]
    assert pet_name
    assert status == 200


def test_add_comment():
    message_id, status = pet.add_comment()
    assert message_id
    assert status == 200


def test_add_like():
    body = pet.add_like()[0]
    status = pet.add_like()[1]
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
