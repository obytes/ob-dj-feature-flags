# ob-dj-feature-flags

ob-dj-feature-flags is a Django package for managing feature flags and controlling access to Django views & API endpoints using decorators.

## Features

- Create and manage feature flags within your Django admin panel.
- Decorators for views and viewsets to easily control access based on feature flags.
- Caching mechanism to improve performance when checking feature flag status.
- Management command to scan viewsets and actions to populate the feature flags automatically (coming soon).

### Overview

```python
from ob_dj_feature_flags.utils.decorators import class_feature_flag, action_feature_flag

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
```

In this example, the TodosViewSet class is decorated with `@class_feature_flag("todos")`, which checks if the 'todos' feature flag is active before allowing access to any actions within the viewset.

Additionally, the list() method is decorated with `@action_feature_flag("todos_list")`, which checks if the 'todos_list' feature flag is active before allowing access to the list action. Similarly, the create() method is decorated with `@action_feature_flag("todos_create")`, which checks if the 'todos_create' feature flag is active before allowing access to the create action.

By combining both class-level and action-level feature flags, you can control access to the entire viewset based on the 'todos' flag, as well as control access to specific actions within the viewset based on the corresponding flags ('todos_list' and 'todos_create' in this example).

## Installation

Use pip to install ob-dj-feature-flags:

```shell
pip install ob-dj-feature-flags
```

## Usage

### Creating Feature Flags

Define feature flags in your Django project using the provided FeatureFlag admin. Each feature flag has a unique name and an active status.


### Decorating Views

Use the `@action_feature_flag` decorator to control access to individual views based on feature flags. Apply the decorator to the desired view functions or class-based views. Example:

```python
from ob_dj_feature_flags.utils.decorators import action_feature_flag

@action_feature_flag('my_feature_flag')
def my_view(request):
    # Your view logic here
    pass
```

This will check if the 'my_feature_flag' is active before allowing access to the view. If the flag is inactive, a JSON response with an error message and status code 404 will be returned.

### Decorating Viewsets

Use the `@class_feature_flag` decorator to control access to viewsets based on feature flags. Apply the decorator to the viewset classes. Example:

```python
from ob_dj_feature_flags.utils.decorators import class_feature_flag

@class_feature_flag('my_feature_flag')
class MyViewSet(viewsets.ModelViewSet):
    # Your viewset logic here
    pass
```

This will check if the 'my_feature_flag' is active before allowing access to any actions within the viewset. If the flag is inactive, a JSON response with an error message and status code 404 will be returned.


## Skipping Feature Flags During Tests

To skip feature flags during tests, you can use the `@skip_feature_flags` decorator. This decorator can be applied to test functions or test methods to bypass the feature flag checks within the tested views or viewsets.

To use the `skip_feature_flags` decorator, import it from `ob_dj_feature_flags.utils.decorators` and apply it to your test functions or methods. Here's an example:

```python
from ob_dj_feature_flags.utils.decorators import skip_feature_flags
import pytest

@skip_feature_flags
def test_my_view():
    # Test logic here
    pass
```

In this example, the `@skip_feature_flags` decorator is applied to the test function, `test_my_view`. This will skip the feature flag checks within the tested view, allowing the test to proceed without considering the feature flags.


## Skipping Feature Flags In The project

If you want to skip feature flags in the entire app, you can add a setting to your Django project's settings module. By setting the `SKIP_FEATURE_FLAGS` setting to `True`, all feature flag checks will be skipped when running the project.

## Configuration

The package provides a caching mechanism to improve performance when checking feature flag status. By default, it uses Django's caching system. You can configure the cache backend and cache timeout in your Django project settings.

## Intergration with feature flag management services

You can create a webhook endpoint to receive feature flag updates from your favorite feature flag management service. The endpoint should accept POST requests with a JSON payload containing the feature flag name and active status. Example:

```json
{
    "name": "my_feature_flag",
    "active": true
}
```
