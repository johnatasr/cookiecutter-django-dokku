import pytest
from {{cookiecutter.github_repository_name}} import settings
from rest_framework.test import APIClient

from {{cookiecutter.github_repository_name}}.core.tests import UserFactory


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup):
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ':memory:',
    }


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def auth_client(user, client):
    client.force_authenticate(user)
    return client
