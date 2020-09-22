from utils.constants import env

Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


def lex(code_str):
    return code_str.replace('(', ' ( ').replace(')', ' ) ').split()


def to_num(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def read(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')

    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return to_num(token)


def parse(tokens):
    return read(tokens)


def eval(code):
    if isinstance(code, str):
        return env[code]
    elif isinstance(code, (int, float)):
        return code
    elif code[0] == 'if':
        (_, test, conseq, alt) = code
        exp = (conseq if eval(test) else alt)
        return eval(exp)
    elif code[0] == 'define':
        (_, symbol, exp) = code
        env[symbol] = eval(exp)
    else:
        proc = eval(code[0])
        args = [eval(arg) for arg in code[1:]]
        return proc(*args)


if __name__ == '__main__':
    code = '(begin (define r 10) (* pi (* r r)))'

    print(eval(parse(lex(code))))
