from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitImportAndFuncDefinition(self, importAndFuncDefinition):
        pass

    @abstractmethod
    def visitSingleFuncDefinition(self, singleFuncDefinition):
        pass

    @abstractmethod
    def visitSequenceImports(self, sequenceImports):
        pass

    @abstractmethod
    def visitSingleImport(self, singleImport):
        pass

    @abstractmethod
    def visitFunctionVoid(self, functionVoid):
        pass

    @abstractmethod
    def visitFunctionReturnType(self, functionReturnType):
        pass

    @abstractmethod
    def visitFunctionMain(self, functionMain):
        pass

    @abstractmethod
    def visitFunctionVoidWithoutMain(self, functionVoidWithoutMain):
        pass

    @abstractmethod
    def visitFunctionReturnTypeWithoutMain(self, functionReturnTypeWithoutMain):
        pass

    @abstractmethod
    def visitNoneFunction(self, noneFunction):
        pass

    @abstractmethod
    def visitDescriptionParam(self, descriptionParam):
        pass

    @abstractmethod
    def visitDescriptionParams(self, descriptionParams):
        pass

    @abstractmethod
    def visitNoneParam(self, noneParam):#olhar esse noneParam
        pass

    @abstractmethod
    def visitMultipleParams(self, multipleParams):
        pass

    @abstractmethod
    def visitNoneParam(self, noneParam):
        pass

    @abstractmethod
    def visitIntV(self, intV):
        pass

    @abstractmethod
    def visitF32(self, f32):
        pass

    @abstractmethod
    def visitF64(self, f64):
        pass

    @abstractmethod
    def visitRune(self, rune):
        pass

    @abstractmethod
    def visitString(self, string):
        pass

    @abstractmethod
    def visitBoolV(self, boolv):
        pass

    @abstractmethod
    def visitBlockStatement(self, blockStatement):
        pass

    @abstractmethod
    def visitVarStatement(self, varStatement):
        pass

    @abstractmethod
    def visitVarAssignment(self, varAssignment):
        pass

    @abstractmethod
    def visitFuncCallS(self, funcCall):
        pass

    @abstractmethod
    def visitIfStatement(self, ifStatement):
        pass

    @abstractmethod
    def visitForStatement(self, forStatement):
        pass

    @abstractmethod
    def visitReturnStatement(self, returnStatement):
        pass

    @abstractmethod
    def visitNoneStatement(self, noneStatement):
        pass
    
    @abstractmethod
    def visitDeclarationImutable(self, declarationImutable):
        pass

    @abstractmethod
    def visitMutableDeclaration(self, mutableDeclaration):
        pass

    @abstractmethod
    def visitConstantDeclaration(self, constantDeclaration):
        pass

    @abstractmethod
    def visitVarModification(self, varModification):
        pass

    @abstractmethod
    def visitFuncCompoundParams(self, funcCompoundParams):
        pass

    @abstractmethod#olhar aqui
    def visitFuncNoParams(self, funcNoParams):
        pass

    @abstractmethod
    def visitListId(self, listId):
        pass

    @abstractmethod
    def visitPlusExpres(self, plusExpres):
        pass

    @abstractmethod#olhar aqui
    def visitNoneExpression(self, noneExpression):
        pass
    
    @abstractmethod
    def visitOnlyIf(self, onlyIf):
        pass

    @abstractmethod
    def visitIfAndElse(self, ifAndElse):
        pass

    @abstractmethod
    def visitElseIf(self, elseIf):
        pass

    @abstractmethod
    def visitOnlyElse(self, onlyElse):
        pass

    @abstractmethod
    def visitForEach(self, forEach):
        pass

    @abstractmethod
    def visitConventionalFor(self, conventionalFor):
        pass

    @abstractmethod
    def visitOnlyExpressionRelationalFor(self, onlyExpressionRelationalFor):
        pass

    @abstractmethod
    def visitIdImutable(self, idImutable):
        pass

    @abstractmethod
    def visitReturnExpression(self, returnExpression):
        pass

    @abstractmethod
    def visitExpressionPlus(self, expressionPlus):
        pass

    @abstractmethod
    def visitExpressionMinus(self, expressionMinus):
        pass

    @abstractmethod
    def visitSingleTerm(self, singleTerm):
        pass

    @abstractmethod
    def visitExpressionRelationalEqual(self, expressionRelationalEqual):
        pass

    @abstractmethod
    def visitExpressionRelationalNotEqual(self, expressionRelationalNotEqual):
        pass

    @abstractmethod
    def visitExpressionRelationalLessThan(self, expressionRelationalLessThan):
        pass

    @abstractmethod
    def visitExpressionRelationalGreaterThan(self, expressionRelationalGreaterThan):
        pass

    @abstractmethod
    def visitExpressionRelationalLessThanOrEqual(self, expressionRelationalLessThanOrEqual):
        pass

    @abstractmethod
    def visitExpressionRelationalGreaterThanOrEqual(self, expressionRelationalGreaterThanOrEqual):
        pass

    @abstractmethod
    def visitExpressionRelationalAnd(self, expressionRelationalAnd):
        pass

    @abstractmethod
    def visitExpressionRelationalOr(self, expressionRelationalOr):
        pass

    @abstractmethod
    def visitExpressionRelationalNot(self, expressionRelationalNot):
        pass

    @abstractmethod
    def visitMultiplication(self, multiplication):
        pass

    @abstractmethod
    def visitDivision(self, division):
        pass

    @abstractmethod
    def visitMod(self, mod):
        pass

    @abstractmethod
    def visitOnlyFactor(self, onlyFactor):
        pass

    @abstractmethod
    def visitFactorID(self, factorID):
        pass

    @abstractmethod
    def visitFactorNumber(self, factorNumber):
        pass

    @abstractmethod
    def visitFactorString(self, factorString):
        pass

    @abstractmethod
    def visitFactorTrue(self, factorTrue):
        pass

    @abstractmethod
    def visitFactorFalse(self, factorFalse):
        pass

    @abstractmethod
    def visitFactorRune(self, factorRune):
        pass

    @abstractmethod
    def visitFactorExpression(self, factorExpression):
        pass

    @abstractmethod
    def visitInc(self, inc):
        pass

    @abstractmethod
    def visitDec(self, dec):
        pass