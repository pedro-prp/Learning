import operator as op
import math


env = dict()

# math constants
env.update(vars(math))

# basic operations
env.update({
    '+': op.add,
    '-': op.sub,
    '/': op.truediv,
    '*': op.mul,
    '=': op.eq,
    '<': op.lt,
    '>': op.gt,
    '<=': op.le,
    '>=': op.ge,
})

# advanced methods
env.update({
    'begin': lambda *x: x[-1],
    'apply': lambda proc, args: proc(*args),
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
    'cons': lambda x, y: [x] + y,
    'eq?': op.is_,
    'expt': pow,
    'length': len,
    'list': lambda *x: list(x),
    'list?': lambda x: isinstance(x, list),
    'map': map,
    'max': max,
    'min': min,
    'not': op.not_,
    'null?': lambda x: x == [],
    'number?': lambda x: isinstance(x, (int, float)),
    'print': print,
    'procedure?': callable,
    'round': round,
    'symbol': lambda x: isinstance(x, str)
})
