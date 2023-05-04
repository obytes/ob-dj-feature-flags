from django.db import models
from django.utils.translation import gettext_lazy as _

from ob_dj_feature_flags.core.flags.managers import FeatureFlagManager
from ob_dj_feature_flags.utils.model import DjangoModelCleanMixin


class FeatureFlag(DjangoModelCleanMixin, models.Model):
    name = models.CharField(max_length=50, help_text=_("Name of the flag"), unique=True)
    description = models.TextField(
        help_text=_("Description of the flag"), blank=True, null=True
    )
    active = models.BooleanField(
        default=False,
        help_text=_("Whether the flag is active or not"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("When the flag was created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("When the flag was last updated"),
    )

    objects = FeatureFlagManager()

    class Meta:
        verbose_name = _("Feature Flag")
        verbose_name_plural = _("Feature Flags")

    def __str__(self):
        return f"{self.name} - {self.active}"
