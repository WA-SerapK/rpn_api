"""All endpoints"""
from flask import jsonify, request, make_response
from flask_restx import Namespace, Resource

from app.models.models import value_model

ns = Namespace('rpn', description='RPN operations')

rpn_stacks = {}
operand = {
    "addition": "add",
    "subtraction": "sub",
    "multiplication": "mul",
    "division": "div"
}


@ns.route('/stack')
class Stack(Resource):
    """Class to handle create and retrieve stacks"""
    def post(self):
        """Create a new stack."""
        stack_id = str(len(rpn_stacks) + 1)
        rpn_stacks[stack_id] = []

        return make_response(jsonify({'stack_id': stack_id}), 201)

    def get(self):
        """List the available stack."""
        return make_response(jsonify(rpn_stacks), 200)


@ns.route('/op')
class Operand(Resource):
    """Retrieve list operand."""
    def get(self):
        """List all the operand."""
        return make_response(jsonify(operand), 200)


@ns.route('/stack/<stack_id>')
class StackStackId(Resource):
    """Handle operations for a specific stack."""
    @ns.expect(value_model)
    def post(self, stack_id):
        """Push a new value to a stack."""
        if stack_id not in rpn_stacks:
            return make_response(jsonify({'message': 'Stack not found'}), 404)

        value = request.json.get('value')
        if value is None:
            return make_response(jsonify({'message': 'Value is required in payload'}), 400)

        rpn_stacks[stack_id].append(value)

        return make_response(jsonify({'message': f'Value {value} pushed to stack {stack_id}'}), 200)

    def get(self, stack_id):
        """Get a stack."""
        if stack_id not in rpn_stacks:
            return make_response(jsonify({'message': 'Stack not found'}), 404)

        return make_response(jsonify(rpn_stacks[stack_id]), 200)

    def delete(self, stack_id):
        """Delete a stack."""
        if stack_id not in rpn_stacks:
            return make_response(jsonify({'message': 'Stack not found'}), 404)

        del rpn_stacks[stack_id]

        return make_response(jsonify({'message': 'Stack deleted'}), 200)

