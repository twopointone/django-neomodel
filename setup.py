from setuptools import setup

setup(
    name="django-neomodel",
    version="5.4.0",
    description="Custom Django Neomodel to support 5.22.0",
    url="https://github.com/myplace/neomodel/commit/da18b6047d7d332a5d2bbf90b74dbdd0d911f73b",
    author="MyPlace",
    author_email="",
    license="BSD 2-clause",
    packages=["django_neomodel"],
    install_requires=["neomodel==5.4.0", "django~=4.2.8"],
)
