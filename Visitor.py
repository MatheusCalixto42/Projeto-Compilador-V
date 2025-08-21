from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):

###################################################################
# Classes to visit the Abstract Syntax of Program
##################################################################

    def visitImportAndFuncDefinition(self,importAndFuncDefinition):
        importAndFuncDefinition.program_import.accept(self)
        importAndFuncDefinition.function_definition.accept(self)

    def visitSingleFuncDefinition(self,singleFuncDefinition):
        singleFuncDefinition.function_definition.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Import
################################################################## 

    def visitSequenceImports(self,sequenceImports):
        print('import', end=' ')
        print(sequenceImports.id, end=' ')
        sequenceImports.program_import.accept(self)

    def visitSingleImport(self,singleImport):
        print('import', end=' ')
        print(singleImport.id, end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Function Definition
##################################################################

    def visitFunctionVoid(self,functionVoid):
        global tab
        print('fn', end=' ', sep=' ')
        print(functionVoid.id, end=' ')
        print('(', end=' ')
        functionVoid.param.accept(self) #usar if para o caso de n ter parametro?
        print(')', end=' ')
        print('{')
        tab =  tab + 3
        functionVoid.block_statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
        functionVoid.function_definition.accept(self)

    def visitFunctionReturnType(self,functionReturnType):
        global tab
        print('fn', end=' ', sep=' ')
        print(functionReturnType.id, end=' ')
        print('(', end=' ')
        functionReturnType.param.accept(self)
        print(')', end=' ')
        functionReturnType.type.accept(self)
        print('{')
        tab =  tab + 3
        functionReturnType.block_statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
        functionReturnType.function_definition.accept(self)

    def visitFunctionMain(self,functionMain):
        global tab
        print('fn', end=' ', sep=' ')
        print('main', end=' ')
        print('(', end=' ')
        print(')', end=' ')
        print('{')
        tab =  tab + 3
        functionMain.block_statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', end=' ')
        functionMain.function_definition_without_main.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Function Definition without main
##################################################################

    def visitFunctionVoidWithoutMain(self,functionvoidwithoutmain):
        global tab
        print('fn', end = '', sep= '')
        print(functionvoidwithoutmain.id, end=' ')
        print('(', end=' ')
        functionvoidwithoutmain.param.accept(self)
        print(')', end=' ')
        print('{')
        tab =  tab + 3
        functionvoidwithoutmain.block_statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
        functionvoidwithoutmain.function_definition_without_main.accept(self)

    def visitFunctionReturnTypeWithoutMain(self,functionreturntypewithoutmain):
        global tab
        print('fn', end = '', sep= '')
        print(functionreturntypewithoutmain.id, end=' ')
        print('(', end=' ')
        functionreturntypewithoutmain.param.accept(self)
        print(')', end=' ')
        functionreturntypewithoutmain.type.accept(self)
        print('{')
        tab =  tab + 3
        functionreturntypewithoutmain.block_statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
        functionreturntypewithoutmain.function_definition_without_main.accept(self)

    def visitNoneFunction(self, noneFunction):
        pass

###################################################################
# Classes to visit the Abstract Syntax of Param
##################################################################

    def visitNoneParam(self,noneparam): #olhar isso
        pass
    
    def visitDescriptionParam(self,descriptionparam):
        print(descriptionparam.id, end=' ')
        descriptionparam.type.accept(self)

    def visitDescriptionParams(self,descriptionparams):
        descriptionparams.param.accept(self)
        descriptionparams.more_params.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of MoreParams
##################################################################    

    def visitMultipleParams(self,multipleparams):
        print(',', end=' ')
        multipleparams.param.accept(self)
        multipleparams.more_params.accept(self)

    def visitNoneParam(self, noneParam):
        pass

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

###################################################################
# Classes to visit the Abstract Syntax of BlockStatement
##################################################################     

    def visitBlockStatement(self,blockStatement):
        blockStatement.statement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Statement
##################################################################

    def visitVarStatement(self,varStatement):#var_statemnt
        varStatement.var_statement.accept(self)
        varStatement.statement.accept(self)
    
    def visitVarAssignment(self,varAssignment):
        varAssignment.var_assignment.accept(self)
        varAssignment.statement.accept(self)

    def visitFuncCallS(self,funcCall):
        funcCall.func_call.accept(self)
        funcCall.statement.accept(self)
    
    def visitIfStatement(self,ifStatement):
        ifStatement.if_statement.accept(self)
        ifStatement.statement.accept(self)

    def visitForStatement(self,forStatement):
        forStatement.for_statement.accept(self)
        forStatement.statement.accept(self)

    def visitReturnStatement(self,returnStatement):
        returnStatement.return_statement.accept(self)

    def visitNoneStatement(self, noneStatement):
        pass

 ###################################################################
# Classes to visit the Abstract Syntax of Var Statement
##################################################################   

    def visitDeclarationImutable(self,declarationImutable):
        declarationImutable.declaration_imutable.accept(self)

    def visitMutableDeclaration(self,mutableDeclaration):
        print('mut', end=' ',sep=' ')
        print(mutableDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('\n')
        mutableDeclaration.expression.accept(self)
    
    def visitConstantDeclaration(self,constantDeclaration):
        print('const', end=' ',sep=' ')
        print(constantDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        constantDeclaration.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Var Assignment
##################################################################

    def visitVarModification(self,varModification):
        print(varModification.id, end=' ')
        print('=', end=' ',sep=' ') 
        varModification.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Func Call
##################################################################

    def visitFuncCompoundParams(self,funcCompoundParams):
        print(funcCompoundParams.id, end=' ')
        print('(', end=' ')
        funcCompoundParams.id_list.accept(self)
        print(')', end=' ')

    def visitFuncNoParams(self,funcNoParams):
        print(funcNoParams.id, end=' ')
        print('(', end=' ')
        print(')', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of If Statement
##################################################################

    def visitListId(self,listId):
        listId.expression.accept(self)
        listId.more_expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of More Expression
##################################################################    

    def visitPlusExpres(self,plusExpres):
        print(',' , end=' ', sep=' ')
        plusExpres.expression.accept(self)
        plusExpres.more_expression.accept(self)
    
    def visitNoneExpression(self,noneExpression):
        pass

###################################################################
# Classes to visit the Abstract Syntax of If Statement
##################################################################

    def visitOnlyIf(self,onlyIf):
        global tab
        print('if', end=' ', sep=' ')
        onlyIf.expressionrelational.accept(self)
        print('{')
        tab =  tab + 3
        onlyIf.blockstatement.accept(self)
        tab =  tab - 3
        print(blank(),'}', sep=' ')

    def visitIfAndElse(self,ifAndElse):
        global tab
        print('if', end=' ', sep=' ')
        ifAndElse.expressionrelational.accept(self)
        print('{')
        tab =  tab + 3
        ifAndElse.blockstatement.accept(self)
        tab =  tab - 3
        print(blank(), '}',sep=' ')
        ifAndElse.elseV.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Else
##################################################################

    def visitElseIf(self,elseIf):
        print('else', end=' ', sep=' ')
        elseIf.if_statement.accept(self)

    def visitOnlyElse(self,onlyElse):
        global tab
        print('else', end=' ', sep=' ')
        print('{')
        tab =  tab + 3   
        onlyElse.blockstatement.accept(self)
        tab =  tab - 3
        print(blank(),'}', sep=' ')

###################################################################
# Classes to visit the Abstract Syntax of For
##################################################################

    def visitForEach(self,forEach):
        global tab
        print('for', end=' ', sep=' ')
        print(forEach.id, end=' ')
        print('in', end=' ', sep=' ')
        forEach.expression.accept(self)
        print('{')
        tab =  tab + 3
        forEach.blockstatement.accept(self)
        tab =  tab - 3
        print(blank(),'}', sep=' ')

    def visitConventionalFor(self,conventionalFor):
        global tab
        print('for', end=' ', sep=' ')
        conventionalFor.declarationmutable.accept(self)
        print(';', end=' ', sep=' ')
        conventionalFor.expressionrelational.accept(self)
        print(';', end=' ', sep=' ')
        conventionalFor.increment.accept(self)
        print('{')
        tab =  tab + 3
        conventionalFor.statement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
       
       

    def visitOnlyExpressionRelationalFor(self,onlyExpressionRelationalFor):
        global tab
        print('for', end=' ', sep=' ')
        onlyExpressionRelationalFor.expressionrelational.accept(self)
        print('{')
        tab =  tab + 3
        onlyExpressionRelationalFor.blockstatement.accept(self)
        tab =  tab - 3
        print(blank(), '}', sep=' ')
        

###################################################################
# Classes to visit the Abstract Syntax of Imutable Declaration
##################################################################

    def visitIdImutable(self,idImutable):
        print(idImutable.id, end=' ')
        print(':=', end=' ',sep=' ')
        idImutable.expression.accept(self)
        print()
        

###################################################################
# Classes to visit the Abstract Syntax of Return Statement
##################################################################    

    def visitReturnExpression(self,returnExpression):
        print('return', end=' ')
        if(returnExpression.expression == None):
            pass

        returnExpression.expression.accept(self)
        

###################################################################
# Classes to visit the Abstract Syntax of Expression
##################################################################

    def visitExpressionPlus(self,expressionPlus):
        expressionPlus.expression.accept(self)
        print('+', end=' ')
        expressionPlus.term.accept(self)

    def visitExpressionMinus(self,expressionMinus):
        expressionMinus.expression.accept(self)
        print('-', end=' ')
        expressionMinus.term.accept(self)

    def visitSingleTerm(self,singleTerm):
        singleTerm.term.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Relational Expression
##################################################################

    def visitExpressionRelationalEqual(self,expressionRelationalEqual):
        expressionRelationalEqual.expression1.accept(self)
        print('==', end=' ')
        expressionRelationalEqual.expression2.accept(self)

    def visitExpressionRelationalNotEqual(self,expressionRelationalNotEqual):
        expressionRelationalNotEqual.expression1.accept(self)
        print('!=', end=' ')
        expressionRelationalNotEqual.expression2.accept(self)

    def visitExpressionRelationalLessThan(self,expressionRelationalLessThan):
        expressionRelationalLessThan.expression1.accept(self)
        print('<', end=' ')
        expressionRelationalLessThan.expression2.accept(self)

    def visitExpressionRelationalGreaterThan(self,expressionRelationalGreaterThan):
        expressionRelationalGreaterThan.expression1.accept(self)
        print('>', end=' ')
        expressionRelationalGreaterThan.expression2.accept(self)

    def visitExpressionRelationalLessThanOrEqual(self,expressionRelationalLessThanOrEqual):
        expressionRelationalLessThanOrEqual.expression1.accept(self)
        print('<=', end=' ')
        expressionRelationalLessThanOrEqual.expression2.accept(self)

    def visitExpressionRelationalGreaterThanOrEqual(self,expressionRelationalGreaterThanOrEqual):
        expressionRelationalGreaterThanOrEqual.expression1.accept(self)
        print('>=', end=' ')
        expressionRelationalGreaterThanOrEqual.expression2.accept(self)

    def visitExpressionRelationalAnd(self,expressionRelationalAnd):
        expressionRelationalAnd.expression1.accept(self)
        print('&&', end=' ')
        expressionRelationalAnd.expression2.accept(self)

    def visitExpressionRelationalOr(self,expressionRelationalOr):
        expressionRelationalOr.expression1.accept(self)
        print('||', end=' ')
        expressionRelationalOr.expression2.accept(self)

    def visitExpressionRelationalNot(self,expressionRelationalNot):
        print('!', end=' ')
        expressionRelationalNot.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Term
##################################################################

    def visitMultiplication(self,multiplication):
        multiplication.term.accept(self)
        print('*', end=' ')
        multiplication.factor.accept(self)

    def visitDivision(self,division):
        division.term.accept(self)
        print('/', end=' ')
        division.factor.accept(self)
    
    def visitMod(self,mod):
        mod.term.accept(self)
        print('%', end=' ')
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

###################################################################
# Classes to visit the Abstract Syntax of Increment
##################################################################

    def visitInc(self, inc):
        print(inc.id, end=' ')
        print('++', end=' ')

    def visitDec(self, dec):
        print(dec.id, end=' ')
        print('--', end=' ')

def main():
    f = open("teste.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(start='program')
    result = parser.parse(debug=True)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

if __name__ == "__main__":
    main()
