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


def parse(code):
    code = [to_num(x) for x in code]

    return read(code)


if __name__ == '__main__':
    code = '(+ 2 (* 2 1))'

    print(parse(lex(code)))
