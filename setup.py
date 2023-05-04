from setuptools import setup

# version = "0.0.3"

setup(
    install_requires=[
        "django",
        "djangorestframework",
    ],
    packages=[
        "ob_dj_feature_flags.apis",
        "ob_dj_feature_flags.apis.flags",
        "ob_dj_feature_flags.core",
        "ob_dj_feature_flags.core.flags",
        "ob_dj_feature_flags.utils",
    ],
    tests_require=["pytest"],
    use_scm_version={
        "write_to": "version.py",
    },
    setup_requires=["setuptools_scm"],
)
