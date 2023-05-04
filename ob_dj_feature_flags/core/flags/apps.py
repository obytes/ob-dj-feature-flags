from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlagsConfig(AppConfig):
    name = "ob_dj_feature_flags.core.flags"
    verbose_name = _("Flags")

    def ready(self):
        from ob_dj_feature_flags.core.flags import receivers  # noqa
