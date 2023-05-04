import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.flags.factories import FeatureFlagFactory

url = reverse(
    "todos:todos-list",
)


@pytest.mark.django_db
def test_todos_api_feature_flags(api_client):
    todos_flag = FeatureFlagFactory(name="todos", active=True)
    todos_list_flag = FeatureFlagFactory(name="todos_list", active=True)
    todos_create_flag = FeatureFlagFactory(name="todos_create", active=True)

    # test list
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    todos_list_flag.active = False
    todos_list_flag.save()

    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"error": "Inactive feature"}

    # test create
    response = api_client.post(url, data={"title": "test"})
    assert response.status_code == status.HTTP_201_CREATED
    todos_create_flag.active = False
    todos_create_flag.save()

    response = api_client.post(url, data={"title": "test"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"error": "Inactive feature"}

    # test class decorator
    todos_create_flag.active = True
    todos_create_flag.save()

    todos_list_flag.active = True
    todos_list_flag.save()

    todos_flag.active = False
    todos_flag.save()
    
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"error": "Inactive feature"}

    response = api_client.post(url, data={"title": "test"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"error": "Inactive feature"}
