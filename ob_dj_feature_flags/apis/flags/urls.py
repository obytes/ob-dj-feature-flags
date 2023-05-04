from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from ob_dj_feature_flags.apis.flags.views import FeatureFlagsViewSet

app_name = "flags"

router = SimpleRouter(trailing_slash=False)

router.register(r"", FeatureFlagsViewSet, basename="feature_flags"),

urlpatterns = [
    path("", include(router.urls)),
]
