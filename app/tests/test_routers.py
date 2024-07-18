"""Unit tests for app."""
import pytest
from api import app, api
from app.routers.routers import ns, rpn_stacks

api.add_namespace(ns)

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_create_stack(client):
    response = client.post('/rpn/stack')
    assert response.status_code == 200
    data = response.get_json()
    stack_id = data['stack_id']
    assert stack_id in rpn_stacks


def test_list_stacks(client):
    response = client.get('/rpn/stack')
    assert response.status_code == 200

    stacks = response.get_json()
    assert isinstance(stacks, dict)
    assert stacks == rpn_stacks
