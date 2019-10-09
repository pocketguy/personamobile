from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO


class MyTestCase(APITestCase):
    def setUp(self):
        User.objects.create_superuser("admin", "admin@example.com", "password")

    def login(self):
        self.assertTrue(self.client.login(username="admin", password="password"))

    def gen_image(self):
        image = Image.new("RGB", (60, 30), color="red")
        bio = BytesIO()
        image.save(bio, "PNG")
        bio.seek(0)
        return bio


class FileTest(MyTestCase):
    def test_file_post(self):
        """
        Ensure admin can create a new file object.
        """
        url = reverse("file-list")
        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "file": self.gen_image(),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login()

        url = reverse("file-list")
        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "file": self.gen_image(),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FactoryTest(MyTestCase):
    def create_file(self):
        url = reverse("file-list")
        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "file": self.gen_image(),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.json()

    def test_factory_post(self):
        """
        Ensure admin can create a new factory object.
        """
        url = reverse("factory-list")

        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "cover_id": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login()

        file = self.create_file()

        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "cover_id": file["id"],
        }
        url = reverse("factory-list")
        response = self.client.post(url, data, format="json")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
