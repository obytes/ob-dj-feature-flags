import logging

from rest_framework import serializers

from ob_dj_feature_flags.core.todos.models import Todo

logger = logging.getLogger(__name__)


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
