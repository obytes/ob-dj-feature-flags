from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodosConfig(AppConfig):
    name = "ob_dj_feature_flags.core.todos"
    verbose_name = _("Todos")
