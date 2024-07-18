"""Method for operations"""


def compute(op: str, a: float, b: float) -> float:
    """Compute the result of a given operation."""
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        assert b != 0, 'Division by zero'
        return a / b
    else:
        raise ValueError('Invalid operation')
