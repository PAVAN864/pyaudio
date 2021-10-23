"""Update the json list if more words need to get recognised"""
symbol = {
    'alpha': 'α',
    'beta': 'β',
    'gamma': 'γ',
    'lambda': 'λ',
    'plus': '+',
    'add': '+',
    'subtract': '-',
    'minus': '-',
    'into': '*',
    'multiply': 'X',
    'multiplied by': 'X',
    'divide': '/',
    'divided by': '/',
    'by': '/',
    'percentage': '%',
    'mod': '%',
    'theta': 'θ',
    'integration': '∫',
    'Integration of': '∫',
    'integration of': '∫',
    'derivative': '∂',
    'differentiation': '∂',
    'equal to': '=',
    'equals to': '=',
    'equas': '=',
    'summation':'Σ',
    'delta': 'Δ',
    'of': ''
}


def get():
    # export the symbol list
    return symbol
