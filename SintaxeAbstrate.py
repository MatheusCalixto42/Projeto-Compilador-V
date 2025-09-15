from abc import abstractmethod
from abc import ABCMeta

#####################################################
# Class for Program
####################################################

class ProgramAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundImportItems(ProgramAbstract):
    def __init__(self, program_import, program_items):
        self.program_import = program_import
        self.program_items = program_items
    def accept(self, visitor):
        return visitor.visitCompoundImportItems(self)

class ProgramItems(ProgramAbstract):
    def __init__(self, program_items):
        self.program_items = program_items
    def accept(self, visitor):
        return visitor.visitProgramItems(self)

#######################################################
# Class for Program_import
######################################################

class ProgramImportAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass    

class SequenceImports(ProgramImportAbstract):
    def __init__(self, import_token, id, program_import):
        self.import_token = import_token 
        self.id = id          
        self.program_import = program_import
    def accept(self, visitor):
        return visitor.visitSequenceImports(self)

class SingleImport(ProgramImportAbstract):
    def __init__(self, import_token, id):
        self.id = id
        self.import_token = import_token
    def accept(self, visitor):
        return visitor.visitSingleImport(self)
    
#######################################################
# Class for Program_items
######################################################

class ProgramItemsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SequenceProgramItems(ProgramItemsAbstract):
    def __init__(self, program_item, program_items):
        self.program_item = program_item
        self.program_items = program_items
    def accept(self, visitor):
        return visitor.visitSequenceProgramItems(self)

class SingleProgramItem(ProgramItemsAbstract):
    def __init__(self, program_item):
        self.program_item = program_item
    def accept(self, visitor):
        return visitor.visitSingleProgramItem(self)

#######################################################
# Class for Program_item
######################################################
class ProgramItemAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConstantDeclaration(ProgramItemAbstract):
    def __init__(self, constant):
        self.constant = constant
    def accept(self, visitor):
        return visitor.visitConstantDeclaration(self)

class FunctionDeclaration(ProgramItemAbstract):
    def __init__(self, function):
        self.function = function
    def accept(self, visitor):
        return visitor.visitFunctionDeclaration(self)

#######################################################
# Class for Const_declaration
# ######################################################

class ConstantDeclarationAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConstantDeclarationRule(ConstantDeclarationAbstract):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitConstantDeclarationRule(self)

#######################################################
# Class for Function_definition
######################################################

class FunctionDefinition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass   

class FunctionVoid(FunctionDefinition): # função com retorno void
    def __init__(self, signature, blockStm):
        self.signature = signature
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitFunctionVoid(self)

class FunctionReturnType(FunctionDefinition): #função com retorno de algum tipo
    def __init__(self,signature, id, blockStm):
        self.signature = signature
        self.id = id
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitFunctionReturnType(self)


#######################################################
# Class for Signature
######################################################

class SignatureAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class SignatureWithParams(SignatureAbstract):
    def __init__(self,id, sigparams):
        self.id = id
        self.sigparams = sigparams  #Lembrar de colocar passando nada para NoneParams
    def accept(self, visitor):
        return visitor.visitSignatureWithParams(self)

#######################################################
# Class for SigParams
######################################################

class SigParamsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParam(SigParamsAbstract):
    def __init__(self,id, idType):
        self.id = id
        self.idType = idType
    def accept(self, visitor):
        return visitor.visitSingleSigParam(self)
    
class SequenceSigParams(SigParamsAbstract):
    def __init__(self,id, idType, sigparams):
        self.id = id
        self.idType = idType
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSequenceSigParams(self)

########################################################
# Class for Params
########################################################

class ParamsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SequenceParams(ParamsAbstract):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitSequenceParams(self)

class SingleParams(ParamsAbstract):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParams(self)

########################################################
# Class for BlockStmt
#######################################################

class BlockStmAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class BlockStm(BlockStmAbstract):
    def __init__(self, stms):
        self.stms = stms  #Lembrar de colocar passando nada para NoneStms
    def accept(self, visitor):
        return visitor.visitBlockStm(self)
    
#######################################################
# Class for Stms
#######################################################

class StmsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SequenceStm(StmsAbstract):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitSequenceStm(self)

class SingleStm(StmsAbstract):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

########################################################
# Class for Stm
#######################################################

class StmAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class VarStm(StmAbstract):
    def __init__(self, var_stm ):
        self.var_stm = var_stm
    def accept(self, visitor):
        return visitor.visitVarStm(self)

class VarAssign(StmAbstract):
    def __init__(self, var_assign):
        self.var_assign = var_assign
    def accept(self, visitor):
        return visitor.visitVarAssign(self)

class ListStm(StmAbstract):
    def __init__(self, list_stm):
        self.list_stm = list_stm
    def accept(self, visitor):
        return visitor.visitListStm(self)

class ListAssign(StmAbstract):
    def __init__(self, list_assign):
        self.list_assign = list_assign
    def accept(self, visitor):
        return visitor.visitListAssign(self)

class FuncCalls(StmAbstract):
    def __init__(self, func_call):
        self.func_call = func_call
    def accept(self, visitor):
        return visitor.visitFuncCalls(self)

class IfStm(StmAbstract):
    def __init__(self, if_stm):
        self.if_stm = if_stm
    def accept(self, visitor):
        return visitor.visitIfStm(self)

class ForStm(StmAbstract):
    def __init__(self, for_stm):
        self.for_stm = for_stm
    def accept(self, visitor):
        return visitor.visitForStm(self)
    
class Break(StmAbstract):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitBreakStm(self)

class Return(StmAbstract):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitReturnStm(self)
    
class IncrementStm(StmAbstract):
    def __init__(self, increment_stm):
        self.increment_stm = increment_stm
    def accept(self, visitor):
        return visitor.visitIncrementStm(self)

class AssignStm(StmAbstract):
    def __init__(self, assign_stm):
        self.assign_stm = assign_stm
    def accept(self, visitor):
        return visitor.visitAssignStm(self)


#########################################################
# Class for Var_Stm
########################################################

class VarStmAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ImutableDeclaration(VarStmAbstract):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitImutableDeclaration(self)

class MutableDeclaration(VarStmAbstract):
    def __init__(self, mut, id, exp):
        self.mut = mut
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitMutableDeclaration(self)


##########################################################
# Class for Var_assign
#########################################################

class VarAssignAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VarModification(VarAssignAbstract):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitVarModification(self)

##########################################################
# Class for List_stm
#########################################################

class ListStmAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclarationImutableListRule(ListStmAbstract):
    def __init__(self, id, params):
        self.id = id
        self.params = params  
    def accept(self, visitor):
        return visitor.visitDeclarationImutableListRule(self)

class DeclarationMutableList(ListStmAbstract):
    def __init__(self, mut, id, params):
        self.mut = mut
        self.id = id
        self.params = params #lembrar de colocar sem nd para o None nesses casos
    def accept(self, visitor):
        return visitor.visitDeclarationMutableList(self)

class DeclarationMutableListLengthDefinition(ListStmAbstract):
    def __init__(self, mut, id, number, type):
        self.mut = mut
        self.id = id
        self.number = number
        self.type = type
    def accept(self, visitor):
        return visitor.visitDeclarationMutableListLengthDefinition(self)


##########################################################
# Class for List_assign
#########################################################

class ListAssignAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ListModification(ListAssignAbstract):
    def __init__(self, id, number, exp):
        self.id = id
        self.number = number
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitListModification(self)
    
##########################################################
# Class for List Call
#########################################################

class CallListAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):    
        pass

class CallListAll(CallListAbstract):
    def __init__(self, id, dotdot):
        self.id = id
        self.dotdot = dotdot
    def accept(self, visitor):
        return visitor.visitCallListAll(self)

class CallListRange(CallListAbstract):
    def __init__(self, id, number, dotdot, number2):
        self.id = id
        self.number = number
        self.dotdot = dotdot
        self.number2 = number2
    def accept(self, visitor):
        return visitor.visitCallListRange(self)

# class FuncCallListSingle(FuncCallListAbstract):
#     def __init__(self, id, number):
#         self.id = id
#         self.number = number
#     def accept(self, visitor):
#         return visitor.visitFuncCallListSingle(self)


##########################################################
# Class for Func_call
#########################################################

class FuncCallAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class FuncCallWithParams(FuncCallAbstract):
    def __init__(self, id, params):
        self.id = id
        self.params = params #lembrar de colocar passando vazio
    def accept(self, visitor):
        return visitor.visitFuncCallWithParams(self)


############################################################ 
# Class for If_stm
###########################################################

class IfStmAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class OnlyIf(IfStmAbstract):
    def __init__(self,expRel,blockStm):
        self.expRel = expRel
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitOnlyIf(self)

class IfAndElse(IfStmAbstract):
    def __init__(self, expRel, blockStm, elseV):
        self.expRel = expRel
        self.blockStm = blockStm
        self.elseV = elseV
    def accept(self, visitor):
        return visitor.visitIfAndElse(self)

############################################################ 
# Class for ElseOp
###########################################################

class ElseAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class ElseIf(ElseAbstract):
    def __init__(self,if_stm):
        self.if_stm = if_stm
    def accept(self, visitor):
        return visitor.visitElseIf(self)

class OnlyElse(ElseAbstract):
    def __init__(self,blockstm):
        self.blockstm = blockstm
    def accept(self, visitor):
        return visitor.visitOnlyElse(self)

############################################################ 
# Class for For
###########################################################

class ForAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class ForEach(ForAbstract):
    def __init__(self,id,exp,blockStm):
        self.id = id
        self.exp = exp
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitForEach(self)

class ConventionalFor(ForAbstract):
    def __init__(self, id, number, expRel, increment, blockStm):
        self.id = id
        self.number = number
        self.expRel = expRel
        self.increment = increment
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitConventionalFor(self)

class OnlyexpRelFor(ForAbstract):
    def __init__(self,expRel,blockStm):
        self.expRel = expRel
        self.blockStm = blockStm
    def accept(self, visitor):
        return visitor.visitOnlyexpRelFor(self)


########################################################
# Class for Exp
#######################################################

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpPlus(Exp):
    def __init__(self, exp, term):
        self.exp = exp
        self.term = term
    def accept(self, visitor):
        return visitor.visitExpPlus(self)

class ExpMinus(Exp):
    def __init__(self, exp, term):
        self.exp = exp
        self.term = term
    def accept(self, visitor):
        return visitor.visitExpMinus(self)

class SingleTerm(Exp):
    def __init__(self, term):
        self.term = term
    def accept(self, visitor):
        return visitor.visitSingleTerm(self)    

class ExpIncrement(Exp):
    def __init__(self, increment):
        self.increment = increment
    def accept(self, visitor):
        return visitor.visitExpIncrement(self)
    
class ExpFuncCall(Exp):
    def __init__(self,funcCall):
        self.funcCall = funcCall
    def accept(self, visitor):
        return visitor.visitExpFuncCall(self)

class ExpCallList(Exp):
    def __init__(self,calllist):
        self.calllist = calllist
    def accept(self, visitor):
        return visitor.visitExpCallList(self)


########################################################
# Class for ExpRel
#######################################################

class ExpRelAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpRelEqual(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelEqual(self)

class ExpRelNotEqual(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelNotEqual(self)

class ExpRelLessThan(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelLessThan(self)

class ExpRelGreaterThan(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelGreaterThan(self)

class ExpRelLessThanOrEqual(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelLessThanOrEqual(self)

class ExpRelGreaterThanOrEqual(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelGreaterThanOrEqual(self)

class ExpRelAnd(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelAnd(self)

class ExpRelOr(ExpRelAbstract):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRelOr(self)

class ExpRelNot(ExpRelAbstract):
    def __init__(self, exp):
        self.exp = exp 
    def accept(self, visitor):
        return visitor.visitExpRelNot(self)

############################################################ 
# Class for Term
###########################################################

class Term(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Multiplication(Term):
    def __init__(self, term,factor):
        self.term = term
        self.factor = factor
    def accept(self, visitor):
        return visitor.visitMultiplication(self)

class Division(Term):
    def __init__(self, term,factor):
        self.term = term
        self.factor = factor
    def accept(self, visitor):
        return visitor.visitDivision(self)

class Mod(Term):
    def __init__(self, term,factor):
        self.term = term
        self.factor = factor
    def accept(self, visitor):
        return visitor.visitMod(self)

class OnlyFactor(Term):
    def __init__(self, factor):
        self.factor = factor
    def accept(self, visitor):
        return visitor.visitOnlyFactor(self)

########################################################
# Class for Factor
#######################################################

class Factor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FactorID(Factor):
    def __init__(self, id):
        self.id = id   
    def accept(self, visitor):
        return visitor.visitFactorID(self)

class FactorNumber(Factor):
    def __init__(self, number):
        self.number = number
    def accept(self, visitor):
        return visitor.visitFactorNumber(self)
    
class FactorNumberFloat(Factor):
    def __init__(self, numberfloat):
        self.numberfloat = numberfloat
    def accept(self, visitor):
        return visitor.visitFactorNumberFloat(self)

class FactorString(Factor):
    def __init__(self, string):
        self.string = string
    def accept(self, visitor):
        return visitor.visitFactorString(self)

class FactorTrue(Factor):
    def __init__(self, true):
        self.true = true
    def accept(self, visitor):
        return visitor.visitFactorTrue(self)

class FactorFalse(Factor):
    def __init__(self, false):
        self.false = false
    def accept(self, visitor):
        return visitor.visitFactorFalse(self)

class FactorRune(Factor):
    def __init__(self, rune):
        self.rune = rune
    def accept(self, visitor):
        return visitor.visitFactorRune(self)

class FactorExp(Factor):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitFactorExp(self)

class FactorList(Factor):
    def __init__(self, id, number):
        self.id = id
        self.number = number
    def accept(self, visitor):
        return visitor.visitFactorList(self)

class FactorCientificNotation(Factor):
    def __init__(self, cientificNotation):
        self.cientificNotation = cientificNotation
    def accept(self,visitor):
        return visitor.visitFactorCientificNotation(self)

class FactorBinary(Factor):
    def __init__(self, factorBinary):
        self.factorBinary = factorBinary
    def accept(self,visitor):
        return visitor.visitFactorBinary(self)

class FactorHex(Factor):
    def __init__(self, factorHex):
        self.factorHex = factorHex
    def accept(self, visitor):
        return visitor.visitFactorHex(self)

class FactorOctal(Factor):
    def __init__(self, factorOctal):
        self.factorOctal = factorOctal
    def accept(self, visitor):
        return visitor.visitFactorOctal(self)

class FactorSizeOfExp(Factor):
    def __init__(self, sizeofexp):
        self.sizeofexp = sizeofexp
    def accept(self, visitor):
        return visitor.visitFactorSizeOfExp(self)

############################################################ 
# Class for Size of Exp
############################################################

class SizeOfExpAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SizeOfExp(SizeOfExpAbstract):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSizeOfExp(self)

class SizeOfType(SizeOfExpAbstract):
    def __init__(self, idType):
        self.idType = idType
    def accept(self, visitor):
        return visitor.visitSizeOfType(self)

############################################################ 
# Class for Increment
############################################################

class Increment(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Inc(Increment):
    def __init__(self,id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitInc(self)

class Dec(Increment):
    def __init__(self,id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitDec(self)
    
############################################################ 
# Class for Assign
############################################################

class AssignAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignPlusEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignPlusEquals(self)

class AssignMinusEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignMinusEquals(self)

class AssignMultiplicationEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignMultiplicationEquals(self)

class AssignDivideEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitDivideEquals(self)

class AssignModEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignModEquals(self)

class AssignAndEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignAndEquals(self)

class AssignOrEquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignOrEquals(self)

class AssignXOREquals(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignXOREquals(self)
    
class AssignDeslocationLeft(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignDeslocationLeft(self)

class AssignDeslocationRight(AssignAbstract):
    def __init__(self,id,exp):
        self.id = id
        self.exp = exp
    def accept(self,visitor):
        return visitor.visitAssignDeslocationRight(self)