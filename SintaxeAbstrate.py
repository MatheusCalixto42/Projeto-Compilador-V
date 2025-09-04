from abc import abstractmethod
from abc import ABCMeta

#####################################################
# Classes da Sintaxe Abstrata para Program
####################################################

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ImportAndFuncDefinition(Program):
    def __init__(self, program_import, program_items):
        self.program_import = program_import
        self.program_items = program_items
    def accept(self, visitor):
        return visitor.visitImportAndFuncDefinition(self)

class ProgramItems(Program):
    def __init__(self, program_items):
        self.program_items = program_items
    def accept(self, visitor):
        return visitor.visitProgramItems(self)

#######################################################
# Classes da Sintaxe Abstrata para Import
######################################################

class ProgramImport(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass    

class SequenceImports(ProgramImport):
    def __init__(self, import_token, id, program_import):
        self.import_token = import_token 
        self.id = id          
        self.program_import = program_import
    def accept(self, visitor):
        return visitor.visitSequenceImports(self)

class SingleImport(ProgramImport):
    def __init__(self, id, import_token):
        self.id = id
        self.import_token = import_token
    def accept(self, visitor):
        return visitor.visitSingleImport(self)
    
#######################################################
# Classes da Sintaxe Abstrata para Program Items
######################################################

class ProgramItemsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class MultipleProgramItems(ProgramItemsAbstract):
    def __init__(self, item, items_recursao):
        self.item = item
        self.items_recursao = items_recursao
    def accept(self, visitor):
        return visitor.visitMultipleProgramItems(self)

class NoneItems(ProgramItemsAbstract):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitNoneItems(self)

#######################################################
# Classes da Sintaxe Abstrata para Program Item
######################################################
class ProgramItemAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConstanteDeclaration(ProgramItemAbstract):
    def __init__(self, constante):
        self.constante = constante
    def accept(self, visitor):
        return visitor.visitConstanteDeclaration(self)

class FunctionDeclaration(ProgramItemAbstract):
    def __init__(self, function):
        self.function = function
    def accept(self, visitor):
        return visitor.visitFunctionDeclaration(self)

#######################################################
# Classes da Sintaxe Abstrata para Const
# ######################################################

class ConstanteDeclarationAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConstanteDeclarationRule(ConstanteDeclarationAbstract):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitConstanteDeclarationRule(self)

#######################################################
# Classes da Sintaxe Abstrata para Function Definition
######################################################

class FunctionDefinition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass   

class FunctionVoid(FunctionDefinition): # função com retorno void
    def __init__(self, id, param, block_statement):
        self.id = id
        self.param = param
        self.block_statement = block_statement
    def accept(self, visitor):
        return visitor.visitFunctionVoid(self)

class FunctionReturnType(FunctionDefinition): #função com retorno de algum tipo
    def __init__(self,id, param, type , block_statement):
        self.id = id
        self.param = param
        self.type = type
        self.block_statement = block_statement
    def accept(self, visitor):
        return visitor.visitFunctionReturnType(self)

class FunctionMain(FunctionDefinition): #função main
    def __init__(self, id, block_statement):
        self.id = id
        self.block_statement = block_statement
    def accept(self, visitor):
        return visitor.visitFunctionMain(self)   

#######################################################
# Classes da Sintaxe Abstrata para Param
######################################################

class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DescriptionParam(Param):
    def __init__(self,id, type):
        self.id = id
        self.type = type
    def accept(self, visitor):
        return visitor.visitDescriptionParam(self)

########################################################
# Classes da Sintaxe Abstrata para MoreParams
#######################################################
    
class MoreParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class MultipleParams(MoreParams):
    def __init__(self, param, more_params):
        self.param = param
        self.more_params = more_params
    def accept(self, visitor):
        return visitor.visitMultipleParams(self)

class NoneParam(MoreParams):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitNoneParam(self)
#Testar a ideia da linguagem sua -> criar uma regra no arquivo expressionlanguageparser em q tem o NONE sendo passado


########################################################
# Classe da Sintaxe Abstrata para Params
########################################################

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
#tiramos uma classe para vazio e colocamos uma regra no Expressionlanguageparser
class DescriptionParams(Params):
    def __init__(self, param, more_params):
        self.param = param
        self.more_params = more_params
    def accept(self, visitor):
        return visitor.visitDescriptionParams(self)

########################################################
# Classes da Sintaxe Abstrata para Type
#######################################################

class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class IntV(Type):
    def __init__(self, intv):
        self.intv = intv
    def accept(self, visitor):
        return visitor.visitIntV(self)

class F32(Type):
    def __init__(self, f32):
        self.f32 = f32
    def accept(self, visitor):
        return visitor.visitF32(self)

class F64(Type):
    def __init__(self,f64):
        self.f64 = f64
    def accept(self, visitor):
        return visitor.visitF64(self)

class Rune(Type):
    def __init__(self,rune):
        self.rune = rune
    def accept(self, visitor):
        return visitor.visitRune(self)

class String(Type):
    def __init__(self,string):
        self.string = string
    def accept(self, visitor):
        return visitor.visitString(self)

class BoolV(Type):
    def __init__(self,boolv):
        self.boolv = boolv
    def accept(self, visitor):
        return visitor.visitBoolV(self)
    

########################################################
# Classes da Sintaxe Abstrata para BlockStatement
#######################################################

class BlockStatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class BlockStatement(BlockStatementAbstract):
    def __init__(self, statements):
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitBlockStatement(self)

class NoneBlockStatement(BlockStatementAbstract):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitNoneBlockStatement(self)
    
#######################################################
# Classes da Sintaxe Abstrata para Statements
#######################################################

class StatementsAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class MultipleStatement(StatementsAbstract):
    def __init__(self, statement, statements):
        self.statement = statement
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitMultipleStatement(self)

class SingleStatement(StatementsAbstract):
    def __init__(self, statement):
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitSingleStatement(self)

########################################################
# Classes da Sintaxe Abstrata para Statement
#######################################################

class StatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class VarStatement(StatementAbstract):
    def __init__(self, var_statement ):
        self.var_statement = var_statement
    def accept(self, visitor):
        return visitor.visitVarStatement(self)

class VarAssignment(StatementAbstract):
    def __init__(self, var_assignment):
        self.var_assignment = var_assignment
    def accept(self, visitor):
        return visitor.visitVarAssignment(self)

class ListStatement(StatementAbstract):
    def __init__(self, list_statement):
        self.list_statement = list_statement
    def accept(self, visitor):
        return visitor.visitListStatement(self)

class ListAssignment(StatementAbstract):
    def __init__(self, list_assignment ):
        self.list_assignment = list_assignment
    def accept(self, visitor):
        return visitor.visitListAssignment(self)

class FuncCallS(StatementAbstract):
    def __init__(self, func_call):
        self.func_call = func_call
    def accept(self, visitor):
        return visitor.visitFuncCallS(self)

class IfStatement(StatementAbstract):
    def __init__(self, if_statement ):
        self.if_statement = if_statement
    def accept(self, visitor):
        return visitor.visitIfStatement(self)

class ForStatement(StatementAbstract):
    def __init__(self, for_statement ):
        self.for_statement = for_statement
    def accept(self, visitor):
        return visitor.visitForStatement(self)
    
class BreakStatement(StatementAbstract):
    def __init__(self, break_statement):
        self.break_statement = break_statement
    def accept(self, visitor):
        return visitor.visitBreakStatement(self)

class ReturnStatement(StatementAbstract):
    def __init__(self, return_statement):
        self.return_statement = return_statement
    def accept(self, visitor):
        return visitor.visitReturnStatement(self)
    
class IncrementStatement(StatementAbstract):
    def __init__(self, increment_statement):
        self.increment_statement = increment_statement
    def accept(self, visitor):
        return visitor.visitIncrementStatement(self)

class AssignmentStatement(StatementAbstract):
    def __init__(self, assignment_statement):
        self.assignment_statement = assignment_statement
    def accept(self, visitor):
        return visitor.visitAssignmentStatement(self)


#########################################################
# Classes da Sintaxe Abstrata para Var Statement
########################################################

class VarStatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclarationImutable(VarStatementAbstract):
    def __init__(self, declaration_imutable):
        self.declaration_imutable = declaration_imutable
    def accept(self, visitor):
        return visitor.visitDeclarationImutable(self)

class MutableDeclaration(VarStatementAbstract):
    def __init__(self, mut, id, expression):
        self.mut = mut
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitMutableDeclaration(self)

class ConstantDeclaration(VarStatementAbstract):
    def __init__(self, const, id, expression):
        self.const = const
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitConstantDeclaration(self)

##########################################################
# Classes da Sintaxe Abstrata para Var Assignment
#########################################################

class VarAssignmentAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VarModification(VarAssignmentAbstract):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarModification(self)

##########################################################
# Classes da Sintaxe Abstrata para List Statement
#########################################################

class ListStatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclarationImutableList(ListStatementAbstract):
    def __init__(self, declaration_imutable_list):
        self.declaration_imutable_list = declaration_imutable_list
    def accept(self, visitor):
        return visitor.visitDeclarationImutableList(self)

class DeclarationMutableList(ListStatementAbstract):
    def __init__(self, mut, id, id_list):
        self.mut = mut
        self.id = id
        self.id_list = id_list
    def accept(self, visitor):
        return visitor.visitDeclarationMutableList(self)

class DeclarationMutableListLengthDefinition(ListStatementAbstract):
    def __init__(self, mut, id, number, type):
        self.mut = mut
        self.id = id
        self.number = number
        self.type = type
    def accept(self, visitor):
        return visitor.visitDeclarationMutableListLengthDefinition(self)


##########################################################
# Classes da Sintaxe Abstrata para List Assignment
#########################################################

class ListAssignmentAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ListModification(ListAssignmentAbstract):
    def __init__(self, id, number, expression):
        self.id = id
        self.number = number
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitListModification(self)
    

##########################################################
# Classes da Sintaxe Abstrata para Declaration Imutable List
#########################################################

class DeclarationImutableListAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclarationImutableListRule(DeclarationImutableListAbstract):
    def __init__(self, id, id_list):
        self.id = id
        self.id_list = id_list  
    def accept(self, visitor):
        return visitor.visitDeclarationImutableListRule(self)

##########################################################
# Classes da Sintaxe Abstrata para Func Call
#########################################################

class FuncCall(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class FuncCompoundParams(FuncCall):
    def __init__(self, id, id_list):
        self.id = id
        self.id_list = id_list
    def accept(self, visitor):
        return visitor.visitFuncCompoundParams(self)

class FuncNoParams(FuncCall):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitFuncNoParams(self)

class FuncCallList(FuncCall):
    def __init__(self, funcCallList):
        self.funcCallList = funcCallList
    def accept(self, visitor):
        return visitor.visitFuncCallList(self)


##########################################################
# Classes da Sintaxe Abstrata para Func Call List
#########################################################

class FuncCallListAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):    
        pass

class FuncCallListAll(FuncCallListAbstract):
    def __init__(self, id, dotdot):
        self.id = id
        self.dotdot = dotdot
    def accept(self, visitor):
        return visitor.visitFuncCallListAll(self)

class FuncCallListRange(FuncCallListAbstract):
    def __init__(self, id, number, dotdot, number2):
        self.id = id
        self.number = number
        self.dotdot = dotdot
        self.number2 = number2
    def accept(self, visitor):
        return visitor.visitFuncCallListRange(self)

# class FuncCallListSingle(FuncCallListAbstract):
#     def __init__(self, id, number):
#         self.id = id
#         self.number = number
#     def accept(self, visitor):
#         return visitor.visitFuncCallListSingle(self)

##########################################################
# Classes da Sintaxe Abstrata para If Statement
#########################################################

class IdList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ListId(IdList):
    def __init__(self,expression, more_expression):
        self.expression = expression
        self.more_expression = more_expression
    def accept(self, visitor):
        return visitor.visitListId(self)

##########################################################
# Classes da Sintaxe Abstrata para More Expression
#########################################################

class MoreExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class PlusExpres(MoreExpression):
    def __init__(self, expression, more_expression):
        self.expression = expression
        self.more_expression = more_expression
    def accept(self, visitor):
        return visitor.visitPlusExpres(self)

class NoneExpression(MoreExpression):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitNoneExpression(self)

############################################################ 
# Classes da Sintaxe Abstrata para If Statement
###########################################################

class IfStatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class OnlyIf(IfStatementAbstract):
    def __init__(self,expressionrelational,blockstatement):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement
    def accept(self, visitor):
        return visitor.visitOnlyIf(self)

class IfAndElse(IfStatementAbstract):
    def __init__(self,expressionrelational,blockstatement,elseV):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement
        self.elseV = elseV
    def accept(self, visitor):
        return visitor.visitIfAndElse(self)

############################################################ 
# Classes da Sintaxe Abstrata para Else
###########################################################

class Else(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class ElseIf(Else):
    def __init__(self,if_statement):
        self.if_statement = if_statement
    def accept(self, visitor):
        return visitor.visitElseIf(self)

class OnlyElse(Else):
    def __init__(self,blockstatement):
        self.blockstatement = blockstatement
    def accept(self, visitor):
        return visitor.visitOnlyElse(self)

############################################################ 
# Classes da Sintaxe Abstrata para For
###########################################################

class For(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class ForEach(For):
    def __init__(self,id,expression,blockstatement):
        self.id = id
        self.expression = expression
        self.blockstatement = blockstatement
    def accept(self, visitor):
        return visitor.visitForEach(self)

class ConventionalFor(For):
    def __init__(self,declarationimutable,expressionrelational,increment, statement):
        self.declarationmutable = declarationimutable
        self.expressionrelational = expressionrelational
        self.increment = increment
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitConventionalFor(self)

class OnlyExpressionRelationalFor(For):
    def __init__(self,expressionrelational,blockstatement):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement
    def accept(self, visitor):
        return visitor.visitOnlyExpressionRelationalFor(self)

#######################################################
# Classes da Sintaxe Abstrata para Declaration Imutable
######################################################

class DeclarationImutableAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class IdImutable(DeclarationImutableAbstract):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitIdImutable(self)


#######################################################
# Classes da Sintaxe Abstrata para Break Statement
######################################################

class BreakStatementAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class OnlyBreak(BreakStatementAbstract):
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.visitOnlyBreak(self)

#######################################################
# Classes da Sintaxe Abstrata para Return Statement
######################################################

class Return(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ReturnExpression(Return):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitReturnExpression(self)

########################################################
# Classes da Sintaxe Abstrata para Expression
#######################################################

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressionPlus(Expression):
    def __init__(self, expression, term):
        self.expression = expression
        self.term = term
    def accept(self, visitor):
        return visitor.visitExpressionPlus(self)

class ExpressionMinus(Expression):
    def __init__(self, expression, term):
        self.expression = expression
        self.term = term
    def accept(self, visitor):
        return visitor.visitExpressionMinus(self)
    
class ExpressionIncrement(Expression):
    def __init__(self, increment):
        self.increment = increment
    def accept(self, visitor):
        return visitor.visitExpressionIncrement(self)
    
class ExpressionFuncCall(Expression):
    def __init__(self,funcCall):
        self.funcCall = funcCall
    def accept(self, visitor):
        return visitor.visitExpressionFuncCall(self)

class SingleTerm(Expression):
    def __init__(self, term):
        self.term = term
    def accept(self, visitor):
        return visitor.visitSingleTerm(self)

########################################################
# Classes da Sintaxe Abstrata para Expression Relational
#######################################################

class ExpressionRelational(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressionRelationalEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalEqual(self)

class ExpressionRelationalNotEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalNotEqual(self)


class ExpressionRelationalLessThan(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalLessThan(self)

class ExpressionRelationalGreaterThan(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalGreaterThan(self)

class ExpressionRelationalLessThanOrEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalLessThanOrEqual(self)

class ExpressionRelationalGreaterThanOrEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalGreaterThanOrEqual(self)

class ExpressionRelationalAnd(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalAnd(self)

class ExpressionRelationalOr(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def accept(self, visitor):
        return visitor.visitExpressionRelationalOr(self)

class ExpressionRelationalNot(ExpressionRelational):
    def __init__(self, expression):
        self.expression = expression 
    def accept(self, visitor):
        return visitor.visitExpressionRelationalNot(self)

############################################################ 
# Classes da Sintaxe Abstrata para Term
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
# Classes da Sintaxe Abstrata para Factor
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

class FactorExpression(Factor):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitFactorExpression(self)

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

class FactorInterpolationString(Factor):
    def __init__(self, interpolationString):
        self.interpolationString = interpolationString
    def accept(self, visitor):
        return visitor.visitFactorInterpolationString(self)

class FactorSizeOfExpression(Factor):
    def __init__(self, sizeofexpression):
        self.sizeofexpression = sizeofexpression
    def accept(self, visitor):
        return visitor.visitFactorSizeOfExpression(self)

############################################################ 
# Classes da Sintaxe Abstrata para Size of Expression
############################################################

class SizeOfExpressionAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SizeOfExpression(SizeOfExpressionAbstract):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitSizeOfExpression(self)

class SizeOfType(SizeOfExpressionAbstract):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor):
        return visitor.visitSizeOfType(self)

############################################################ 
# Classes da Sintaxe Abstrata para Increment
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
# Classes da Sintaxe Abstrata para Assignment
############################################################

class AssignmentAbstract(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignmentPlusEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitMaisIgual(self)

class AssignmentMinusEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitMenosIgual(self)

class AssignmentMultiplicationEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitMultiIgual(self)

class AssignmentDivideEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitDivIgual(self)

class AssignmentModEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitModIgual(self)

class AssignmentAndEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitAndIgual(self)

class AssignmentOrEquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitOrIgual(self)

class AssignmentXOREquals(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitXORIgual(self)
    
class AssignmentDeslocationLeft(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitDeslocaEsqIgual(self)

class AssignmentDeslocationRight(AssignmentAbstract):
    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    def accept(self,visitor):
        return visitor.visitDeslocaDirIgual(self)