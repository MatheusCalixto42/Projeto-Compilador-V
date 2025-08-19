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
	'int' : 'INT',
	'f32' : 'F32',
	'f64' : 'F64',
	'bool' : 'BOOL', 
	'rune' : 'RUNE',
    'is': 'IS',
    'isreftype': 'ISREFTYPE',
    'main' : 'MAIN',
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
  'LE', 'GT', 'GE', 'AND','NOT', 'BIT_AND', 'BIT_OR', 'BIT_XOR', 'LSHIFT', 'RSHIFT',
  'BIT_NOT', 'INCREMENT', 'DECREMENT', 'DOTDOT', 'DECLARE_ASSIGN', 'QUESTION',
  'EXCLAMATION', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
  'DOT', 'COMMA', 'SEMICOLON', 'COLON','DOLLAR','ID','NUMBER','BINARY','OCTAL'
  'HEX','NOTACAOCIENTIFICA','NUMBERFLOAT','ASPASSIMPLES','ASPASDUPLAS', 'STRING'] + list(reservadas.values())

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

def t_STRING(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    return t

def t_ID(t):
    r'[a-z][a-z0-9_]*'
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

def t_XOMENTARIOSIMPLES(t):
    r'//.*'
    pass

def t_BLOCODECOMENTARIO(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore  = ' \t' 


lexer = lex.lex()


#codigo  de exemplo em V para testar
codigo_v = """
fn soma(a int, b int) int {
	return a + b
}

fn main(){
	println('Hello World!')

    n_O_me := 20
    
	nome := 'Matheus'	// Variável imutável (seria o const do C)
	mut idade := 30		// Variável mutável (igual a uma variável comum no C)

	println('Nome: ${nome}')
	println('Idade: ${idade}')

	idade = 25
 
    idade = 'matheus'

	print('Idade atualizada: ${idade}\n')

	println('\n---------------------------------------\n')

	saldo := 100.50	// Padrão f64
	esta_ativo := true	// booleano
	letras := ['a', 'b', 'c']	// []rune (array de caracteres)

	println('Saldo: ${saldo}')
	println('Ativo: ${esta_ativo}')
	println('Primeira letra: ${letras[0]}')

	println('\n---------------------------------------\n')

	if idade < 25 {
		println('Idade menor que 25 anos')
	} else if idade == 25 {
		println('Idade igual a 25 anos')
	} else {
		println('Idade maior que 25 anos')
	}

	println('\n---------------------------------------\n')

	for i := 0; i < 5; i++ {
		println('Contador: ${i}')
	}
	
	numeros := [1,2,3,4,5]
	for i in numeros {
		println('Número: ${i}')
	}

	println('\n---------------------------------------\n')

	println('Função soma: ${soma(numeros[0],numeros[1])}')


}
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

#print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))
