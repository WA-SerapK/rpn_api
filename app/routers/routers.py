"""All endpoints"""
from flask import jsonify
from flask_restx import Namespace, Resource


ns = Namespace('rpn', description='RPN operations')

rpn_stacks = {}

@ns.route('/stack')
class Stack(Resource):
    """Class to handle create and retrieve stacks"""
    def post(self):
        """Create a new stack."""
        stack_id = str(len(rpn_stacks) + 1)
        rpn_stacks[stack_id] = []

        return jsonify({'stack_id': stack_id})

    def get(self):
        """List the available stack."""
        return jsonify(rpn_stacks)





