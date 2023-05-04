import pytest

from tests.core.flags.factories import FeatureFlagFactory


@pytest.mark.django_db
def test_feature_flag_factory():
    instance = FeatureFlagFactory()
    assert instance.id
    assert instance.name
    assert instance.description
    assert instance.active is not None
    assert instance.created_at
    assert instance.updated_at
    assert str(instance) == f"{instance.name} - {instance.active}"
