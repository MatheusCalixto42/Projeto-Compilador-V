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
    def __init__(self, program_import, function_definition):
        self.program_import = program_import
        self.function_definition = function_definition
        

class SingleFuncDefinition(Program):
    def __init__(self,function_definition):
        self.function_definition = function_definition

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

class SingleImport(ProgramImport):
    def __init__(self, id, import_token):
        self.id = id
        self.import_token = import_token

#######################################################
# Classes da Sintaxe Abstrata para Function Definition
######################################################

class FunctionDefinition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass   

class FunctionVoid(FunctionDefinition): # função com retorno void
    def __init__(self, id, param, block_statement, function_definition):
        self.id = id
        self.param = param
        self.block_statement = block_statement
        self.function_definition = function_definition

class FunctionReturnType(FunctionDefinition): #função com retorno de algum tipo
    def __init__(self,id, param, type , block_statement, function_definition ):
        self.id = id
        self.param = param
        self.type = type
        self.block_statement = block_statement
        self.function_definition = function_definition
        
class FunctionMain(FunctionDefinition): #função main
    def __init__(self, main, block_statement, function_definition_without_main):
        self.main = main
        self.block_statement = block_statement
        self.function_definition_without_main = function_definition_without_main

#######################################################
# Classes da Sintaxe Abstrata para Function Definition without main
######################################################

class function_definition_without_main(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class FunctionVoidWithoutMain(function_definition_without_main): #funções voids sem ter main
    def __init__(self,id,param,block_statement,function_definition_without_main):
        self.id = id
        self.param = param
        self.block_statement = block_statement
        self.function_definition_without_main = function_definition_without_main 

class FunctionReturnTypeWithoutMain(function_definition_without_main): #funções sem main que retornam algo
    def __init__(self,id,type,block_statement,function_definition_without_main):
        self.id = id
        self.type = type
        self.block_statement = block_statement
        self.function_definition_without_main = function_definition_without_main

#######################################################
# Classes da Sintaxe Abstrata para Param
######################################################

class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class NoneParam(Param):
    def __init__(self):
        pass
    
class DescriptionParam(Param):
    def __init__(self,id, type):
        self.id = id
        self.type = type

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

class SingleParam(MoreParams):
    def __init__(self, param):
        self.param = param

########################################################
# Classes da Sintaxe Abstrata para Type
#######################################################

class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class Int(Type):
    def __init__(self, int):
        self.int = int

class F32(Type):
    def __init__(self, f32):
        self.f32 = f32

class F64(Type):
    def __init__(self,f64):
        self.f64 = f64

class Rune(Type):
    def __init__(self,rune):
        self.rune = rune

class String(Type):
    def __init__(self,string):
        self.string = string

class Bool(Type):
    def __init__(self,bool):
        self.bool = bool

########################################################
# Classes da Sintaxe Abstrata para Block Statement
#######################################################

class BlockStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class VarDeclaration(BlockStatement):
    def __init__(self, var_statament):
        self.var_statament = var_statament

class VarAssignment(BlockStatement):
    def __init__(self, var_assignment):
        self.var_assignment = var_assignment

class IfStatement(BlockStatement):
    def __init__(self, if_statement):
        self.if_statement = if_statement

class ForStatement(BlockStatement):
    def __init__(self, for_statement):
        self.for_statement = for_statement

class ReturnStatement(BlockStatement):
    def __init__(self, return_statement):
        self.return_statement = return_statement

#########################################################
# Classes da Sintaxe Abstrata para Var Statement
########################################################

class VarStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclarationImutable(VarStatement):
    def __init__(self, declaration_imutable):
        self.declaration_imutable = declaration_imutable

class MutableDeclaration(VarStatement):
    def __init__(self, mut, id, expression):
        self.mut = mut
        self.id = id
        self.expression = expression

class ConstantDeclaration(VarStatement):
    def __init__(self, const, id, expression):
        self.const = const
        self.id = id
        self.expression = expression

##########################################################
# Classes da Sintaxe Abstrata para Var Assignment
#########################################################

class VarAssignment(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VarModification(VarAssignment):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
       
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

class FuncNoParams(FuncCall):
    def __init__(self, id):
        self.id = id

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

class NoneExpression(MoreExpression):
    def __init__(self):
        pass
    
############################################################ 
# Classes da Sintaxe Abstrata para If Statement
###########################################################

class IfStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class OnlyIf(IfStatement):
    def __init__(self,expressionrelational,blockstatement):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement

class IfAndElse(IfStatement):
    def __init__(self,expressionrelational,blockstatement,elseV):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement
        self.elseV = elseV

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

class OnlyElse(Else):
    def __init__(self,blockstatement):
        self.blockstatement = blockstatement

############################################################ 
# Classes da Sintaxe Abstrata para For
###########################################################

class For(metaClass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class ForEach(For):
    def __init__(self,id,expression,blockstatement):
        self.id = id
        self.expression = expression
        self.blockstatement = blockstatement

class ConventionalFor(For):
    def __init__(self,declarationimutable,expressionrelational,increment):
        self.declarationmutable = declarationimutable
        self.expressionrelational = expressionrelational
        self.increment = increment

class OnlyExpressionRelationalFor(For):
    def __init__(self,expressionrelational,blockstatement):
        self.expressionrelational = expressionrelational
        self.blockstatement = blockstatement

#######################################################
# Classes da Sintaxe Abstrata para Declaration Imutable
######################################################

class DeclarationImutable(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ID_imutable(DeclarationImutable):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

#######################################################
# Classes da Sintaxe Abstrata para Return Statement
######################################################

class ReturnStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ReturnExpression(ReturnStatement):
    def __init__(self, expression):
        self.expression = expression

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

class ExpressionMinus(Expression):
    def __init__(self, expression, term):
        self.expression = expression
        self.term = term

class SingleTerm(Expression):
    def __init__(self, term):
        self.term = term

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

class ExpressionRelationalNotEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

class ExpressionRelationalLessThan(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

class ExpressionRelationalGreaterThan(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

class ExpressionRelationalLessThanOrEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

class ExpressionRelationalGreaterThanOrEqual(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2  

class ExpressionRelationalAnd(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2  

class ExpressionRelationalOr(ExpressionRelational):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2  

class ExpressionRelationalNot(ExpressionRelational):
    def __init__(self, expression):
        self.expression = expression    

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

class Division(Term):
    def __init__(self, term,factor):
        self.term = term
        self.factor = factor

class Mod(Term):
    def __init__(self, term,factor):
        self.term = term
        self.factor = factor

class OnlyFactor(Term):
    def __init__(self, factor):
        self.factor = factor


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

class FactorNumber(Factor):
    def __init__(self, number):
        self.number = number    

class FactorString(Factor):
    def __init__(self, string):
        self.string = string

class FactorTrue(Factor):
    def __init__(self, true):
        self.true = true    

class FactorFalse(Factor):
    def __init__(self, false):
        self.false = false  

class FactorRune(Factor):
    def __init__(self, rune):
        self.rune = rune

class FactorExpression(Factor):
    def __init__(self, expression):
        self.expression = expression

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

class Dec(Increment):
    def __init__(self,id):
        self.id = id