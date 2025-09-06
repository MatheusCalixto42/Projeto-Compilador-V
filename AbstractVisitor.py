from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitCompoundImportItems(self, compoundImportItems):
        pass

    @abstractmethod
    def visitProgramItems(self, programItems):
        pass

    @abstractmethod
    def visitSequenceImports(self, sequenceImports):
        pass

    @abstractmethod
    def visitSingleImport(self, singleImport):
        pass

    @abstractmethod
    def visitSequenceProgramItems(self, sequenceProgramItems):
        pass

    @abstractmethod
    def visitSingleProgramItem(self, singleProgramItem):
        pass

    @abstractmethod
    def visitConstantDeclaration(self, constanteDeclaration):
        pass

    @abstractmethod
    def visitFunctionDeclaration(self, functionDeclaration):
        pass

    @abstractmethod
    def visitConstantDeclarationRule(self, constantDeclarationRule):
        pass

    @abstractmethod
    def visitFunctionVoid(self, functionVoid):
        pass

    @abstractmethod
    def visitFunctionReturnType(self, functionReturnType):
        pass

    @abstractmethod
    def visitSignatureWithParams(self, signatureWithParams):
        pass

    @abstractmethod
    def visitSingleSigParam(self, singleSigParam):
        pass

    @abstractmethod
    def visitSequenceSigParams(self, sequenceSigParams):
        pass

    @abstractmethod
    def visitSequenceParams(self, sequenceParams):
        pass

    @abstractmethod
    def visitSingleParams(self, singleParams):
        pass

    @abstractmethod
    def visitBlockStm(self, blockStm):
        pass

    @abstractmethod
    def visitSequenceStm(self, sequenceStm):
        pass

    @abstractmethod
    def visitSingleStm(self, singleStm):
        pass

    @abstractmethod
    def visitVarStm(self, varStm):
        pass

    @abstractmethod
    def visitVarAssign(self, varAssign):
        pass

    @abstractmethod
    def visitListStm(self, listStm):
        pass

    @abstractmethod
    def visitListAssign(self, listAssign):
        pass

    @abstractmethod
    def visitFuncCalls(self, funcCalls):
        pass

    @abstractmethod
    def visitIfStm(self, ifStm):
        pass

    @abstractmethod
    def visitForStm(self, forStm):
        pass

    @abstractmethod
    def visitIncrementStm(self, incrementStm):
        pass

    @abstractmethod
    def visitAssignStm(self, assignStm):
        pass

    @abstractmethod
    def visitBreakStm(self, breakStm):
        pass

    @abstractmethod
    def visitReturnStm(self, returnStm):
        pass
    
    @abstractmethod
    def visitImutableDeclaration(self, imutableDeclaration):
        pass
    
    @abstractmethod
    def visitMutableDeclaration(self, mutableDeclaration):
        pass

    @abstractmethod
    def visitVarModification(self, varModification):
        pass

    @abstractmethod
    def visitDeclarationImutableListRule(self, declarationImutableListRule):
        pass
    
    @abstractmethod
    def visitDeclarationMutableList(self, declarationMutableList):
        pass

    @abstractmethod
    def visitDeclarationMutableListLengthDefinition(self, listLengthDefinition):
        pass

    @abstractmethod
    def visitListModification(self, listModification):
        pass

    @abstractmethod
    def visitCallListAll(self, callListAll):
        pass

    @abstractmethod
    def visitCallListRange(self, callRange):
        pass

    # @abstractmethod
    # def visitFuncCallListSingle(self, funcCallSingle):
    #     pass

    @abstractmethod
    def visitFuncCallWithParams(self, funcCallWithParams):
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
    def visitOnlyexpRelFor(self, onlyExpressionRelationalFor):
        pass

#    @abstractmethod
#    def visitIdImutable(self, idImutable):
#        pass

    @abstractmethod
    def visitExpPlus(self, expressionPlus):
        pass

    @abstractmethod
    def visitExpMinus(self, expressionMinus):
        pass

    @abstractmethod
    def visitSingleTerm(self, singleTerm):
        pass
    
    @abstractmethod
    def visitExpIncrement(self, expressionIncrement):
        pass

    @abstractmethod
    def visitExpFuncCall(self, expressionFuncCall):
        pass

    @abstractmethod
    def visitExpCallList(self, expressionCallList):
        pass

    @abstractmethod
    def visitExpRelEqual(self, expressionRelationalEqual):
        pass

    @abstractmethod
    def visitExpRelNotEqual(self, expressionRelationalNotEqual):
        pass

    @abstractmethod
    def visitExpRelLessThan(self, expressionRelationalLessThan):
        pass

    @abstractmethod
    def visitExpRelGreaterThan(self, expressionRelationalGreaterThan):
        pass

    @abstractmethod
    def visitExpRelLessThanOrEqual(self, expressionRelationalLessThanOrEqual):
        pass

    @abstractmethod
    def visitExpRelGreaterThanOrEqual(self, expressionRelationalGreaterThanOrEqual):
        pass

    @abstractmethod
    def visitExpRelAnd(self, expressionRelationalAnd):
        pass

    @abstractmethod
    def visitExpRelOr(self, expressionRelationalOr):
        pass

    @abstractmethod
    def visitExpRelNot(self, expressionRelationalNot):
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
    def visitFactorNumberFloat(self, factorNumberFloat):
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
    def visitFactorExp(self, factorExpression):
        pass

    @abstractmethod
    def visitFactorList(self, factorList):
        pass

    @abstractmethod
    def visitFactorCientificNotation(self, cientific_notation):
        pass

    @abstractmethod
    def visitFactorBinary(self, binary):
        pass

    @abstractmethod
    def visitFactorOctal(self, octal):
        pass

    @abstractmethod
    def visitFactorHex(self, hex):
        pass

 #   @abstractmethod
 #   def visitFactorInterpolationString(self, factorInterpolationString):
 #       pass

    @abstractmethod
    def visitFactorSizeOfExp(self, factorSizeOfExpression):
        pass

    @abstractmethod
    def visitSizeOfExp(self, sizeOfExpression):
        pass

    @abstractmethod
    def visitSizeOfType(self, sizeOfType):
        pass

    @abstractmethod
    def visitInc(self, inc):
        pass

    @abstractmethod
    def visitDec(self, dec):
        pass

    @abstractmethod
    def visitAssignPlusEquals(self, mais_igual):
        pass

    @abstractmethod
    def visitAssignMinusEquals(self, menos_igual):
        pass

    @abstractmethod
    def visitAssignMultiplicationEquals(self, multi_igual):
        pass

    @abstractmethod
    def visitDivideEquals(self, div_igual):
        pass

    @abstractmethod
    def visitAssignModEquals(self, mod_igual):
        pass

    @abstractmethod
    def visitAssignAndEquals(self, and_igual):
        pass

    @abstractmethod
    def visitAssignOrEquals(self, or_igual):
        pass

    @abstractmethod
    def visitAssignXOREquals(self, xor_igual):
        pass

    @abstractmethod
    def visitAssignDeslocationLeft(self, desloca_esq_igual):
        pass

    @abstractmethod
    def visitAssignDeslocationRight(self, desloca_dir_igual):
        pass
