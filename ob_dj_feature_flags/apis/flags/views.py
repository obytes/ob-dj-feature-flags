import logging

from rest_framework import mixins, permissions, viewsets

from ob_dj_feature_flags.apis.flags.serializers import FeatureFlagsSerializer
from ob_dj_feature_flags.core.flags.models import FeatureFlag

logger = logging.getLogger(__name__)


class FeatureFlagsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = FeatureFlagsSerializer
    queryset = FeatureFlag.objects.all()
