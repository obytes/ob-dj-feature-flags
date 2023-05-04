from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        basePath="/api/",
        license=openapi.License(name="Privately owned"),
    ),
    public=True,
    urlconf="config.urls",
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("admin/", admin.site.urls),
    path("flags/", include("ob_dj_feature_flags.apis.flags.urls")),
    path("todos/", include("ob_dj_feature_flags.apis.todos.urls")),
]
