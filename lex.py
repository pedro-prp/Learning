import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    code = re.sub(r';;.*', "", code)

    patterns = {
        'STRING': r'\".+\"',
        'NUMBER': r'[+-]?\d+(\.\d+)?',
        'NAME': r'(([a-zA-Z\-\?>%!+.]+)|(?:;+.+))',
        'CHAR': r'#\\\w*',
        'BOOL': r'#[t|f]',
        'LPAR': r'\(',
        'RPAR': r'\)',
        'QUOTE': r'\''
    }

    regex = '|'.join(f"(?P<{k}>{v})" for k,v in patterns.items())

    regex = re.compile(regex)

    for match in regex.finditer(code):
        value = match.group()
        kind = match.lastgroup

        yield Token(kind, value)

    return [Token('INVALIDA', 'valor inválido')]