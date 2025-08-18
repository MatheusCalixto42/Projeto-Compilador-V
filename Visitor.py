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
        print('fn', end=' ', sep=' ')
        print(functionVoid.id, end=' ')
        print('(', end=' ')
        functionVoid.param.accept(self) #usar if para o caso de n ter parametro?
        print(')', end=' ')
        print('{'+ blank(), end=' ')
        functionVoid.block_statement.accept(self)
        print('}', end=' ')
        functionVoid.function_definition.accept(self)

    def visitFunctionReturnType(self,functionReturnType):
        print('fn', end=' ', sep=' ')
        print(functionReturnType.id, end=' ')
        print('(', end=' ')
        functionReturnType.param.accept(self)
        print(')', end=' ')
        functionReturnType.type.accept(self)
        print('{'+ blank(), end=' ')
        functionReturnType.block_statement.accept(self)
        print('}', end=' ')
        functionReturnType.function_definition.accept(self)

    def visitFunctionMain(self,functionMain):
        print('fn', end=' ', sep=' ')
        print('main', end=' ')
        print('(', end=' ')
        print(')', end=' ')
        print('{' + blank(), end=' ')
        functionMain.block_statement.accept(self)
        print('}', end=' ')
        functionMain.function_definition_without_main.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Function Definition without main
##################################################################

    def visitFunctionVoidWithoutMain(self,functionvoidwithoutmain):
        functionvoidwithoutmain.id.accept(self)
        functionvoidwithoutmain.param.accept(self)
        functionvoidwithoutmain.block_statement.accept(self)
        functionvoidwithoutmain.function_definition_without_main.accept(self)

    def visitFunctionReturnTypeWithoutMain(self,functionreturntypewithoutmain):
        functionreturntypewithoutmain.id.accept(self)
        functionreturntypewithoutmain.type.accept(self)
        functionreturntypewithoutmain.block_statement.accept(self)
        functionreturntypewithoutmain.function_definition_without_main.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Param
##################################################################

    def visitNoneParam(self,noneparam): #olhar isso
        pass
    
    def visitDescriptionParam(self,descriptionparam):
        descriptionparam.id.accept(self)
        descriptionparam.type.accept(self)

    def visitDescriptionParams(self,descriptionparams):
        descriptionparams.param.accept(self)
        descriptionparams.more_params.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of MoreParams
##################################################################    

    def visitMultipleParams(self,multipleparams):
        multipleparams.param.accept(self)
        multipleparams.more_params.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Type
##################################################################

    def visitIntV(self,intV):
        intV.int.accept(self)

    def visitF32(self,f32):
        f32.f32.accept(self)

    def visitF64(self,f64):
        f64.f64.accept(self)

    def visitRune(self,rune):
        rune.rune.accept(self)

    def visitString(self,string):
        string.string.accept(self)
    
    def visitBoolV(self,boolV):
        boolV.bool.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Block Statement
##################################################################

    def visitVarDeclaration(self,varDeclaration):
        varDeclaration.var_statament.accept(self)
    
    def visitVarAssignment(self,varAssignment):
        varAssignment.var_assignment.accept(self)
    
    def visitIfStatement(self,ifStatement):
        ifStatement.if_statement.accept(self)

    def visitForStatement(self,forStatement):
        forStatement.for_statement.accept(self)

    def visitReturnStatement(self,returnStatement):
        returnStatement.return_statement.accept(self)

 ###################################################################
# Classes to visit the Abstract Syntax of Var Statement
##################################################################   

    def visitDeclarationImmutable(self,declarationImmutable):
        declarationImmutable.declaration_immutable.accept(self)

    def visitMutableDeclaration(self,mutableDeclaration):
        mutableDeclaration.mut.accept(self)
        mutableDeclaration.id.accept(self)
        mutableDeclaration.expression.accept(self)
    
    def visitConstantDeclaration(self,constantDeclaration):
        constantDeclaration.const.accept(self)
        constantDeclaration.id.accept(self)
        constantDeclaration.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Var Assignment
##################################################################

    def visitVarModification(self,varModification):
        varModification.id.accept(self)
        varModification.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Func Call
##################################################################

    def visitFuncCompoundParams(self,funcCompoundParams):
        funcCompoundParams.id.accept(self)
        funcCompoundParams.id_list.accept(self)

    def visitFuncNoParams(self,funcNoParams):
        funcNoParams.id.accept(self)
    
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
        plusExpres.expression.accept(self)
        plusExpres.more_expression.accept(self)
    
    def visitNoneExpression(self,noneExpression):
        pass

###################################################################
# Classes to visit the Abstract Syntax of If Statement
##################################################################

    def visitOnlyIf(self,onlyIf):
        onlyIf.expressionrelational.accept(self)
        onlyIf.blockstatement.accept(self)
    
    def visitIfAndElse(self,ifAndElse):
        ifAndElse.expressionrelational.accept(self)
        ifAndElse.blockstatement.accept(self)
        ifAndElse.elseV.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Else
##################################################################

    def visitElseIf(self,elseIf):
        elseIf.if_statement.accept(self)

    def visitOnlyElse(self,onlyElse):
        onlyElse.blockstatement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of For
##################################################################

    def visitForEach(self,forEach):
        forEach.id.accept(self)
        forEach.expression.accept(self)
        forEach.blockstatement.accept(self)

    def visitConventionalFor(self,conventionalFor):
        conventionalFor.declarationmutable.accept(self)
        conventionalFor.expressionrelational.accept(self)
        conventionalFor.increment.accept(self)
        conventionalFor.block_statement.accept(self)

    def visitOnlyExpressionRelationalFor(self,onlyExpressionRelationalFor):
        onlyExpressionRelationalFor.expressionrelational.accept(self)
        onlyExpressionRelationalFor.blockstatement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Imutable Declaration
##################################################################

    def visitIdImutable(self,idImutable):
        idImutable.id.accept(self)
        idImutable.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Return Statement
##################################################################    

    def visitReturnExpression(self,returnExpression):
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

    def visitRelationalNot(self,relationalNot):
        relationalNot.expression.accept(self)

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
        factorID.id.accept(self)

    def visitFactorNumber(self,factorNumber):
        factorNumber.number.accept(self)
    
    def visitFactorString(self,factorString):
        factorString.string.accept(self)

    def visitFactorTrue(self,factorTrue):
        factorTrue.true.accept(self)
    
    def visitFactorFalse(self,factorFalse):
        factorFalse.false.accept(self)
    
    def visitFactorRune(self,factorRune):
        factorRune.rune.accept(self)

    def visitFactorExpression(self,factorExpression):
        factorExpression.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Increment
##################################################################

    def visitInc(self, inc):
        inc.id.accept(self)

    def visitDec(self, dec):
        dec.id.accept(self)

def main():
    f = open("input3.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

if __name__ == "__main__":
    main()