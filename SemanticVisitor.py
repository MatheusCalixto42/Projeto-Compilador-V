from Visitor import *
import SymbolTable as st

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT32 or type2 == st.FLOAT32):
            return st.FLOAT32
        elif (type1 == st.FLOAT64 or type2 == st.FLOAT64):
            return st.FLOAT64
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    
    def __init__(self):
        self.printer = Visitor()
        self.n_errors = 0
        self.main_defined = False
        st.beginScope('main')

    def visitImportAndFuncDefinition(self, importAndFuncDefinition):
        importAndFuncDefinition.program_import.accept(self) 
        importAndFuncDefinition.program_items.accept(self)

    def visitProgramItems(self, programItems):
        programItems.program_items.accept(self)

    def visitSequenceImports(self, sequenceImports):
        idName = sequenceImports.id
        if st.getBindable(idName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{idName}' já foi declarado.")
        else:
            st.addModule(idName)
        sequenceImports.program_import.accept(self)

    def visitSingleImport(self, singleImport):
        idName = singleImport.id
        if st.getBindable(idName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{idName}' já foi declarado.")
        else:
            st.addModule(idName)

    def visitMultipleProgramItems(self, multipleProgramItems):
        multipleProgramItems.item.accept(self)
        if multipleProgramItems.items_recursao != None: #ISso é necessário??
            multipleProgramItems.items_recursao.accept(self)

    def visitNoneItems(self, noneItems):
        pass

    def visitConstanteDeclaration(self, constanteDeclaration):
        constanteDeclaration.constante.accept(self)

    def visitFunctionDeclaration(self, functionDeclaration):
        functionDeclaration.function.accept(self)

    def visitConstanteDeclarationRule(self, constanteDeclarationRule):
        idName = constanteDeclarationRule.id
        typeExp = constanteDeclarationRule.expression.accept(self)  
        if st.getBindable(idName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{idName}' já foi declarado.")
        else:
            st.addImutableVar(idName, typeExp)
        return typeExp
    
    def visitFunctionVoid(self, functionVoid):
        func_id = functionVoid.id
        params = []
        if functionVoid.param is not None: #isso faz com que n precise de classes com nd para expressar vazio?
            params = functionVoid.param.accept(self)
        
        st.addFunction(func_id, params, None) 

        st.beginScope(func_id)
        for i in range(0, len(params),2):
            st.addImutableVar(params[i], params[i+1])

        functionVoid.block_statement.accept(self)
        st.endScope()

    def visitFunctionReturnType(self, functionReturnType):
        func_id = functionReturnType.id
        params = []
        if functionReturnType.param is not None:
            params = functionReturnType.param.accept(self)

        typeFunc = functionReturnType.type.accept(self)
        st.addFunction(func_id, params, typeFunc)

        st.beginScope(func_id)
        for i in range(0, len(params),2):
            st.addImutableVar(params[i], params[i+1])

        functionReturnType.block_statement.accept(self)
        st.endScope()

    def visitFunctionMain(self, functionMain):
        func_id = functionMain.id
        params = []

        if self.main_defined:
            self.n_errors += 1
            print(f"Erro: A função 'main' já foi definida.")
        else:
            self.main_defined = True
        st.addFunction(func_id, [], None)
        st.beginScope(func_id)
        functionMain.block_statement.accept(self)
        st.endScope()

    def visitDescriptionParams(self, descriptionParams):
        param_type = descriptionParams.param.accept(self)
        params = [param_type
                  ]
        more_params = descriptionParams.more_params.accept(self)
        if more_params:
            params.extend(more_params) #Aqui adiciona os parâmetros adicionais
        return params

    def visitMultipleParams(self, multipleParams):
        param_type =multipleParams.param.accept(self)
        params = [param_type]
        moreParams = multipleParams.more_params.accept(self)
        if moreParams:
            params.extend(moreParams)
        return params
    
    def visitNoneParam(self, noneParam):
        return []
    
    def visitDescriptionParam(self, descriptionParam):
        idName = descriptionParam.id
        typeParam = descriptionParam.type.accept(self)

        if st.lookup(idName): #Verifica se ja existe no escopo atual ou superior
            self.n_errors += 1
            print(f"Erro: O identificador '{idName}' já foi declarado.")
        else:
            st.addImutableVar(idName, typeParam)
        return typeParam
    

    def visitBlockStatement(self, blockStatement):
        if blockStatement.statements != None:
            blockStatement.statements.accept(self)
    
    def visitNoneBlockStatement(self, noneBlockStatement):
        pass

    def visitMultipleStatement(self, multipleStatement):
        multipleStatement.statement.accept(self)
        multipleStatement.statements.accept(self)

    def visitSingleStatement(self, singleStatement):
        singleStatement.statement.accept(self)

########################################################
#Semantico para Statement
#######################################################

    def visitVarStatement(self, varStatement):
        varStatement.var_statement.accept(self)

    def visitVarAssignment(self, varAssignment):
        varAssignment.var_assignment.accept(self)

    def visitListStatement(self, listStatement):
        listStatement.list_statement.accept(self)

    def visitListAssignment(self, listAssignment):
        listAssignment.list_assignment.accept(self)

    def visitFuncCallS(self, funcCallS):
        funcCallS.func_call.accept(self)

    def visitIfStatement(self, ifStatement):
        ifStatement.if_statement.accept(self)

    def visitForStatement(self, forStatement):
        forStatement.for_statement.accept(self)

    def visitBreakStatement(self, breakStatement):
        breakStatement.break_statement.accept(self)
    
    def visitReturnStatement(self, returnStatement):
        returnStatement.return_statement.accept(self)

    def visitIncrementStatement(self, incrementStatement):
        incrementStatement.increment_statement.accept(self)

    def visitAssignmentStatement(self, assignment_statement):
        assignment_statement.assignment_statement.accept(self)

#########################################################
# Semantico para Var Statement
########################################################

    def visitDeclarationImutable(self, declarationImutable):
        declarationImutable.declaration_imutable.accept(self)

    def visitMutableDeclaration(self, mutableDeclaration):
        varName = mutableDeclaration.id
        typeVar = mutableDeclaration.expression.accept(self)
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addMutableVar(varName, typeVar)

    def visitConstantDeclaration(self, constantDeclaration):
        varName = constantDeclaration.id
        typeVar = constantDeclaration.expression.accept(self)   #self.visit(constantDeclaration.expression)
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addConstVar(varName, typeVar)

##########################################################
#Semantico para Var Assignment
#########################################################

    def visitVarModification(self, varModification): #tenho que mudar algo na tabela?? Guardar o novo valor??
        varName = varModification.id
        typeVar = varModification.expression.accept(self) 
        if st.getBindable(varName) == None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' não foi declarado.")
        else:
            bindable = st.getBindable(varName)
            if bindable[st.BINDABLE] == "IMUTABLEVAR" or bindable[st.BINDABLE] == "CONSTANTE":
                self.n_errors += 1
                print(f"Erro: A variável '{varName}' é imutável e não pode ser modificada.")
            else:
                if bindable[st.TYPE] != typeVar:
                    self.n_errors += 1
                    print(f"Erro: Tipo incompatível na atribuição à variável '{varName}'. Esperado '{bindable[TYPE]}', mas recebeu '{typeVar}'.")


##########################################################
#Semantico para List Statement
#########################################################

    def visitDeclarationImutableList(self, declarationImutableList):
        declarationImutableList.declaration_imutable_list.accept(self)

    def visitDeclarationMutableList(self, declarationMutableList): #o que pode mudar por ser uma lista? alguma modificação na tabela de simbolos?
        varName = declarationMutableList.id
        typeVar = declarationMutableList.id_list.accept(self) #possivel problema--> verificar cada tipo de var dentro??
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addArray(varName, typeVar)

    def visitDeclarationMutableListLengthDefinition(self, listLengthDefinition):
        varName = listLengthDefinition.id
        typeVar = listLengthDefinition.type.accept(self)  
        length = listLengthDefinition.number              # tamanho da lista

        # Verifica se já existe uma variável com esse nome
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addArray(varName, typeVar)
            bindable = st.getBindable(varName) # Fiz um campo tamanho para a lista, é necessario??
            bindable['length'] = length

##########################################################
#Semantico para List Assignment
#########################################################

    def visitListModification(self, listModification):
        varName = listModification.id
        index = listModification.number
        exprType = listModification.expression.accept(self)

        bindable = st.getBindable(varName)
        if bindable is None:
            self.n_errors += 1
            print(f"Erro: A lista '{varName}' não foi declarada.")

        if bindable[st.BINDABLE] != "MUTABLEVAR":
            self.n_errors += 1
            print(f"Erro: '{varName}' não é uma lista mutável e não pode ser modificada.")

        if index < 0 or index >= bindable[st.LENGTH]:
            self.n_errors += 1
            print(f"Erro: Índice {index} fora dos limites da lista '{varName}'.")
            return
        
        if bindable[st.TYPE] != exprType:
            self.n_errors += 1
            print(f"Erro: Tipo incompatível na atribuição ao elemento da lista '{varName}'. Esperado '{bindable[st.TYPE]}', mas recebeu '{exprType}'.")

##########################################################
#Semantico para Declaration Imutable List
#########################################################
    
    def visitDeclarationImutableListRule(self, declarationImutableListRule):
        varName = DeclarationImutableListRule.id
        typeList = declarationImutableListRule.id_list.accept(self)
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addImutableVar(varName, typeList)

##########################################################
#Semantico para Func Call
#########################################################
    def visitFuncCompoundParams(self, funcCompoundParams):
        bindable = st.getBindable(funcCompoundParams.id)

        if(funcCompoundParams.id is "println" or funcCompoundParams.id is "print"):
            funcCompoundParams.params.accept(self)
            return st.VOID

        elif (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = funcCompoundParams.params.accept(self)
            if (list(bindable[st.PARAMS][1::2]) == typeParams):
                return bindable[st.TYPE]
            funcCompoundParams.accept(self.printer)
            self.n_errors+=1 
            print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
            print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
        else:
            funcCompoundParams.accept(self.printer)
            self.n_errors+=1 
            print("\n\t[Erro] Chamada de funcao invalida. O id", funcCompoundParams.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None
    
    def visitFuncNoParams(self, funcNoParams):
        bindable = st.getBindable(funcNoParams.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        funcNoParams.accept(self.printer)
        self.n_errors+=1 
        print("\n\t[Erro] Chamada de funcao invalida. O id", funcNoParams.id, "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None
    
    def visitFuncCallList(self, funcCallList):
        funcCallList.funcCallList.accept(self)

##########################################################
#Semantico para Func Call List
#########################################################

    def visitFuncCallListAll(self, funcCallListAll):
        FuncName = funcCallListAll.id
    
        bindable = st.getBindable(FuncName)
        if bindable is None:
            self.n_errors += 1
            print(f"\n\t[Erro] Identificador '{FuncName}' não foi declarado antes do uso.\n")
            return None

        if bindable[st.BINDABLE] != st.ARRAY:
            self.n_errors += 1
            print(f"\n\t[Erro] O identificador '{FuncName}' não é indexável (esperado array ou lista).\n")
            return None
        # Se esta tudo certo retorna o tipo dos elementos do array
        return bindable[st.TYPE]
    
    def visitFuncCallListRange(self, funcCallRange):
        FuncName = funcCallRange.id
        index1 = funcCallRange.number
        index2 = funcCallRange.number2

        bindable = st.getBindable(FuncName)
        if bindable is None:
            self.n_errors += 1
            print(f"\n\t[Erro] Identificador '{FuncName}' não foi declarado antes do uso.\n")
            return None
        
        if bindable[st.BINDABLE] != "ARRAY":
            self.n_errors += 1
            print(f"Erro: '{FuncName}' não é um array.")
            return None
        
        if index1 < 0 or index2 >= bindable[st.LENGTH]:
            self.n_errors += 1
            print(f"Erro: Índice  fora dos limites do array '{FuncName}'.")
            return None
        
##########################################################
#Semantico para id list
#########################################################

    def visitListId(self, listId):
        firstType = listId.expression.accept(self)

        restTypes = []
        if listId.more_expression != None:
            restTypes = listId.more_expression.accept(self)

        if firstType != restTypes:
            self.n_errors += 1
            print("[Erro] Tipos diferentes entre os parametros")
        # Retorna a lista de tipos
        return [firstType] + restTypes
    
##########################################################
#Semantico para more expression
#########################################################

    def visitPlusExpres(self, plusExpres):
        firstType = plusExpres.expression.accept(self)

        restTypes = []
        if plusExpres.more_expression != None:
            restTypes = plusExpres.more_expression.accept(self)

        if firstType != restTypes:
            self.n_errors += 1
            print("[Erro] Tipos diferentes entre os parametros")
        # Retorna a lista de tipos
        return [firstType] + restTypes
    
    def visitNoneExpression(self, noneExpression):
        pass

##########################################################
#Semantico para if statement 
#########################################################

    def visitOnlyIf(self, onlyIf):
        typeExp = onlyIf.expressionrelational.accept(self)
        if (typeExp != st.BOOL):
            onlyIf.expressionrelational.accept(self.printer)
            self.n_errors+=1 
            print ("\n\t[Erro] A expressao ", end='')
            onlyIf.expressionrelational.accept(self.printer)
            print(" eh", typeExp, end='')
            print (". Deveria ser boolean\n")
        onlyIf.blockstatement.accept(self)

    def visitIfAndElse(self, ifAndElse):
        typeExp = ifAndElse.expressionrelational.accept(self)
        if (typeExp != st.BOOL):
            ifAndElse.expressionrelational.accept(self.printer)
            self.n_errors+=1 
            print ("\n\t[Erro] A expressao ", end='')
            ifAndElse.expressionrelational.accept(self.printer)
            print(" eh", typeExp, end='')
            print (". Deveria ser boolean\n")
        ifAndElse.blockstatement.accept(self)
        ifAndElse.elseV.accept(self)

##########################################################
#Semantico para else  
#########################################################  

    def visitElseIf(self,elseIf):  
        typeExp = elseIf.if_statement.accept(self)
        if (typeExp != st.BOOL):
            elseIf.expressionrelational.accept(self.printer)
            self.n_errors+=1 
            print ("\n\t[Erro] A expressao ", end='')
            elseIf.expressionrelational.accept(self.printer)
            print(" eh", typeExp, end='')
            print (". Deveria ser boolean\n")
    
    def visitOnlyElse(self,onlyElse):
        onlyElse.blockstatement.accept(self)
    

###################################################################
# Semantico do For
##################################################################
#
    def visitForEach(self,forEach):
        
        idName = forEach.id
        typeExp = forEach.expression.accept(self)

        if typeExp not in st.Numero and typeExp != st.STRING:
            self.n_errors += 1
            print("Erro: A expressão do for deve ser numérica ou string")
            forEach.expression.accept(self.printer)

        st.beginScope('forEach')

        if st.getBindable(idName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{idName}' já foi declarado.")
        else:
            st.addImutableVar(idName, typeExp)
        
        forEach.blockstatement.accept(self)

        st.endScope()
#

    def visitConventionalFor(self,conventionalFor):
        st.beginScope('conventionalFor')
        conventionalFor.declarationimutable.accept(self)
        typeExp = conventionalFor.expressionrelational.accept(self)
        if(typeExp != st.BOOL):
            print("Erro: Expressão de controle do for deve ser booleana")
            conventionalFor.expressionrelational.accept(self.printer)
        conventionalFor.increment.accept(self)
        conventionalFor.statement.accept(self)
        st.endScope()
       
#
    def visitOnlyExpressionRelationalFor(self,onlyExpressionRelationalFor):
        typeExp = onlyExpressionRelationalFor.expressionrelational.accept(self)
        if(typeExp != st.BOOL):
            print("Erro: Expressão de controle do for deve ser booleana")
            onlyExpressionRelationalFor.expressionrelational.accept(self.printer)
        onlyExpressionRelationalFor.blockstatement.accept(self)


##################### Limite

###################################################################
# Semantico do Imutable Declaration
##################################################################

    def visitIdImutable(self,idImutable):
        varName = idImutable.id
        typeVar = idImutable.expression.accept(self)
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addImutableVar(varName, typeVar)
        idImutable.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Break Statement
##################################################################    

    def visitOnlyBreak(self, onlyBreak):
        if st.currentScope != "forEach" or st.currentScope != "conventionalFor" or st.currentScope != "expressionFor":
            self.n_errors += 1
            print("\n\t[Erro] 'break' usado fora de um laço.\n")

###################################################################
# Classes to visit the Abstract Syntax of Return Statement
##################################################################    

    def visitReturnExpression(self,returnExpression):

        if(returnExpression.expression == None):
            pass

        returnExpression.expression.accept(self)
        

###################################################################
# Classes to visit the Abstract Syntax of Expression
##################################################################

    def visitExpressionPlus(self,expressionPlus):
        expressionPlus.expression.accept(self)
      
        expressionPlus.term.accept(self)

    def visitExpressionMinus(self,expressionMinus):
        expressionMinus.expression.accept(self)
        
        expressionMinus.term.accept(self)

    def visitSingleTerm(self,singleTerm):
        singleTerm.term.accept(self)

    def visitExpressionIncrement(self, expressionIncrement):
     
        expressionIncrement.increment.accept(self)
        

    def visitExpressionFuncCall(self, expressionFuncCall):
        expressionFuncCall.funcCall.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Relational Expression
##################################################################

    def visitExpressionRelationalEqual(self,expressionRelationalEqual):
        expressionRelationalEqual.expression1.accept(self)
        
        expressionRelationalEqual.expression2.accept(self)

    def visitExpressionRelationalNotEqual(self,expressionRelationalNotEqual):
        expressionRelationalNotEqual.expression1.accept(self)
        
        expressionRelationalNotEqual.expression2.accept(self)

    def visitExpressionRelationalLessThan(self,expressionRelationalLessThan):
        expressionRelationalLessThan.expression1.accept(self)
        
        expressionRelationalLessThan.expression2.accept(self)

    def visitExpressionRelationalGreaterThan(self,expressionRelationalGreaterThan):
        expressionRelationalGreaterThan.expression1.accept(self)
        
        expressionRelationalGreaterThan.expression2.accept(self)

    def visitExpressionRelationalLessThanOrEqual(self,expressionRelationalLessThanOrEqual):
        expressionRelationalLessThanOrEqual.expression1.accept(self)
        
        expressionRelationalLessThanOrEqual.expression2.accept(self)

    def visitExpressionRelationalGreaterThanOrEqual(self,expressionRelationalGreaterThanOrEqual):
        expressionRelationalGreaterThanOrEqual.expression1.accept(self)
        
        expressionRelationalGreaterThanOrEqual.expression2.accept(self)

    def visitExpressionRelationalAnd(self,expressionRelationalAnd):
        expressionRelationalAnd.expression1.accept(self)
        
        expressionRelationalAnd.expression2.accept(self)

    def visitExpressionRelationalOr(self,expressionRelationalOr):
        expressionRelationalOr.expression1.accept(self)
        
        expressionRelationalOr.expression2.accept(self)

    def visitExpressionRelationalNot(self,expressionRelationalNot):
        
        expressionRelationalNot.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Term
##################################################################

    def visitMultiplication(self,multiplication):
        multiplication.term.accept(self)
        
        multiplication.factor.accept(self)

    def visitDivision(self,division):
        division.term.accept(self)
        
        division.factor.accept(self)
    
    def visitMod(self,mod):
        mod.term.accept(self)
        
        mod.factor.accept(self)
    
    def visitOnlyFactor(self,onlyFactor):
        onlyFactor.factor.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Factor
##################################################################

    def visitFactorID(self,factorID):
        print(factorID.id, end=' ')

    def visitFactorNumber(self,factorNumber):
        print(factorNumber.number, end=' ')

    def visitFactorNumberFloat(self, factorNumberFloat):
        print(factorNumberFloat.numberfloat, end=' ')

    def visitFactorString(self,factorString):
        print(factorString.string, end=' ')

    def visitFactorTrue(self,factorTrue):
        print(factorTrue.true, end=' ')
    
    def visitFactorFalse(self,factorFalse):
        print(factorFalse.false, end=' ')

    def visitFactorRune(self,factorRune):
        print(factorRune.rune, end=' ')

    def visitFactorExpression(self,factorExpression):
        print('(', end=' ')
        factorExpression.expression.accept(self)
        print(')', end=' ')

    def visitFactorList(self, factorList):
        print(factorList.id, end=' ')
        print('[', end=' ', sep=' ')
        print(factorList.number, end = ' ')
        print(']', end=' ', sep=' ')

    def visitFactorCientificNotation(self, cientific_notation):
        print(cientific_notation.cientificNotation, end=' ')

    def visitFactorBinary(self, binary):
        print(binary.factorBinary, end=' ')

    def visitFactorOctal(self, octal):
        print(octal.factorOctal, end=' ')

    def visitFactorHex(self, hex):
        print(hex.factorHex, end=' ')

    def visitFactorInterpolationString(self, factorInterpolationString):
        print(factorInterpolationString.interpolationString, end=' ')

    def visitFactorSizeOfExpression(self, factorSizeofExpression):
        factorSizeofExpression.sizeofexpression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Size of Expression
##################################################################

    def visitSizeOfExpression(self, sizeOfExpression):
       
        sizeOfExpression.expression.accept(self)
        

    def visitSizeOfType(self, sizeOfType):
        
        sizeOfType.type.accept(self)
        

###################################################################
# Classes to visit the Abstract Syntax of Increment
##################################################################

    def visitInc(self, inc):
        print(blank(), inc.id + '++', end=' ')

    def visitDec(self, dec):
        print(blank(), dec.id + '--', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Assignment
##################################################################

    def visitMaisIgual(self, mais_igual):
        
        mais_igual.expression.accept(self)

    def visitMenosIgual(self, menos_igual):
        
        menos_igual.expression.accept(self)
    
    def visitMultiIgual(self, multi_igual):
        
        multi_igual.expression.accept(self)

    def visitDivIgual(self, div_igual):
        
        div_igual.expression.accept(self)

    def visitModIgual(self, mod_igual):
        
        mod_igual.expression.accept(self)

    def visitAndIgual(self, and_igual):
        
        and_igual.expression.accept(self)

    def visitOrIgual(self, or_igual):
        
        or_igual.expression.accept(self)

    def visitXORIgual(self, xor_igual):
        
        xor_igual.expression.accept(self)

    def visitDeslocaEsqIgual(self, desloca_esq_igual):
        
        desloca_esq_igual.expression.accept(self)

    def visitDeslocaDirIgual(self, desloca_dir_igual):
        
        desloca_dir_igual.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Type
##################################################################

    def visitIntV(self,intV):
        print(intV.intv, end=' ')

    def visitF32(self,f32):
        print(f32.f32, end=' ')

    def visitF64(self,f64):
        print(f64.f64, end=' ')

    def visitRune(self,rune):
        print(rune.rune, end=' ')

    def visitString(self,string):
        print(string.string, end=' ')
    
    def visitBoolV(self,boolV):
        print(boolV.boolv, end=' ')


def main():
    f = open("testeSemanticoV.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime erros semanticos encontrados")
    svisitor = SemanticVisitor()
    svisitor = SemanticVisitor()
    result.accept(svisitor)
    print(f"Foram encontrados {svisitor.n_errors} erros")


if __name__ == "__main__":
    main()