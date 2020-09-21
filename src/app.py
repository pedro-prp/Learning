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
    else:
        func, *args = map(eval, ast)
        return func(*args)


if __name__ == '__main__':
    code = '(+ 3 (* 2 (/ 6 2)))'

    print(eval(parse(lex(code))))
