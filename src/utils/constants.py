import operator as op
import math


env = dict()
env.update(vars(math))
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
    'begin': lambda *x: x[-1],
})
