import pytest
from django.test import Client
from shop.models import Shop
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestShop:
    def test_shop_index_view(self):
        client = Client()

        response = client.get("/")
        assert response.status_code == 200

    def test_shop_add_view(self):
        client = Client()

        user = User.objects.create(username="test", email="test@test.com", password="test")
        client.force_login(user)

        response = client.post("/", {"title": "test", "text": "test"})
        assert response.status_code == 302
        assert Shop.objects.count() == 1

        response = client.post("/", {"title": "test", "text": "test"}, follow=True)
        assert response.status_code == 200
        assert Shop.objects.count() == 2
