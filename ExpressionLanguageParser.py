import ply.yacc as yacc
from LexicoV import *
import SintaxeAbstrate as sa

def p_program1(p):
    '''Program : Program_Import Function_Definition'''
    p[0] = sa.ImportAndFuncDefinition(p[1],p[2])

def p_program2(p):
    '''Program : Function_definition'''
    p[0] = sa.SingleFuncDefinition(p[1])

def p_program_import1(p):
    '''Program_import : IMPORT ID Program_import'''
    p[0] = sa.SequenceImports(p[1],p[2],p[3])

def p_program_import2(p):
    '''Program_import : IMPORT ID'''
    p[0] = sa.SingleImport(p[1], p[2])

def p_function_definition1(p):
    '''Function_definition : FN ID LPAREN Param RPAREN LBRACE Block_statement RBRACE Function_definition'''
    p[0] = sa.FunctionVoid(p[2], p[4], p[7], p[9])

def p_function_definition2(p):
    '''Function_definition : FN ID LPAREN Param RPAREN Type LBRACE Block_statement RBRACE Function_definition'''
    p[0] = sa.FunctionReturnType(p[2], p[4], p[6], p[8], p[10])

def p_function_definition3(p):
    '''Function_definition : FN MAIN LPAREN RPAREN LBRACE Block_statement RBRACE Function_definition_without_main'''
    p[0] = sa.FunctionMain(p[2], p[6], p[8])

def p_function_definition_without_main1(p):
    '''Function_definition_without_main : FN ID LPAREN Param RPAREN LBRACE Block_statement RBRACE Function_definition_without_main'''
    p[0] = sa.FunctionVoidWithoutMain(p[2], p[4], p[7], p[9])

def p_function_definition_without_main2(p):
    '''Function_definition_without_main : FN ID LPAREN Param RPAREN Type LBRACE Block_statement RBRACE Function_definition_without_main'''
    p[0] = sa.FunctionReturnTypeWithoutMain(p[2], p[4], p[6], p[8], p[10])


def p_params(p):
    '''Params : Param More_Params'''
    p[0] = sa.DescriptionParams(p[1], p[2])


def p_more_param(p):
    '''More_param : COMMA Param More_Params'''
    p[0] = sa.MultipleParams(p[2], p[3])

#isso aqui funciona?
def p_more_param_empty(p): 
    '''More_param :'''
    p[0] = sa.MultipleParams(None, None)


def p_param(p):
    '''Param : ID Type'''
    p[0] = sa.DescriptionParam(p[1], p[2])

def p_type1(p):
    '''Type : INT'''
    p[0] = sa.IntV(p[1])

def p_type2(p):
    '''Type : F32'''
    p[0] = sa.F32(p[1])

def p_type3(p):
    '''Type : F64'''
    p[0] = sa.F64(p[1])

def p_type4(p):
    '''Type : STRING'''
    p[0] = sa.String(p[1])

def p_type5(p):
    '''Type : BOOL'''
    p[0] = sa.BoolV(p[1])

def p_type6(p):
    '''Type : RUNE'''
    p[0] = sa.Rune(p[1])

def p_block_statement(p):
    '''Block_statement :  Var_statement'''
    p[0] = sa.VarDeclaration(p[1])

def p_block_statement2(p):
    '''Block_statement :  Var_assignment'''
    p[0] = sa.VarAssignment(p[1])

def p_block_statement3(p):
    '''Block_statement :  Func_call'''
    p[0] = sa.FuncCall(p[1])

def p_block_statement4(p):
    '''Block_statement :  If_statement'''
    p[0] = sa.IfStatement(p[1])

def p_block_statement5(p):
    '''Block_statement :  For_statement'''
    p[0] = sa.ForStatement(p[1])

def p_block_statement6(p):
    '''Block_statement :  Return_statement'''
    p[0] = sa.ReturnStatement(p[1])

def p_var_declaration(p):
    '''Var_declaration :  DeclarationImutable'''
    p[0] = sa.DeclarationImutable(p[1])

def p_var_declaration2(p):
    '''Var_declaration :  MUT ID DECLARE_ASSIGN Expression'''
    p[0] = sa.MutableDeclaration(p[1], p[2], p[4])

def p_var_declaration3(p):
    '''Var_declaration :  CONST ID DECLARE_ASSIGN Expression '''
    p[0] = sa.ConstantDeclaration(p[1], p[2], p[4])

def p_var_assignment(p):
    '''Var_assignment :  ID ASSIGN Expression '''
    p[0] = sa.VarModification(p[1], p[3])

def p_func_call(p):
    '''Func_call : ID LPAREN id_list RPAREN'''
    p[0] = sa.FuncCompoundParams(p[1], p[3])

def p_func_call_empty(p):
    '''Func_call : ID LPAREN RPAREN'''
    p[0] = sa.FuncNoParams(p[1])

def p_id_list(p):
    '''id_list : Expression more_Expressions'''
    p[0] = sa.ListId(p[1], p[2])

def p_more_expression(p):
    '''more_Expressions : COMMA Expression more_Expressions'''
    p[0] = sa.PlusExpres(p[2], p[3])

#ou essa abordagem?
def p_more_expression_empty(p):
    '''more_Expressions :'''
    p[0] = sa.NoneExpression()

def p_if_statement(p):
    '''If_statement : IF ExpressionRelacional LBRACE Block_statement RBRACE'''
    p[0] = sa.OnlyIf(p[2], p[4])

def p_if_statement_else(p):
    '''If_statement_else : IF ExpressionRelacional LBRACE Block_statement RBRACE Else? '''
    p[0] = sa.IfAndElse(p[2], p[4], p[6])

def p_else(p):
    '''Else : ELSE If_statement'''
    p[0] = sa.ElseIf(p[2])

def p_else2(p):
    '''Else2 : ELSE LBRACE Block_statement RBRACE'''
    p[0] = sa.OnlyElse(p[3])

def p_for_each_statement(p):
    '''For_statement : FOR ID IN Expression LBRACE Block_statement RBRACE'''
    p[0] = sa.ForEach(p[2], p[4], p[6])

def p_for_statement(p):
    '''For_statement : FOR DeclarationImutable SEMICOLON ExpressionRelacional SEMICOLON Increment LBRACE Block_statement RBRACE'''
    p[0] = sa.ConventionalFor(p[2], p[4], p[6], p[8])

def p_for_statement2(p):
    '''For_statement : FOR ExpressionRelacional LBRACE Block_statement RBRACE'''
    p[0] = sa.OnlyExpressionRelationalFor(p[2], p[4])

def p_declaration_imutable(p):
    '''DeclarationImutable : ID DECLARE_ASSIGN Expression'''
    p[0] = sa.IdImutable(p[1], p[3])


def p_return_statement(p):
    '''Return_statement : RETURN Expression'''
    p[0] = sa.ReturnExpression(p[2])

def p_expression_plus(p):
    '''Expression : Expression PLUS Term'''
    p[0] = sa.ExpressionPlus(p[1], p[3])

def p_expression_minus(p):
    '''Expression : Expression MINUS Term'''
    p[0] = sa.ExpressionMinus(p[1], p[3])

def p_expression_term(p):
    '''Expression : Term'''
    p[0] = sa.SingleTerm(p[1])

def p_term_mult(p):
    '''Term : Term TIMES Factor'''
    p[0] = sa.Multiplication(p[1], p[3])

def p_term_divide(p):
    '''Term : Term DIVIDE Factor'''
    p[0] = sa.Division(p[1], p[3])

def p_term_mod(p):
    '''Term : Term MOD Factor'''
    p[0] = sa.Mod(p[1], p[3])

def p_term_factor(p):
    '''Term : Factor'''
    p[0] = sa.OnlyFactor(p[1])

def p_factor_id(p):
    '''Factor : ID'''
    p[0] = sa.FactorID(p[1])

def p_factor_number(p):
    '''Factor : NUMBER'''
    p[0] = sa.FactorNumber(p[1])

def p_factor_string(p):
    '''Factor : STRING'''
    p[0] = sa.FactorString(p[1])

def p_factor_true(p):
    '''Factor : TRUE'''
    p[0] = sa.FactorTrue(p[1])

def p_factor_false(p):
    '''Factor : FALSE'''
    p[0] = sa.FactorFalse(p[1])

def p_factor_rune(p):
    '''Factor : RUNE'''
    p[0] = sa.FactorRune(p[1])

def p_factor_expression(p):
    '''Factor : LPAREN Expression RPAREN'''
    p[0] = sa.FactorExpression(p[2])

def p_increment_plus(p):
    '''Increment : ID PLUS PLUS'''
    p[0] = sa.Inc(p[1])

def p_increment_minus(p):
    '''Increment : ID MINUS MINUS'''
    p[0] = sa.Dec(p[1])

def p_expression_relacional_equals(p):
    '''ExpressionRelacional : Expression EQ Expression'''
    p[0] = sa.ExpressionRelationalEqual(p[1], p[3])

def p_expression_relacional_not_equals(p):
    '''ExpressionRelacional : Expression NEQ Expression'''
    p[0] = sa.ExpressionRelationalNotEquals(p[1], p[3])

def p_expression_relacional_less_than(p):
    '''ExpressionRelacional : Expression LT Expression'''
    p[0] = sa.ExpressionRelationalLessThan(p[1], p[3])

def p_expression_relacional_less_than_or_equal(p):
    '''ExpressionRelacional : Expression LE Expression'''
    p[0] = sa.ExpressionRelationalLessThanOrEqual(p[1], p[3])

def p_expression_relacional_greater_than(p):
    '''ExpressionRelacional : Expression GT Expression'''
    p[0] = sa.ExpressionRelationalGreaterThan(p[1], p[3])

def p_expression_relacional_greater_than_or_equal(p):
    '''ExpressionRelacional : Expression GE Expression'''
    p[0] = sa.ExpressionRelationalGreaterThanOrEqual(p[1], p[3])

def p_expression_relacional_and(p):
    '''ExpressionRelacional : Expression AND Expression'''
    p[0] = sa.ExpressionRelationalAnd(p[1], p[3])

def p_expression_relacional_or(p):
    '''ExpressionRelacional : Expression OR Expression'''
    p[0] = sa.ExpressionRelationalOr(p[1], p[3])    

def p_expression_relacional_not(p):
    '''ExpressionRelacional : NOT Expression'''
    p[0] = sa.ExpressionRelationalNot(p[2])

def p_error(p):
    print("Syntax error in input!")
