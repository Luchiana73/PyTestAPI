import json
import requests
import settings
from faker import Faker


class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'
        self.session = requests.Session()
        self.my_token = None
        self.my_id = None
        self.pet_id = None

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {'email': settings.VALID_EMAIL, 'password': settings.VALID_PASSWORD}
        res = self.session.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json().get('token')
        self.my_token = my_token
        my_id = res.json().get('id')
        self.my_id = my_id
        status = res.status_code
        self.session.headers.update({'Authorization': f'Bearer {self.my_token}'})
        return my_token, my_id, status

    def get_list_users(self) -> json:
        """Запрос для получения списка пользователей"""
        res = self.session.get(self.base_url + 'users')
        status = res.status_code
        my_id = res.text
        return status, my_id

    def create_pet(self) -> json:
        """Запрос для создания питомца"""
        data = {
            "name": "Funtik",
            "type": "hamster",
            "age": 2,
            "gender": "Female",
            "owner_id": self.my_id
        }
        res = self.session.post(self.base_url + 'pet', data=json.dumps(data))
        pet_id = res.json().get('id')
        self.pet_id = pet_id
        status = res.status_code
        return pet_id, status

    def add_pet_photo(self) -> json:
        """Запрос для добавления фотографии питомца"""
        files = {'pic': ('pet.jpg', open('D:\\Desktop\\PycharmProjects\\PyTestAPI\\tests\\Photo\\pet.jpg', 'rb'),
                         'image/jpeg')}
        res = self.session.post(self.base_url + f'pet/{self.pet_id}/image', files=files)
        status = res.status_code
        link = res.json().get('link')
        return status, link

    def update_pet(self):
        """Запрос для обновления информации о питомце"""
        fake = Faker()
        data = {"id": self.pet_id,
                "name": fake.first_name(),
                "type": "cat",
                "age": 10,
                "gender": "Male"}
        res = self.session.patch(self.base_url + 'pet', data=json.dumps(data))
        status = res.status_code
        updated_pet_id = res.json()['id']
        return updated_pet_id, status

    def get_pet_by_id(self):
        """Запрос для получения информации о питомце по его id"""
        res = requests.get(self.base_url + f'pet/{self.pet_id}')
        status = res.status_code
        pet_name = res.json()['pet']['name']
        return pet_name, status

    def add_comment(self):
        """Запрос для добавления комментария о питомце"""
        fake = Faker()
        data = {"message": fake.text()}
        res = self.session.put(self.base_url + f'/pet/{self.pet_id}/comment', data=json.dumps(data))
        status = res.status_code
        message_id = res.json()['id']
        return message_id, status

    def add_like(self):
        """Запрос для добавления отметки "нравится" к питомцу"""
        res = self.session.put(self.base_url + f'/pet/{self.pet_id}/like')
        status = res.status_code
        body = res.text
        return body, status

    def delete_pet(self):
        """Запрос для удаления питомца"""
        res = self.session.delete(self.base_url + f'/pet/{self.pet_id}')
        status = res.status_code
        body = res.text
        return body, status


pet = Pets()

pet.get_token()
pet.get_list_users()
pet.create_pet()
pet.add_pet_photo()
pet.update_pet()
pet.get_pet_by_id()
pet.add_comment()
pet.add_like()
pet.delete_pet()
