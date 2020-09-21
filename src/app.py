def lex(code_str):
    return code_str.replace('(', ' ( ').replace(')', ' ) ').split()


def to_num(token):
    try:
        return float(token)
    except:
        return token


if __name__ == '__main__':
    code = '(+ 2 1)'
    
    code = lex(code)
    code = [to_num(x) for x in code]

    print(code)
