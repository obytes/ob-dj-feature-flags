from django.contrib import admin

from ob_dj_feature_flags.core.flags.models import FeatureFlag


class FeatureFlagAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "active"]
    list_filter = ["active"]
    search_fields = ["name", "description"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "active",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


admin.site.register(FeatureFlag, FeatureFlagAdmin)
