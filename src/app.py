from utils.constants import env


def lex(code_str):
    return code_str.replace('(', ' ( ').replace(')', ' ) ').split()


def to_num(token):
    try:
        return float(token)
    except ValueError:
        return token


def read(tokens):
    token = tokens.pop(0)

    if token != '(':
        return token

    res = []
    while tokens[0] != ')':
        elem = read(tokens)
        res.append(elem)

    del tokens[0]
    return res


def parse(tokens):
    tokens = [to_num(x) for x in tokens]

    return read(tokens)


def eval(ast):
    if isinstance(ast, str):
        return env[ast]
    elif isinstance(ast, float):
        return ast
    elif ast[0] == 'if':
        (_, test, conseq, alt) = ast
        exp = (conseq if eval(test) else alt)

        return exp
    else:
        func, *args = map(eval, ast)
        return func(*args)


def schemestr(exp):
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')'
    else:
        return str(exp)


def repl(prompt='lis.py> '):
    while True:
        val = eval(parse(lex(prompt)))
        if val is not None:
            print(schemestr(val))


if __name__ == '__main__':
    repl()
