import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.flags.factories import FeatureFlagFactory

url = reverse("flags:feature_flags-list")


@pytest.mark.django_db
def test_feature_flags_list(api_client):
    todos_flag = FeatureFlagFactory(name="todos", active=True)
    FeatureFlagFactory(name="todos_list", active=True)
    FeatureFlagFactory(name="todos_create", active=True)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["count"] == 3
    assert response.json()["results"][0]["name"] == todos_flag.name
    assert response.json()["results"][0]["active"] == todos_flag.active
