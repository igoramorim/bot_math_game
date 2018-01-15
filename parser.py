import ast
import re


def expr(code, context=None):
    """Eval a math expression and return the result"""
    if not context:
        context = {}
    code = code.format(**context)

    # An especial case for my own when using percents values.
    # TODO: Fail if you are not comparing same type value like "50 > 20%" haves to fail
    code = re.sub('%', '', code)

    expr = ast.parse(code, mode='eval')
    code_object = compile(expr, '<string>', 'eval')

    return eval(code_object)


# assert expr('10 > 5') == True
# assert expr('1+1==2') == True
#
# assert expr('10 > 5 and 20 < 40') == True
# assert expr('{a} >= {b}', dict(a=100, b=100)) == True
# assert expr('{a} >= {b}', dict(a=200, b=400)) == False
#
# assert expr('1 + 1 + 1 + 1 + 1') == 5
# assert expr('10 ** 5') == 100000
# assert expr('10 - 100') == -90
# assert expr('(10 + 20 * 50 / 2) + 100') == 610
#
# assert expr('10% > 5%')
