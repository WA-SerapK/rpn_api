"""Unit tests for app."""
import uuid

import pytest
from api import app, api
from app.routers.routers import ns, rpn_stacks, operand

api.add_namespace(ns)


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_create_stack(client):
    response = client.post('/rpn/stack')
    assert response.status_code == 201
    data = response.get_json()
    stack_id = data['stack_id']
    assert stack_id in rpn_stacks


def test_list_stacks(client):
    response = client.get('/rpn/stack')
    assert response.status_code == 200

    stacks = response.get_json()
    assert isinstance(stacks, dict)
    assert stacks == rpn_stacks


def test_list_operands(client):
    response = client.get('/rpn/op')
    assert response.status_code == 200

    operands = response.get_json()
    assert isinstance(operands, dict)
    assert operands == operand


def test_success_push_value(client):
    response = client.post('/rpn/stack')
    stack_id = response.get_json()['stack_id']

    response = client.post(f'/rpn/stack/{stack_id}', json={'value': 5})
    print(response.status_code)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == f'Value 5 pushed to stack {stack_id}'
    assert rpn_stacks[stack_id] == [5]


def test_push_value_with_no_value(client):
    response = client.post('/rpn/stack')
    stack_id = response.get_json()['stack_id']

    response = client.post(f'/rpn/stack/{stack_id}', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['message'] == 'Value is required in payload'


def test_success_get_stack(client):
    response = client.post('/rpn/stack')
    stack_id = response.get_json()['stack_id']

    response = client.get(f'/rpn/stack/{stack_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data == []


def test_failed_get_nonexistent_stack(client):
    response = client.get('/rpn/stack/test')
    assert response.status_code == 404
    data = response.get_json()
    assert data['message'] == 'Stack not found'


def test_success_delete_stack(client):
    response = client.post('/rpn/stack')
    stack_id = response.get_json()['stack_id']

    response = client.delete(f'/rpn/stack/{stack_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Stack deleted'
    assert stack_id not in rpn_stacks


def test_failed_delete_nonexistent_stack(client):
    response = client.delete('/rpn/stack/test')
    assert response.status_code == 404
    data = response.get_json()
    assert data['message'] == 'Stack not found'
