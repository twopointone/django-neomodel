from setuptools import setup

setup(
    name="django-neomodel",
    version="0.3.0",
    description="Custom Django Neomodel to support 5.22.0",
    url="https://github.com/myplace/django-neomodel",
    author="MyPlace",
    author_email="",
    license="BSD 2-clause",
    packages=["django_neomodel"],
    install_requires=["neomodel==5.4.0", "django~=4.2.8"],
)
