#Dicionario que representa a tabela de simbolos.
symbolTable = []
INT = 'int'
FLOAT32 = 'float32'
FLOAT64 = 'float64'
BOOL = 'boolean'
STRING = 'string'
RUNETYPE = 'rune'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fn'
VARIABLE = 'var'
CONSTANTE = 'const'
SCOPE = 'scope'
MUTABLEVAR = 'mutvar'
IMUTABLEVAR = 'imutvar'
LENGTH = 'length'
OFFSET = 'offset'
MODULE = 'module' #imports
SP = 'sp'
# Se DEBUG = -1, imprime conteudo da tabela de símbolos após cada mudança
DEBUG = -1
Number = [INT,FLOAT32,FLOAT64]
inteiro = [INT]
real = [FLOAT32,FLOAT64]


curoffset = 0
def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()

def addModule(name):
    # Adiciona um módulo/import na tabela de símbolos
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: MODULE, TYPE: MODULE}
    printTable()

def addMutableVar(name, type, offset = None):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: MUTABLEVAR, TYPE : type, OFFSET: offset}
    printTable()

def addImutableVar(name, type, offset = None):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: IMUTABLEVAR, TYPE : type, OFFSET: offset}
    printTable()

def addConstVar(name, type, offset = None):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: CONSTANTE, TYPE : type, OFFSET: offset}
    printTable()

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}
    printTable()

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def getScope(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][SCOPE]
    return None

def currentScope():
    global symbolTable
    return symbolTable[-1]

def main():
    global DEBUG
    DEBUG = -1
    print('\n# Criando escopo main')
    beginScope('main')
    print ('\n# Adicionando Vinculavel funcao some')
    addFunction('some', ['a', INT, 'b', INT], INT)
    print('\n# Criando escopo some')
    beginScope('some')
    print('\n# Adicionando var a do tipo int')
    addMutableVar('a', INT)
    print('\n# Pegar escopo de var a')
    print(getScope('a'))
    print('\n# Adicionando var b do tipo int')
    addImutableVar('b', INT)
    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))
    print('\n# Consultando bindable')
    print(str(getBindable('some')))
    print('\n# Consultando bindable')
    print(str(getBindable('a')))
    print('\n# Consultando bindable')
    print(str(getBindable('b')))
    print('\n# Consultando escopo atual')
    print(str(currentScope()))
    print('\n# Removendo escopo some')
    endScope()

if __name__ == "__main__":
    main()