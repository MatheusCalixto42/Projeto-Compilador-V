import ply.lex as lex
from tabulate import tabulate

reservadas = { # Analisar defer, as, suporte a global
    'as': 'AS',
    'assert': 'ASSERT',
    'break': 'BREAK',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'defer': 'DEFER',
    'else': 'ELSE',
    'enum': 'ENUM',
    'false': 'FALSE',
    'fn': 'FN',
    'for': 'FOR',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'is': 'IS',
    'isreftype': 'ISREFTYPE',
    'match': 'MATCH',
    'mut': 'MUT',
    'none': 'NONE',
    'or': 'OR',
    'return': 'RETURN',
    'sizeof': 'SIZEOF',
    'true': 'TRUE',
    'type': 'TYPE',
    'typeof': 'TYPEOF',
    'union': 'UNION',
    'unsafe': 'UNSAFE',
    '__global': 'GLOBAL',
}

tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',
  'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MOD_ASSIGN', 'BIT_AND_ASSIGN', 'BIT_OR_ASSIGN',
  'BIT_XOR_ASSIGN', 'BIT_LSHIFT_ASSIGN', 'BIT_RSHIFT_ASSIGN', 'EQ', 'NEQ', 'LT',
  'LE', 'GT', 'GE', 'AND', 'NOT', 'BIT_AND', 'BIT_OR', 'BIT_XOR', 'LSHIFT', 'RSHIFT',
  'BIT_NOT', 'INCREMENT', 'DECREMENT', 'DOTDOT', 'DECLARE_ASSIGN', 'QUESTION',
  'EXCLAMATION', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
  'DOT', 'COMMA', 'SEMICOLON', 'COLON','DOLLAR','ID','NUMBER','BINARY','OCTAL'
  'HEX','NOTACAOCIENTIFICA','NUMBERFLOAT','ASPASSIMPLES','ASPASDUPLAS'] + list(reservadas.values())

t_PLUS         = r'\+'
t_MINUS        = r'-'
t_TIMES        = r'\*'
t_DIVIDE       = r'/'
t_MOD          = r'%'

t_ASSIGN            = r'='
t_PLUS_ASSIGN       = r'\+='
t_MINUS_ASSIGN      = r'-='
t_TIMES_ASSIGN      = r'\*='
t_DIVIDE_ASSIGN     = r'/='
t_MOD_ASSIGN        = r'%='
t_BIT_AND_ASSIGN    = r'&='
t_BIT_OR_ASSIGN     = r'\|='
t_BIT_XOR_ASSIGN    = r'\^='
t_BIT_LSHIFT_ASSIGN = r'<<='
t_BIT_RSHIFT_ASSIGN = r'>>='

t_EQ  = r'=='
t_NEQ = r'!='
t_LT  = r'<'
t_LE  = r'<='
t_GT  = r'>'
t_GE  = r'>='

t_AND = r'&&'
t_OR  = r'\|\|'
t_NOT = r'!'

t_BIT_AND = r'&'
t_BIT_OR  = r'\|'
t_BIT_XOR = r'\^'
t_LSHIFT  = r'<<'
t_RSHIFT  = r'>>'
t_BIT_NOT = r'~'

t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'

t_DOTDOT         = r'\.\.'     
t_DECLARE_ASSIGN = r':='       
t_QUESTION       = r'\?'       
t_EXCLAMATION    = r'!' 

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_DOT       = r'\.'
t_COMMA     = r','
t_SEMICOLON = r';'
t_COLON     = r':'
t_DOLLAR    = r'\$'
t_ASPASSIMPLES = r'\''
t_ASPASDUPLAS = r'\"'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value,'ID') #busca nas reservadas se tem alguma igual, se tiver retorna com o nome que esta la, por exemplo "IF", se n tiver retorna com 'ID'
    return t

def t_BINARY(t):
    r'0[bB][01]+'
    t.value = int(t.value, 2)
    return t

def t_OCTAL(t):
    r'0[oO][0-7]+'
    t.value = int(t.value, 8)
    return t

def t_HEX(t):
    r'0[xX][0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t

def t_NOTACAOCIENTIFICA(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)'
    t.value = float(t.value)
    return t

def t_NUMBERFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


t_ignore  = ' \t' 


lexer = lex.lex()

#codigo  de exemplo em V para testar
codigo_v = """
x := 10
y := 20
z := x + y * 2
if x == y {
    println('iguais')
} else {
    println('diferentes')
}
++x
--y
$myvar = 42
"""
lexer.input(codigo_v)

tabela = []

# Função para calcular coluna
def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

for tok in lexer:
    coluna = find_column(codigo_v, tok)
    tabela.append([tok.type, tok.value, tok.lineno, tok.lexpos])

cabecalho = ["Token", "Lexema", "Linha", "Posição"]

print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))