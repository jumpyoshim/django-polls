import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_question_list_view(self):
        response = self.client.get(reverse('polls:list'))
        assert response.status_code == 200

    def test_question_detail_view(self):
        response = self.client.get(reverse('polls:detail', kwargs={'pk': 1}))
        assert response.status_code == 404

    def test_question_create_view(self):
        response = self.client.get(reverse('polls:create'))
        assert response.status_code == 200

    def test_vote_view(self):
        response = self.client.get(reverse('polls:vote', kwargs={'pk': 1}))
        assert response.status_code == 404
