from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .util import gen_image
import random


class MyTestCase(APITestCase):
    def setUp(self):
        random.seed(42)
        User.objects.create_superuser("admin", "admin@example.com", "password")

    def login(self):
        self.assertTrue(self.client.login(username="admin", password="password"))

    def create_file(self):
        url = reverse("file-list")
        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "file": gen_image(),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.json()


class FileTest(MyTestCase):
    def test_file_post(self):
        url = reverse("file-list")
        data = {"file": gen_image(), "description": "Some detailed info about factory"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login()

        url = reverse("file-list")
        data = {
            "file": gen_image("factory.png"),
            "description": "Some detailed info about factory",
        }
        response = self.client.post(url, data)
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json["description"], data["description"])
        self.assertIsInstance(json["file"], str)

    def test_file_delete(self):
        url = reverse("file-detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login()
        file = self.create_file()
        url = reverse("file-detail", args=[file["id"]])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_file_put(self):
        url = reverse("file-detail", args=[1])
        response = self.client.put(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login()
        file = self.create_file()
        url = reverse("file-detail", args=[file["id"]])

        file["description"] += "qweqwe"
        file["file"] = gen_image()
        response = self.client.put(url, file)
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json["description"], file["description"])
        self.assertEqual(json["id"], file["id"])


class FactoryTest(MyTestCase):
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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {
            "name": "Factory Name",
            "description": "Some detailed info about factory",
            "cover_id": file["id"],
        }
        url = reverse("factory-list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
