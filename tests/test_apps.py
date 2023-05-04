import pytest
from django.apps import apps


@pytest.mark.django_db
def test_app_ready():
    assert apps.ready == True
    assert apps.get_app_config("flags")
    assert apps.get_app_config("flags").verbose_name == "Flags"
    # Make sure app_config path always provided
    assert apps.get_app_config("flags").path
