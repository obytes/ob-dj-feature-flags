from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from ob_dj_feature_flags.core.flags.models import FeatureFlag

CACHE_KEY = "feature_flags_cache"


@receiver([post_save, post_delete], sender=FeatureFlag)
def refresh_flags_cache(sender, **kwargs):
    flags = FeatureFlag.objects.all()
    flags_cache = {flag.name: flag.active for flag in flags}
    cache.set(CACHE_KEY, flags_cache)
