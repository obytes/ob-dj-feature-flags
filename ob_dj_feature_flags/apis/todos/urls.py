from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from ob_dj_feature_flags.apis.todos.views import TodosViewSet

app_name = "todos"

router = SimpleRouter(trailing_slash=False)

router.register(r"", TodosViewSet, basename="todos"),

urlpatterns = [
    path("", include(router.urls)),
]
