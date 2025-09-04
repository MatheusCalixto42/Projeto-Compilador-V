from Visitor import *
from SintaxeAbstrate import *
import SymbolTable as st


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
        multipleProgramItems.program_item.accept(self)
        if multipleProgramItems.program_items_recursao != None: #ISso é necessário??
            multipleProgramItems.program_items_recursao.accept(self)

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
            st.addMutableVar(varName, typeVar)

    def visitDeclarationMutableListLengthDefinition(self, listLengthDefinition):
        varName = listLengthDefinition.id
        typeVar = listLengthDefinition.type.accept(self)  
        length = listLengthDefinition.number              # tamanho da lista

        # Verifica se já existe uma variável com esse nome
        if st.getBindable(varName) != None:
            self.n_errors += 1
            print(f"Erro: O identificador '{varName}' já foi declarado.")
        else:
            st.addMutableVar(varName, typeVar)
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



def main():
    f = open("testeSemanticoV.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime erros semanticos encontrados")
    svisitor = SemanticVisitor(debug=-1)
    result.accept(svisitor)
    print(f"Foram encontrados {svisitor.getnerros()} erros")


if __name__ == "__main__":
    main()