import factory

from ob_dj_feature_flags.core.flags.models import FeatureFlag


class FeatureFlagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeatureFlag

    name = factory.Faker("name")
    description = factory.Faker("text")
    active = factory.Faker("boolean")
