import logging

from rest_framework import mixins, permissions, viewsets

from ob_dj_feature_flags.apis.todos.serializers import TodosSerializer
from ob_dj_feature_flags.core.todos.models import Todo
from ob_dj_feature_flags.utils.decorators import action_feature_flag, class_feature_flag

logger = logging.getLogger(__name__)

# a test viewset for feature flags decorators
@class_feature_flag("todos")
class TodosViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = Todo.objects.all()
    serializer_class = TodosSerializer

    @action_feature_flag("todos_list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action_feature_flag("todos_create")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
