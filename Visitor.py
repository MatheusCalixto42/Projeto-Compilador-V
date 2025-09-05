from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
from SintaxeAbstrate import FactorBinary
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
        importAndFuncDefinition.program_items.accept(self)

    def visitProgramItems(self,programItems):
        programItems.program_items.accept(self)

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
# Classes to visit the Abstract Syntax of Program Items
################################################################## 

    def visitMultipleProgramItems(self,multipleProgramItems):
        multipleProgramItems.item.accept(self)
        multipleProgramItems.items_recursao.accept(self)

    def visitNoneItems(self,noneItems):
        pass

###################################################################
# Classes to visit the Abstract Syntax of Program Item
################################################################## 

    def visitConstanteDeclaration(self, constanteDeclaration):
        constanteDeclaration.constante.accept(self)

    def visitFunctionDeclaration(self, functionDeclaration):
        functionDeclaration.function.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Const
################################################################## 

    def visitConstanteDeclarationRule(self, constanteDeclarationRule):
        print('const', end=' ')
        print(constanteDeclarationRule.id, end=' ')
        print(':=', end=' ')
        constanteDeclarationRule.expression.accept(self)
        print()

###################################################################
# Classes to visit the Abstract Syntax of Function Definition
##################################################################

    def visitFunctionVoid(self,functionVoid):
        print('fn', end=' ', sep=' ')
        print(functionVoid.id, end=' ')
        print('(', end=' ')
        functionVoid.param.accept(self) #usar if para o caso de n ter parametro?
        print(')', end=' ')
        functionVoid.block_statement.accept(self)
        

    def visitFunctionReturnType(self,functionReturnType):
        print('fn', end=' ', sep=' ')
        print(functionReturnType.id, end=' ')
        print('(', end=' ')
        functionReturnType.param.accept(self)
        print(')', end=' ')
        functionReturnType.type.accept(self)
        functionReturnType.block_statement.accept(self)

    def visitFunctionMain(self,functionMain):
        print('fn', end=' ', sep=' ')
        print(functionMain.id, end=' ')
        print('(', end='')
        print(')', end=' ')
        functionMain.block_statement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Params
##################################################################

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
# Classes to visit the Abstract Syntax of Param
##################################################################
    
    def visitDescriptionParam(self,descriptionparam):
        print(descriptionparam.id, end=' ')
        descriptionparam.type.accept(self)

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
        global tab
        print('{')
        tab = tab + 3
        blockStatement.statements.accept(self)
        tab = tab - 3
        print(blank(), '}')

    def visitNoneBlockStatement(self, noneBlockStatement):
        global tab
        print('{')
        print(blank(), '}')


###################################################################
# Classes to visit the Abstract Syntax of Statements
##################################################################

    def visitMultipleStatement(self, multipleStatement):
        multipleStatement.statement.accept(self)
        multipleStatement.statements.accept(self)

    def visitSingleStatement(self, singleStatement):
        singleStatement.statement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Statement
##################################################################

    def visitVarStatement(self,varStatement):#var_statemnt
        varStatement.var_statement.accept(self)
        print()
        
    
    def visitVarAssignment(self,varAssignment):
        varAssignment.var_assignment.accept(self)
        print()
   
    def visitListStatement(self, listStatement):
        listStatement.list_statement.accept(self)
        print()
        
    def visitListAssignment(self, listAssignment):
        listAssignment.list_assignment.accept(self)
        print()

    def visitFuncCallS(self,funcCall):
        funcCall.func_call.accept(self)
        print()
         
    def visitIfStatement(self,ifStatement):
        ifStatement.if_statement.accept(self)


    def visitForStatement(self,forStatement):
        forStatement.for_statement.accept(self)


    def visitIncrementStatement(self, incrementStatement):
        incrementStatement.increment_statement.accept(self)
        print()


    def visitAssignmentStatement(self, assignmentStatement):
        assignmentStatement.assignment_statement.accept(self)
        print()


    def visitBreakStatement(self, breakStatement):
        breakStatement.break_statement.accept(self)
        print()

    def visitReturnStatement(self,returnStatement):
        returnStatement.return_statement.accept(self)
        print()


 ###################################################################
# Classes to visit the Abstract Syntax of Var Statement
##################################################################   

    def visitDeclarationImutable(self,declarationImutable):
        declarationImutable.declaration_imutable.accept(self)

    def visitMutableDeclaration(self,mutableDeclaration):
        print(blank(), 'mut', end=' ',sep=' ')
        print(mutableDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        mutableDeclaration.expression.accept(self)
    
    def visitConstantDeclaration(self,constantDeclaration):
        print(blank(), 'const', end=' ',sep=' ')
        print(constantDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        constantDeclaration.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Var Assignment
##################################################################

    def visitVarModification(self,varModification):
        print(blank(), varModification.id, end=' ')
        print('=', end=' ',sep=' ') 
        varModification.expression.accept(self)   


###################################################################
# Classes to visit the Abstract Syntax of List Statement
##################################################################

    def visitDeclarationImutableList(self, declarationImutableList):
        declarationImutableList.declaration_imutable_list.accept(self)
        

    def visitDeclarationMutableList(self, declarationMutableList):
        print(blank(), 'mut', end=' ',sep=' ')
        print(declarationMutableList.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('[', end=' ', sep=' ')
        declarationMutableList.id_list.accept(self)
        print(']', end=' ', sep=' ')

    def visitDeclarationMutableListLengthDefinition(self, listLengthDefinition):
        print(blank(), 'mut', end=' ',sep=' ')
        print(listLengthDefinition.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('[', end=' ', sep=' ')
        listLengthDefinition.number.accept(self) #aqui
        print(']', end=' ', sep=' ')
        listLengthDefinition.type.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of List Assigment
##################################################################

    def visitListModification(self, listModification):
        print(blank(),listModification.id, end=' ')
        print('[', end=' ', sep=' ')
        print(listModification.number, end=' ')
        print(']', end=' ', sep=' ')
        print('=', end=' ', sep=' ')
        listModification.expression.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Func Call
##################################################################

    def visitFuncCompoundParams(self,funcCompoundParams):
        print(blank(), funcCompoundParams.id, end=' ')
        print('(', end=' ')
        funcCompoundParams.id_list.accept(self)
        print(')', end=' ')

    def visitFuncNoParams(self,funcNoParams):
        print(blank(), funcNoParams.id, end=' ')
        print('(', end=' ')
        print(')', end=' ')

    def visitFuncCallList(self, funcCallList):
        funcCallList.funcCallList.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Func Call List
##################################################################

    def visitFuncCallListAll(self, funcCallListAll):
        print(blank(), funcCallListAll.id, end=' ')
        print('[', end=' ')
        print(funcCallListAll.dotdot, end=' ')
        print(']', end=' ')

    def visitFuncCallListRange(self, funcCallRange):
        print(blank(), funcCallRange.id, end=' ')
        print('[', end=' ')
        print(funcCallRange.number, end=' ')
        print(funcCallRange.dotdot, end=' ')
        print(funcCallRange.number2, end=' ')
        print(']', end=' ')

    # def visitFuncCallListSingle(self, funcCallSingle):
    #     print(blank(), funcCallSingle.id, end=' ')
    #     print('[', end=' ')
    #     print(funcCallSingle.number, end=' ')
    #     print(']', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of id list
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
        print(blank(), 'if', end=' ', sep=' ')
        onlyIf.expressionrelational.accept(self)
        onlyIf.blockstatement.accept(self)
        

    def visitIfAndElse(self,ifAndElse):
        global tab
        print(blank(), 'if', end=' ', sep=' ')
        ifAndElse.expressionrelational.accept(self)
        ifAndElse.blockstatement.accept(self)
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
        onlyElse.blockstatement.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of For
##################################################################

    def visitForEach(self,forEach):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        print(forEach.id, end=' ')
        print('in', end=' ', sep=' ')
        forEach.expression.accept(self)
        forEach.blockstatement.accept(self)
    

    def visitConventionalFor(self,conventionalFor):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        conventionalFor.declarationimutable.accept(self)
        print(';', end=' ', sep=' ')
        conventionalFor.expressionrelational.accept(self)
        print(';', end=' ', sep=' ')
        conventionalFor.increment.accept(self)
        conventionalFor.statement.accept(self)
       

    def visitOnlyExpressionRelationalFor(self,onlyExpressionRelationalFor):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        onlyExpressionRelationalFor.expressionrelational.accept(self)
        onlyExpressionRelationalFor.blockstatement.accept(self)

        

###################################################################
# Classes to visit the Abstract Syntax of Imutable Declaration
##################################################################

    def visitIdImutable(self,idImutable):
        print(blank(), idImutable.id, end=' ')
        print(':=', end=' ',sep=' ')
        idImutable.expression.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Imutable Declaration List Rule
##################################################################

    def visitDeclarationImutableListRule(self,declarationImutableListRule):
        print(blank(), declarationImutableListRule.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('[', end=' ', sep=' ')
        declarationImutableListRule.id_list.accept(self)
        print(']', end=' ', sep=' ')

###################################################################
# Classes to visit the Abstract Syntax of Break Statement
##################################################################    

    def visitOnlyBreak(self, onlyBreak):
        print(blank(), 'break', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Return Statement
##################################################################    

    def visitReturnExpression(self,returnExpression):
        print(blank(), 'return', end=' ')
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

    def visitExpressionIncrement(self, expressionIncrement):
        global tab
        tab_aux = tab
        tab = 0
        expressionIncrement.increment.accept(self)
        tab = tab_aux

    def visitExpressionFuncCall(self, expressionFuncCall):
        expressionFuncCall.funcCall.accept(self)


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
        print('sizeof', end=' ')
        print('(', end=' ')
        sizeOfExpression.expression.accept(self)
        print(')', end=' ')

    def visitSizeOfType(self, sizeOfType):
        print('sizeof', end=' ')
        print('(', end=' ')
        sizeOfType.type.accept(self)
        print(')', end=' ')

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
        print(blank(),mais_igual.id, end = ' ')
        print('+=', end=' ')
        mais_igual.expression.accept(self)

    def visitMenosIgual(self, menos_igual):
        print(blank(),menos_igual.id, end = ' ')
        print('-=', end=' ')
        menos_igual.expression.accept(self)
    
    def visitMultiIgual(self, multi_igual):
        print(blank(),multi_igual.id, end = ' ')
        print('*=', end=' ')
        multi_igual.expression.accept(self)

    def visitDivIgual(self, div_igual):
        print(blank(),div_igual.id, end = ' ')
        print('/=', end=' ')
        div_igual.expression.accept(self)

    def visitModIgual(self, mod_igual):
        print(blank(),mod_igual.id, end = ' ')
        print('%=', end=' ')
        mod_igual.expression.accept(self)

    def visitAndIgual(self, and_igual):
        print(blank(),and_igual.id, end = ' ')
        print('&=', end=' ')
        and_igual.expression.accept(self)

    def visitOrIgual(self, or_igual):
        print(blank(),or_igual.id, end = ' ')
        print('|=', end=' ')
        or_igual.expression.accept(self)

    def visitXORIgual(self, xor_igual):
        print(blank(), xor_igual.id, end = ' ')
        print('^=', end=' ')
        xor_igual.expression.accept(self)

    def visitDeslocaEsqIgual(self, desloca_esq_igual):
        print(blank(),desloca_esq_igual.id, end = ' ')
        print('<<=', end=' ')
        desloca_esq_igual.expression.accept(self)

    def visitDeslocaDirIgual(self, desloca_dir_igual):
        print(blank(),desloca_dir_igual.id, end = ' ')
        print('>>=', end=' ')
        desloca_dir_igual.expression.accept(self)


def main():
    f = open("teste.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(start='program')
    result = parser.parse(debug=False)
    print("imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

if __name__ == "__main__":
    main()
