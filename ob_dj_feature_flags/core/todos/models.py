from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    completed = models.BooleanField(_("Completed"), default=False)

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __str__(self):
        return self.title
