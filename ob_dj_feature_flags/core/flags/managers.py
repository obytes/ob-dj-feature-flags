import typing

from django.db import models


class FeatureFlagManager(models.Manager):
    def create(self, *args: typing.Any, **kwargs: typing.Any):
        return super().create(*args, **kwargs)
