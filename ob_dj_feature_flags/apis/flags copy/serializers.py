import logging

from rest_framework import serializers

from ob_dj_feature_flags.core.flags.models import FeatureFlag

logger = logging.getLogger(__name__)


class FeatureFlagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureFlag
        fields = "__all__"
