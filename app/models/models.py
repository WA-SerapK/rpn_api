"""All models"""
from flask_restx import fields
from api import api


value_model = api.model('Value', {
    'value': fields.Integer(required=True, description='Value to push onto the stack')
})
