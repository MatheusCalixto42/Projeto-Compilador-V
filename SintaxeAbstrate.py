from abc import abstractmethod
from abc import ABCMeta

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

class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DescriptionParam(Param):
    def __init__(self,id, type):
        self.id = id
        self.type = type
   
    
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


class FuncCall(metaclass=)







