import operator as op

env = dict()
env = {
    '+': op.add,
    '-': op.sub,
    '/': op.truediv,
    '*': op.mul,
    '=': op.eq,
    '<': op.lt,
    '>': op.gt,
    '<=': op.le,
    '>=': op.ge,
}
