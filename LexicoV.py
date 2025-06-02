import ply.lex as lex

reservadas = {
    'true' : 'TRUE',
    'false': 'FALSE',
    'none' : 'NONE',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'match' : 'MATCH',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'or' : 'OR',
    'goto' : 'GOTO',
    'select' : 'SELECT',
    'fn' : 'FN',
    'module' : 'MODULE',
    'import' : 'IMPORT',
    'const' : 'CONST',
    'type' : 'TYPE',
    'struct' : 'STRUCT',
    'enum' : 'ENUM',
    'union' : 'UNION',
    'interface' : 'INTERFACE',
    'implements' : 'IMPLEMENTS',
    'pub' : 'PUB',
    'mut' : 'MUT',
    'shared' : 'SHARED',
    'rlock' : 'RLOCK',
    'lock' : 'LOCK',
    'atomic' : 'ATOMIC',
    'unsafe' : 'UNSAFE',
    'volatile' : 'VOLATILE',
    'as' : 'AS',
    'is' : 'IS',
    'in' : 'IN',
    'isrefttype' : 'ISREFTYPE',
    'sizeof' : 'SIZEOF',
    'typeof' : 'TYPEOF',
    '_offsetof' : 'OFFSETOF',
    '_global' : 'GLOBAL',
    'spawn' : 'SPAWN',
    'go' : 'GO',
    'defer' : 'DEFER',
    'static' : 'STATIC',
    'assert' : 'ASSERT',
    'asm' : 'ASM'
}


tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',
  'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MOD_ASSIGN', 'BIT_AND_ASSIGN', 'BIT_OR_ASSIGN',
  'BIT_XOR_ASSIGN', 'BIT_LSHIFT_ASSIGN', 'BIT_RSHIFT_ASSIGN', 'EQ', 'NEQ', 'LT',
  'LE', 'GT', 'GE', 'AND', 'OR', 'NOT', 'BIT_AND', 'BIT_OR', 'BIT_XOR', 'LSHIFT', 'RSHIFT',
  'BIT_NOT', 'INCREMENT', 'DECREMENT', 'DOTDOT', 'DECLARE_ASSIGN', 'QUESTION',
  'EXCLAMATION', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
  'DOT', 'COMMA', 'SEMICOLON', 'COLON','DOLLAR'] + list(reservadas.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'



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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
  print("Caractere ilegal '%s'" % t.value[0])
  t.lexer.skip(1)



t_ignore  = ' \t' #Ignora branco, tabulação e quebra de linha





lexer = lex.lex()
lexer.input("+\n  - --+\n +  +")
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos)))