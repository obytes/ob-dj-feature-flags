import logging

from rest_framework import mixins, permissions, viewsets

from ob_dj_feature_flags.core.flags.models import FeatureFlag
from ob_dj_feature_flags.apis.flags.serializers import (
    FeatureFlagsSerializer,
)

from ob_dj_feature_flags.utils.decorators import action_feature_flag, class_feature_flag

logger = logging.getLogger(__name__)

class FeatureFlagsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = FeatureFlagsSerializer


# a test viewset for feature flags mixin
@class_feature_flag("test_feature_flag")
class TestFeatureFlagsViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = FeatureFlag.objects.all()
    serializer_class = FeatureFlagsSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @action_feature_flag("test_feature_flag_create")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)