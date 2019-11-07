from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from quotedb import models


class APITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="TestUser")

    def test_api(self):
        # Anonymous user can view
        response = self.client.get(reverse("api:quote-list"))
        self.assertEqual(response.status_code, 200, "anonymous user can view")

        # but not post
        response = self.client.post(reverse("api:quote-list"))
        self.assertEqual(response.status_code, 403, "anonymous user can not post")

        # After logging in
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("api:quote-list"), data={"body": "quote body"}
        )
        # Can create new quote
        self.assertEqual(response.status_code, 201, "Logged in user can post")
        self.assertEqual(models.Quote.objects.count(), 1)
