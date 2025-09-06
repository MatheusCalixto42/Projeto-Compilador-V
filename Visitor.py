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

    def visitCompoundImportItems(self,compoundImportItems):
        compoundImportItems.program_import.accept(self)
        compoundImportItems.program_items.accept(self)

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

    def visitSequenceProgramItems(self,sequenceProgramItems):
        sequenceProgramItems.program_item.accept(self)
        sequenceProgramItems.program_items.accept(self)

    def visitSingleProgramItem(self, singleProgramItem):
        singleProgramItem.program_item.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Program Item
################################################################## 

    def visitConstantDeclaration(self, constantDeclaration):
        constantDeclaration.constant.accept(self)

    def visitFunctionDeclaration(self, functionDeclaration):
        functionDeclaration.function.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Const
################################################################## 

    def visitConstantDeclarationRule(self, constantDeclarationRule):
        print('const', end=' ')
        print(constantDeclarationRule.id, end=' ')
        print(':=', end=' ')
        constantDeclarationRule.exp.accept(self)
        print()

###################################################################
# Classes to visit the Abstract Syntax of Function Definition
##################################################################

    def visitFunctionVoid(self,functionVoid):
        functionVoid.signature.accept(self)
        functionVoid.blockStm.accept(self)
        

    def visitFunctionReturnType(self,functionReturnType):
        functionReturnType.signature.accept(self)
        functionReturnType.id.accept(self)
        functionReturnType.blockStm.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Signature
##################################################################
    
    def visitSignatureWithParams(self, signatureWithParams):
        global tab
        print('fn', end=' ', sep=' ')
        print(signatureWithParams.id, end=' ')
        print('(', end=' ')
        signatureWithParams.s.accept(self) #usar if para o caso de n ter parametro?
        print(')', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Sigparams
##################################################################

    def visitSingleSigParam(self, singleSigParam):
        print(singleSigParam.id, end=' ')
        singleSigParam.idType.accept(self)

    def visitSequenceSigParams(self, sequenceSigParams):
        print(sequenceSigParams.id, end = '')
        print(sequenceSigParams.idType, end = ' ')
        print(',', end=' ')
        sequenceSigParams.sigparams.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Params
##################################################################
    
    def visitSequenceParams(self,sequenceParams):
        sequenceParams.exp.accept(self)
        print(',', end=' ')
        sequenceParams.params.accept(self)

    def visitSingleParams(self, singleParams):
        singleParams.exp.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of BlockStatement
##################################################################     

    def visitBlockStm(self, blockStm):
        global tab
        print('{')
        tab = tab + 3
        blockStm.stms.accept(self)
        tab = tab - 3
        print(blank(), '}')

###################################################################
# Classes to visit the Abstract Syntax of Stms
##################################################################

    def visitSequenceStm(self, sequenceStm):
        sequenceStm.stm.accept(self)
        sequenceStm.stms.accept(self)

    def visitSingleStatement(self, singleStatement):
        singleStatement.stm.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Stm
##################################################################

    def visitVarStm(self,varStm):#var_statemnt
        varStm.var_stm.accept(self)
        print()
        
    
    def visitVarAssign(self,varAssign):
        varAssign.var_assign.accept(self)
        print()
   
    def visitListStm(self, listStm):
        listStm.list_stm.accept(self)
        print()
        
    def visitListAssign(self, listAssign):
        listAssign.list_assign.accept(self)
        print()

    def visitFuncCalls(self,funcCalls):
        funcCalls.func_call.accept(self)
        print()
         
    def visitIfStm(self,ifStm):
        ifStm.if_stm.accept(self)

    def visitForStm(self,forStm):
        forStm.for_stm.accept(self)

    def visitBreakStm(self, breakStm):
        print(blank(), 'break', end=' ')

    def visitReturnStm(self,returnStm):
        print(blank(), 'return', end=' ')
        if(returnStm.expression == None):
            pass

        returnStm.expression.accept(self)

    def visitIncrementStm(self, incrementStm):
        incrementStm.increment_stm.accept(self)
        print()

    def visitAssignStm(self, assignStm):
        assignStm.assign_stm.accept(self)
        print()


 ###################################################################
# Classes to visit the Abstract Syntax of Var Statement
##################################################################   

    def visitImutableDeclaration(self,imutableDeclaration):
        print(blank(), imutableDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        imutableDeclaration.exp.accept(self)

    def visitMutableDeclaration(self,mutableDeclaration):
        print(blank(), 'mut', end=' ',sep=' ')
        print(mutableDeclaration.id, end=' ')
        print(':=', end=' ',sep=' ')
        mutableDeclaration.exp.accept(self)
    

###################################################################
# Classes to visit the Abstract Syntax of Var Assignment
##################################################################

    def visitVarModification(self,varModification):
        print(blank(), varModification.id, end=' ')
        print('=', end=' ',sep=' ') 
        varModification.exp.accept(self)   


###################################################################
# Classes to visit the Abstract Syntax of List Statement
##################################################################

    def visitDeclarationImutableListRule(self, declarationImutableListRule):
        print(blank(), declarationImutableListRule.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('[', end=' ', sep=' ')
        declarationImutableListRule.id_list.accept(self)
        print(']', end=' ', sep=' ')
        

    def visitDeclarationMutableList(self, declarationMutableList):
        print(blank(), 'mut', end=' ',sep=' ')
        print(declarationMutableList.id, end=' ')
        print(':=', end=' ',sep=' ')
        print('[', end=' ', sep=' ')
        declarationMutableList.params.accept(self)
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
        listModification.exp.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Func Call List
##################################################################

    def visitCallListAll(self, callListAll):
        print(blank(), callListAll.id, end=' ')
        print('[', end=' ')
        print(callListAll.dotdot, end=' ')
        print(']', end=' ')

    def visitCallListRange(self, callRange):
        print(blank(), callRange.id, end=' ')
        print('[', end=' ')
        print(callRange.number, end=' ')
        print(callRange.dotdot, end=' ')
        print(callRange.number2, end=' ')
        print(']', end=' ')

    # def visitFuncCallListSingle(self, funcCallSingle):
    #     print(blank(), funcCallSingle.id, end=' ')
    #     print('[', end=' ')
    #     print(funcCallSingle.number, end=' ')
    #     print(']', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Func Call
##################################################################

    def visitFuncCallWithParams(self,funcCallWithParams):
        print(blank(), funcCallWithParams.id, end=' ')
        print('(', end=' ')
        funcCallWithParams.id_list.accept(self)
        print(')', end=' ')


###################################################################
# Classes to visit the Abstract Syntax of If Statement
##################################################################

    def visitOnlyIf(self,onlyIf):
        global tab
        print(blank(), 'if', end=' ', sep=' ')
        onlyIf.expRel.accept(self)
        onlyIf.blockStm.accept(self)
        

    def visitIfAndElse(self,ifAndElse):
        global tab
        print(blank(), 'if', end=' ', sep=' ')
        ifAndElse.expRel.accept(self)
        ifAndElse.blockStm.accept(self)
        ifAndElse.elseV.accept(self)
     

###################################################################
# Classes to visit the Abstract Syntax of Else
##################################################################

    def visitElseIf(self,elseIf):
        print('else', end=' ', sep=' ')
        elseIf.if_stm.accept(self)

    def visitOnlyElse(self,onlyElse):
        global tab
        print('else', end=' ', sep=' ')
        onlyElse.blockstm.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of For
##################################################################

    def visitForEach(self,forEach):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        print(forEach.id, end=' ')
        print('in', end=' ', sep=' ')
        forEach.exp.accept(self)
        forEach.blockstm.accept(self)
    

    def visitConventionalFor(self,conventionalFor):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        print(conventionalFor.id, end=' ')
        print(';', end=' ')
        conventionalFor.expRel.accept(self)
        print(';', end=' ', sep=' ')
        conventionalFor.increment.accept(self)
        conventionalFor.blockstm.accept(self)

    def visitOnlyexpRelFor(self,onlyexpRelFor):
        global tab
        print(blank(), 'for', end=' ', sep=' ')
        onlyexpRelFor.expRel.accept(self)
        onlyexpRelFor.blockStm.accept(self)

        
###################################################################
# Classes to visit the Abstract Syntax of Expression
##################################################################

    def visitExpPlus(self,expPlus):
        expPlus.exp.accept(self)
        print('+', end=' ')
        expPlus.term.accept(self)

    def visitExpMinus(self,expMinus):
        expMinus.exp.accept(self)
        print('-', end=' ')
        expMinus.term.accept(self)

    def visitSingleTerm(self,singleTerm):
        singleTerm.term.accept(self)

    def visitExpIncrement(self, expIncrement):
        global tab
        tab_aux = tab
        tab = 0
        expIncrement.increment.accept(self)
        tab = tab_aux

    def visitExpFuncCall(self, expFuncCall):
        expFuncCall.funcCall.accept(self)

    def visitExpCallList(self, expCallList):
        expCallList.callist.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Relational Expression
##################################################################

    def visitExpRelEqual(self,expRelEqual):
        expRelEqual.exp1.accept(self)
        print('==', end=' ')
        expRelEqual.exp2.accept(self)

    def visitExpRelNotEqual(self,expRelNotEqual):
        expRelNotEqual.exp1.accept(self)
        print('!=', end=' ')
        expRelNotEqual.exp2.accept(self)

    def visitExpRelLessThan(self,expRelLessThan):
        expRelLessThan.exp1.accept(self)
        print('<', end=' ')
        expRelLessThan.exp2.accept(self)

    def visitExpressionRelationalGreaterThan(self,expressionRelationalGreaterThan):
        expressionRelationalGreaterThan.exp1.accept(self)
        print('>', end=' ')
        expressionRelationalGreaterThan.exp2.accept(self)

    def visitExpRelLessThanOrEqual(self,expressionRelationalLessThanOrEqual):
        expressionRelationalLessThanOrEqual.exp1.accept(self)
        print('<=', end=' ')
        expressionRelationalLessThanOrEqual.exp2.accept(self)

    def visitExpRelGreaterThanOrEqual(self,expressionRelationalGreaterThanOrEqual):
        expressionRelationalGreaterThanOrEqual.exp1.accept(self)
        print('>=', end=' ')
        expressionRelationalGreaterThanOrEqual.exp2.accept(self)

    def visitExpRelAnd(self,expressionRelationalAnd):
        expressionRelationalAnd.exp1.accept(self)
        print('&&', end=' ')
        expressionRelationalAnd.exp2.accept(self)

    def visitExpRelOr(self,expressionRelationalOr):
        expressionRelationalOr.exp1.accept(self)
        print('||', end=' ')
        expressionRelationalOr.exp2.accept(self)

    def visitExpRelNot(self,expressionRelationalNot):
        print('!', end=' ')
        expressionRelationalNot.exp.accept(self)

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
    def visitFactorNumber(self,factorNumber):
        print(factorNumber.number, end=' ')

    def visitFactorString(self,factorString):
        print(factorString.string, end=' ')

    def visitFactorID(self,factorID):
        print(factorID.id, end=' ')

    def visitFactorExpression(self,factorExpression):
        print('(', end=' ')
        factorExpression.exp.accept(self)
        print(')', end=' ')

    def visitFactorList(self, factorList):
        print(factorList.id, end=' ',sep=' ')
        print('[', end=' ')
        print(factorList.number, end = ' ',sep=' ')
        print(']', end=' ')

    def visitFactorTrue(self,factorTrue):
        print(factorTrue.true, end=' ')
    
    def visitFactorFalse(self,factorFalse):
        print(factorFalse.false, end=' ')

    def visitFactorRune(self,factorRune):
        print(factorRune.rune, end=' ')

    def visitFactorNumberFloat(self, factorNumberFloat):
        print(factorNumberFloat.numberfloat, end=' ')

    def visitFactorCientificNotation(self, cientific_notation):
        print(cientific_notation.cientificNotation, end=' ')

    def visitFactorBinary(self, binary):
        print(binary.factorBinary, end=' ')

    def visitFactorOctal(self, octal):
        print(octal.factorOctal, end=' ')

    def visitFactorHex(self, hex):
        print(hex.factorHex, end=' ')

#    def visitFactorInterpolationString(self, factorInterpolationString):
#        print(factorInterpolationString.interpolationString, end=' ')

    def visitFactorSizeOfExp(self, factorSizeofExp):
        factorSizeofExp.sizeofexp.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Size of Expression
##################################################################

    def visitSizeofExp(self, sizeOfExp):
        print(blank(), sizeOfExp.sizeof, end=' ')
        print('(', end=' ')
        sizeOfExp.exp.accept(self)
        print(')', end=' ')

    def visitSizeOfType(self, sizeOfType):
        print(blank(), sizeOfType.sizeof, end=' ')
        print('(', end=' ')
        print(sizeOfType.idType, end=' ')
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

    def visitAssignPlusEquals(self, assignPlusEquals):
        print(blank(), assignPlusEquals.id, end = ' ')
        print('+=', end=' ')
        assignPlusEquals.exp.accept(self)

    def visitAssignMinusEquals(self, assignMinusEquals):
        print(blank(), assignMinusEquals.id, end = ' ')
        print('-=', end=' ')
        assignMinusEquals.exp.accept(self)

    def visitAssignMultiplicationEquals(self, assignMultiplicationEquals):
        print(blank(), assignMultiplicationEquals.id, end = ' ')
        print('*=', end=' ')
        assignMultiplicationEquals.exp.accept(self)

    def visitDivideEquals(self, DivideEquals):
        print(blank(), DivideEquals.id, end = ' ')
        print('/=', end=' ')
        DivideEquals.exp.accept(self)

    def visitAssignModEquals(self, assignModEquals):
        print(blank(), assignModEquals.id, end = ' ')
        print('%=', end=' ')
        assignModEquals.exp.accept(self)

    def visitAssignAndEquals(self, assignAndEquals):
        print(blank(), assignAndEquals.id, end = ' ')
        print('&=', end=' ')
        assignAndEquals.exp.accept(self)

    def visitAssignOrEquals(self, assignOrEquals):
        print(blank(), assignOrEquals.id, end = ' ')
        print('|=', end=' ')
        assignOrEquals.exp.accept(self)

    def visitAssignXOREquals(self, assignXOREquals):
        print(blank(), assignXOREquals.id, end = ' ')
        print('^=', end=' ')
        assignXOREquals.exp.accept(self)

    def visitAssignDeslocationLeft(self, assignDeslocationLeft):
        print(blank(),assignDeslocationLeft.id, end = ' ')
        print('<<=', end=' ')
        assignDeslocationLeft.exp.accept(self)

    def visitAssignDeslocationRight(self, assignDeslocationRight):
        print(blank(), assignDeslocationRight.id, end = ' ')
        print('>>=', end=' ')
        assignDeslocationRight.exp.accept(self)


def main():
    f = open("teste.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(start='program')
    result = parser.parse(debug=True)
    print("imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

if __name__ == "__main__":
    main()
