from __future__ import annotations

from functools import wraps

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.test import override_settings

from ob_dj_feature_flags.core.flags.models import FeatureFlag


def get_flags_cache(cache_key="feature_flags_cache"):
    flags_cache = cache.get(cache_key)
    if flags_cache is None:
        flags = FeatureFlag.objects.all()
        flags_cache = {flag.name: flag.active for flag in flags}
        cache.set(cache_key, flags_cache)
    return flags_cache


def action_feature_flag(*feature_flags):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            if getattr(settings, "SKIP_FEATURE_FLAGS", False):
                return view_func(self, request, *args, **kwargs)

            flags_cache = get_flags_cache()
            for flag in feature_flags:
                if flag not in flags_cache:
                    return HttpResponse(
                        content='{"error": "Invalid feature flag"}',
                        content_type="application/json",
                        status=404,
                    )
                if not flags_cache[flag]:
                    return HttpResponse(
                        content='{"error": "Inactive feature"}',
                        content_type="application/json",
                        status=404,
                    )

            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator


def class_feature_flag(*feature_flags):
    def decorator(view_class):
        class DecoratedClass(view_class):
            def dispatch(self, request, *args, **kwargs):
                if getattr(settings, "SKIP_FEATURE_FLAGS", False):
                    return super().dispatch(request, *args, **kwargs)

                flags_cache = get_flags_cache()
                for flag in feature_flags:
                    if flag not in flags_cache:
                        return HttpResponse(
                            content='{"error": "Invalid feature flag"}',
                            content_type="application/json",
                            status=404,
                        )
                    if not flags_cache[flag]:
                        return HttpResponse(
                            content='{"error": "Inactive feature"}',
                            content_type="application/json",
                            status=404,
                        )
                return super().dispatch(request, *args, **kwargs)

        return DecoratedClass

    return decorator


def skip_feature_flags(test_func):
    @wraps(test_func)
    @override_settings(SKIP_FEATURE_FLAGS=True)
    def wrapper(*args, **kwargs):
        return test_func(*args, **kwargs)

    return wrapper
