# ob-dj-feature-flags

Feature flags are a powerful technique that allows you to enable/disable specific features in your application without deploying new code. This gives you the ability to control the behavior of your application dynamically and perform A/B testing, read more about feature flags [here](https://www.atlassian.com/continuous-delivery/principles/feature-flags).

ob-dj-feature-flags provides a simple way to create and manage feature flags within your Django admin panel. It also provides decorators for views and viewsets to easily control access based on feature flags.

## Features

- Create and manage feature flags within your Django admin panel.
- Add decorators to views and viewsets to control access based on the created feature flags.
- Caching mechanism to reduce database hits when checking feature flag statuses.
- Feature flags endpoint to use the same feature flags in your client apps.
- Skip feature flags during tests or in the entire project.

## Setup & Installation

1. Use pip to install ob-dj-feature-flags:

```shell
pip install ob-dj-feature-flags
```

2. Add "ob_dj_feature_flags" to your `INSTALLED_APPS` setting like this:

```python
   # settings.py
   INSTALLED_APPS = [
        ...
        "ob_dj_feature_flags.core.flags",
   ]
```

3. If you plan to use the created feature flags in your client apps, add the feature flags endpoint to your project's urls.py:

```python
   # urls.py
   urlpatterns = [
        ...
        path('ob-dj-feature-flags/', include('ob_dj_feature_flags.apis.flags.urls')),
   ]
```

4. Run `python manage.py migrate` to create the feature flags table.

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

### Use in Your Client Apps

Integrating feature flags into your client apps allows you to control the behavior and enable/disable specific features dynamically. To leverage feature flags in your client app, follow these simple steps:

1. Make a GET request to the feature flags endpoint of your backend API (preferably at startup) `ob-dj-feature-flags/` (check step 3 of Setup & Installation section).
2. The endpoint will provide a JSON response containing the list of feature flags along with their statuses.
3. Store the feature flags and their statuses somewhere in your client app.
4. Use the feature flags to control the behavior of your client app (you can create a wrapper function or a custom hook to simplify this process).

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
