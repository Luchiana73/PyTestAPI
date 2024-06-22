import json
import requests
import settings
from faker import Faker


class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {'email': settings.VALID_EMAIL, 'password': settings.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json().get('token')
        my_id = res.json().get('id')
        status = res.status_code
        return my_token, my_id, status

    def get_list_users(self):
        """Запрос для получения id пользователя поcле его авторизации"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.text
        return status, my_id

    def create_pet(self) -> json:
        """Запрос для создания питомца"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        fake = Faker()
        data = {
            "name": fake.name(),
            "type": "hamster",
            "age": 2,
            "gender": "Female",
            "owner_id": my_id
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json().get('id')
        status = res.status_code
        return pet_id, status

    def add_pet_photo(self) -> json:
        """Запрос для добавления фотографии питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('pet.jpg', open('D:\\Desktop\\PycharmProjects\\PyTestAPI\\tests\\Photo\\pet.jpg', 'rb'),
                         'image/jpeg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', files=files, headers=headers)
        status = res.status_code
        link = res.json().get('link')
        return status, link

    def update_pet(self) -> json:
        """Запрос для обновления информации о питомце"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        fake = Faker()
        data = {"id": pet_id,
                "name": fake.first_name(),
                "type": "cat",
                "age": 10,
                "gender": "Male"}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        updated_pet_id = res.json()['id']
        return updated_pet_id, status

    def get_pet_by_id(self) -> json:
        """Запрос для получения информации о питомце по его id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_name = res.json()['pet']['name']
        return pet_name, status

    def add_comment(self) -> json:
        """Запрос для добавления комментария о питомце"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        fake = Faker()
        data = {"message": fake.text()}
        res = requests.put(self.base_url + f'/pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        message_id = res.json()['id']
        return message_id, status

    def add_like(self):
        """Запрос для добавления отметки "нравится" к питомцу"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'/pet/{pet_id}/like', headers=headers)
        status = res.status_code
        body = res.text
        return body, status

    def delete_pet(self):
        """Запрос для удаления питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'/pet/{pet_id}', headers=headers)
        status = res.status_code
        body = res.text
        return body, status


# pet = Pets()
#
# pet.get_token()
# pet.get_list_users()
# pet.create_pet()
# pet.add_pet_photo()
# pet.update_pet()
# pet.get_pet_by_id()
# pet.add_comment()
# pet.add_like()
# pet.delete_pet()
