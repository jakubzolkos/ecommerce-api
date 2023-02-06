import pytest
from rest_framework.test import APIClient
import django
django.setup()


@pytest.fixture
def api_client():
    return APIClient
