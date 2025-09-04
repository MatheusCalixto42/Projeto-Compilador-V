import ply.yacc as yacc
from LexicoV import *
import SintaxeAbstrate as sa

def p_program1(p):
    '''program : program_Import program_items'''
    p[0] = sa.ImportAndFuncDefinition(p[1],p[2])

def p_program2(p):
    '''program : program_items'''
    p[0] = sa.ProgramItems(p[1])

def p_program_import1(p):
    '''program_Import : IMPORT ID program_Import'''
    p[0] = sa.SequenceImports(p[1],p[2],p[3])

def p_program_import2(p):
    '''program_Import : IMPORT ID'''
    p[0] = sa.SingleImport(p[1], p[2])

def p_program_items_multiple(p):
    '''program_items : program_item program_items'''
    p[0] = sa.MultipleProgramItems(p[1], p[2])

def p_program_items_empty(p):
    '''program_items :'''
    p[0] = sa.NoneItems()

def p_program_item_const(p):
    '''program_item : const_declaration'''
    p[0] = sa.ConstanteDeclaration(p[1])

def p_program_item_function(p):
    '''program_item : function_definition'''
    p[0] = sa.FunctionDeclaration(p[1])

def p_program_const_declaration_rule(p):
    '''const_declaration : CONST ID DECLARE_ASSIGN expression'''
    p[0] = sa.ConstanteDeclarationRule(p[2], p[4])

def p_function_definition1(p):
    '''function_definition : FN ID LPAREN params RPAREN LBRACE block_statement RBRACE '''
    p[0] = sa.FunctionVoid(p[2], p[4], p[7])

def p_function_definition2(p):
    '''function_definition : FN ID LPAREN params RPAREN type LBRACE block_statement RBRACE '''
    p[0] = sa.FunctionReturnType(p[2], p[4], p[6], p[8])

def p_function_definition3(p):
    '''function_definition : FN MAIN LPAREN RPAREN LBRACE block_statement RBRACE function_definition_without_main'''
    p[0] = sa.FunctionMain(p[2], p[6], p[8])

def p_function_definition_main_no_loop(p):
    '''function_definition : FN MAIN LPAREN RPAREN LBRACE block_statement RBRACE '''
    p[0] = sa.FunctionMain(p[2], p[6], None)

def p_function_definition_without_main1(p):
    '''function_definition_without_main : FN ID LPAREN params RPAREN LBRACE block_statement RBRACE function_definition_without_main'''
    p[0] = sa.FunctionVoidWithoutMain(p[2], p[4], p[7], p[9])

def p_function_definition_without_main2(p):
    '''function_definition_without_main : FN ID LPAREN params RPAREN type LBRACE block_statement RBRACE function_definition_without_main'''
    p[0] = sa.FunctionReturnTypeWithoutMain(p[2], p[4], p[6], p[8], p[10])

def p_function_definition_without_main1_no_loop(p):
    '''function_definition_without_main : FN ID LPAREN params RPAREN LBRACE block_statement RBRACE '''
    p[0] = sa.FunctionVoidWithoutMain(p[2], p[4], p[7], None)

def p_function_definition_without_main2_no_loop(p):
    '''function_definition_without_main : FN ID LPAREN params RPAREN type LBRACE block_statement RBRACE '''
    p[0] = sa.FunctionReturnTypeWithoutMain(p[2], p[4], p[6], p[8], None)

#def p_none_function(p):
#   '''function_definition_without_main : '''
#    p[0] = sa.NoneFunction()

def p_params(p):
    '''params : param more_params'''
    p[0] = sa.DescriptionParams(p[1], p[2])


def p_more_param(p):
    '''more_params : COMMA param more_params'''
    p[0] = sa.MultipleParams(p[2], p[3])

#isso aqui funciona?
def p_more_param_empty(p): 
    '''more_params :'''
    p[0] = sa.NoneParam()


def p_param(p):
    '''param : ID type'''
    p[0] = sa.DescriptionParam(p[1], p[2])

def p_type1(p):
    '''type : INT'''
    p[0] = sa.IntV(p[1])

def p_type2(p):
    '''type : F32'''
    p[0] = sa.F32(p[1])

def p_type3(p):
    '''type : F64'''
    p[0] = sa.F64(p[1])

def p_type4(p):
    '''type : STRING'''
    p[0] = sa.String(p[1])

def p_type5(p):
    '''type : BOOL'''
    p[0] = sa.BoolV(p[1])

def p_type6(p):
    '''type : RUNE'''
    p[0] = sa.Rune(p[1])

def p_block_statement(p):
    '''block_statement :  statement '''
    p[0] = sa.BlockStatement(p[1])

def p_statement(p):
    '''statement :  var_statement statement'''
    p[0] = sa.VarStatement(p[1], p[2])

def p_statement2(p):
    '''statement :  var_assignment statement'''
    p[0] = sa.VarAssignment(p[1], p[2])

def p_statement3(p):
    '''statement :  func_call statement'''
    p[0] = sa.FuncCallS(p[1],p[2])

def p_statement4(p):
    '''statement :  if_statement statement'''
    p[0] = sa.IfStatement(p[1], p[2])

def p_statement5(p):
    '''statement :  for_statement statement'''
    p[0] = sa.ForStatement(p[1], p[2])

def p_break_statement_rule(p):
    '''statement : break_statement'''
    p[0] = sa.BreakStatement(p[1])

def p_statement6(p):
    '''statement :  return_statement'''
    p[0] = sa.ReturnStatement(p[1])

def p_statement7(p):
    '''statement : '''
    p[0] = sa.NoneStatement()

def p_statement8(p):
    '''statement : list_statement statement'''
    p[0] = sa.ListStatement(p[1], p[2])

def p_statement9(p):
    '''statement :  list_assignment statement'''
    p[0] = sa.ListAssignment(p[1], p[2])

def p_statement10(p):
    '''statement :  increment_rule statement'''
    p[0] = sa.IncrementStatement(p[1], p[2])

def p_statement_assignment(p):
    '''statement : assignment statement'''
    p[0] = sa.AssignmentStatement(p[1], p[2])

def p_var_declaration(p):
    '''var_statement :  declaration_imutable'''
    p[0] = sa.DeclarationImutable(p[1])

def p_var_declaration2(p):
    '''var_statement :  MUT ID DECLARE_ASSIGN expression'''
    p[0] = sa.MutableDeclaration(p[1], p[2], p[4])

def p_var_declaration3(p):
    '''var_statement :  CONST ID DECLARE_ASSIGN expression '''
    p[0] = sa.ConstantDeclaration(p[1], p[2], p[4])

def p_var_assignment(p):
    '''var_assignment :  ID ASSIGN expression'''
    p[0] = sa.VarModification(p[1], p[3])

def p_list_declaration_imutable(p):
    '''list_statement : declaration_imutable_list'''
    p[0] = sa.DeclarationImutableList(p[1])

def p_list_declaration_mutable(p):
    '''list_statement : MUT ID DECLARE_ASSIGN LBRACKET id_list RBRACKET'''
    p[0] = sa.DeclarationMutableList(p[1], p[2], p[5])

def p_list_declaration_mutable_list_lenght_definition(p):
    '''list_statement : MUT ID DECLARE_ASSIGN LBRACKET id_list RBRACKET type'''
    p[0] = sa.DeclarationMutableListLengthDefinition(p[1], p[2], p[5], p[7])

def p_list_assignment(p):
    '''list_assignment : ID LBRACKET NUMBER RBRACKET ASSIGN expression'''
    p[0] = sa.ListModification(p[1], p[3], p[6])

def p_func_call(p):
    '''func_call : ID LPAREN id_list RPAREN'''
    p[0] = sa.FuncCompoundParams(p[1], p[3])

def p_func_call_empty(p):
    '''func_call : ID LPAREN RPAREN'''
    p[0] = sa.FuncNoParams(p[1])

def p_func_call_list(p):
    '''func_call : func_call_list'''
    p[0] = sa.FuncCallList(p[1])

def p_func_call_list_all(p):
    '''func_call_list : ID LBRACKET DOTDOT RBRACKET'''
    p[0] = sa.FuncCallListAll(p[1], p[3])


def p_func_call_list_range(p):
    '''func_call_list : ID LBRACKET NUMBER DOTDOT NUMBER RBRACKET'''
    p[0] = sa.FuncCallListRange(p[1], p[3], p[4], p[5])

# def p_func_call_list_single(p):
#     '''func_call_list : ID LBRACKET NUMBER RBRACKET'''
#     p[0] = sa.FuncCallListSingle(p[1], p[3])

def p_id_list(p):
    '''id_list : expression more_expressions'''
    p[0] = sa.ListId(p[1], p[2])

def p_more_expression(p):
    '''more_expressions : COMMA expression more_expressions'''
    p[0] = sa.PlusExpres(p[2], p[3])

#ou essa abordagem?
def p_more_expression_empty(p):
    '''more_expressions :'''
    p[0] = sa.NoneExpression()

def p_if_statement(p):
    '''if_statement : IF expression_relacional LBRACE statement RBRACE'''
    p[0] = sa.OnlyIf(p[2], p[4])

def p_if_statement_else(p):
    '''if_statement : IF expression_relacional LBRACE statement RBRACE elseop'''
    p[0] = sa.IfAndElse(p[2], p[4], p[6])

def p_else(p):
    '''elseop : ELSE if_statement'''
    p[0] = sa.ElseIf(p[2])

def p_else2(p):
    '''elseop : ELSE LBRACE statement RBRACE'''
    p[0] = sa.OnlyElse(p[3])

def p_for_each_statement(p):
    '''for_statement : FOR ID IN expression LBRACE statement RBRACE'''
    p[0] = sa.ForEach(p[2], p[4], p[6])

def p_for_statement(p):
    '''for_statement : FOR declaration_imutable SEMICOLON expression_relacional SEMICOLON increment_rule LBRACE statement RBRACE'''
    p[0] = sa.ConventionalFor(p[2], p[4], p[6], p[8])

def p_for_statement2(p):
    '''for_statement : FOR expression_relacional LBRACE statement RBRACE'''
    p[0] = sa.OnlyExpressionRelationalFor(p[2], p[4])

def p_declaration_imutable(p):
    '''declaration_imutable : ID DECLARE_ASSIGN expression'''
    p[0] = sa.IdImutable(p[1], p[3])

def p_declaration_imutable_list(p):
    '''declaration_imutable_list : ID DECLARE_ASSIGN LBRACKET id_list RBRACKET'''
    p[0] = sa.DeclarationImutableListRule(p[1], p[4])

def p_break_only(p):
    '''break_statement : BREAK'''
    p[0] = sa.OnlyBreak()

def p_return_statement(p):
    '''return_statement : RETURN expression'''
    p[0] = sa.ReturnExpression(p[2])

def p_expression_plus(p):
    '''expression : expression PLUS term'''
    p[0] = sa.ExpressionPlus(p[1], p[3])

def p_expression_minus(p):
    '''expression : expression MINUS term'''
    p[0] = sa.ExpressionMinus(p[1], p[3])

def p_expression_increment(p):
    '''expression :  increment_rule'''
    p[0] = sa.ExpressionIncrement(p[1])

def p_expression_func_call(p):
    '''expression : func_call'''
    p[0] = sa.ExpressionFuncCall(p[1])

def p_expression_term(p):
    '''expression : term'''
    p[0] = sa.SingleTerm(p[1])

def p_term_mult(p):
    '''term : term TIMES factor'''
    p[0] = sa.Multiplication(p[1], p[3])

def p_term_divide(p):
    '''term : term DIVIDE factor'''
    p[0] = sa.Division(p[1], p[3])

def p_term_mod(p):
    '''term : term MOD factor'''
    p[0] = sa.Mod(p[1], p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = sa.OnlyFactor(p[1])

def p_factor_id(p):
    '''factor : ID'''
    p[0] = sa.FactorID(p[1])

def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = sa.FactorNumber(p[1])

def p_factor_number_float(p):
    '''factor : NUMBERFLOAT'''
    p[0] = sa.FactorNumberFloat(p[1])

def p_factor_string(p):
    '''factor : WORD'''
    p[0] = sa.FactorString(p[1])

def p_factor_true(p):
    '''factor : TRUE'''
    p[0] = sa.FactorTrue(p[1])

def p_factor_false(p):
    '''factor : FALSE'''
    p[0] = sa.FactorFalse(p[1])

def p_factor_rune(p):
    '''factor : RUNEVALOR'''
    p[0] = sa.FactorRune(p[1])

def p_factor_expression(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = sa.FactorExpression(p[2])

def p_factor_list(p):
    '''factor : ID LBRACKET NUMBER RBRACKET'''
    p[0] = sa.FactorList(p[1], p[3])
    
def p_factor_cientific_notation(p):
    '''factor : NOTACAOCIENTIFICA'''
    p[0] = sa.FactorCientificNotation(p[1])

def p_factor_binary(p):
    '''factor : BINARY'''
    p[0] = sa.FactorBinary(p[1])

def p_factor_octal(p):
    '''factor : OCTAL'''    
    p[0] = sa.FactorOctal(p[1])

def p_factor_hex(p):
    '''factor : HEX'''
    p[0] = sa.FactorHex(p[1])

def p_factor_interpolation_string(p):
    '''factor : INTERPOLATIONSTRING'''
    p[0] = sa.FactorInterpolationString(p[1])

def p_factor_size_of_expression_rule(p):
    '''factor : size_of_expression'''
    p[0] = sa.FactorSizeOfExpression(p[1])

def p_size_of_expression(p):
    '''size_of_expression : SIZEOF LPAREN expression RPAREN'''
    p[0] = sa.SizeOfExpression(p[3])

def p_size_of_type(p):
    '''size_of_expression : SIZEOF LPAREN type RPAREN'''
    p[0] = sa.SizeOfType(p[3])

def p_increment_plus(p):
    '''increment_rule : ID INCREMENT'''
    p[0] = sa.Inc(p[1])

def p_increment_minus(p):
    '''increment_rule : ID DECREMENT'''
    p[0] = sa.Dec(p[1])

def p_expression_relacional_equals(p):
    '''expression_relacional : expression EQ expression'''
    p[0] = sa.ExpressionRelationalEqual(p[1], p[3])

def p_expression_relacional_not_equals(p):
    '''expression_relacional : expression NEQ expression'''
    p[0] = sa.ExpressionRelationalNotEquals(p[1], p[3])

def p_expression_relacional_less_than(p):
    '''expression_relacional : expression LT expression'''
    p[0] = sa.ExpressionRelationalLessThan(p[1], p[3])

def p_expression_relacional_less_than_or_equal(p):
    '''expression_relacional : expression LE expression'''
    p[0] = sa.ExpressionRelationalLessThanOrEqual(p[1], p[3])

def p_expression_relacional_greater_than(p):
    '''expression_relacional : expression GT expression'''
    p[0] = sa.ExpressionRelationalGreaterThan(p[1], p[3])

def p_expression_relacional_greater_than_or_equal(p):
    '''expression_relacional : expression GE expression'''
    p[0] = sa.ExpressionRelationalGreaterThanOrEqual(p[1], p[3])

def p_expression_relacional_and(p):
    '''expression_relacional : expression AND expression'''
    p[0] = sa.ExpressionRelationalAnd(p[1], p[3])

def p_expression_relacional_or(p):
    '''expression_relacional : expression OR expression'''
    p[0] = sa.ExpressionRelationalOr(p[1], p[3])    

def p_expression_relacional_not(p):
    '''expression_relacional : NOT expression'''
    p[0] = sa.ExpressionRelationalNot(p[2])

def p_assignment_plus_equals(p):
    '''assignment : ID PLUS_ASSIGN expression'''
    p[0] = sa.AssignmentPlusEquals(p[1], p[3])

def p_assignment_minus_equal(p):
    '''assignment : ID MINUS_ASSIGN expression'''
    p[0] = sa.AssignmentMinusEquals(p[1], p[3])

def p_assignment_multiply_equals(p):
    '''assignment : ID TIMES_ASSIGN expression'''
    p[0] = sa.AssignmentMultiplicationEquals(p[1], p[3])

def p_assignment_divide_equals(p):
    '''assignment : ID DIVIDE_ASSIGN expression'''
    p[0] = sa.AssignmentDivideEquals(p[1], p[3])

def p_assignment_mod_equals(p):
    '''assignment : ID MOD_ASSIGN expression'''
    p[0] = sa.AssignmentModEquals(p[1], p[3])

def p_assignment_and_equals(p):
    '''assignment : ID BIT_AND_ASSIGN expression'''
    p[0] = sa.AssignmentAndEquals(p[1], p[3])

def p_assignment_or_equals(p):
    '''assignment : ID BIT_OR_ASSIGN expression'''
    p[0] = sa.AssignmentOrEquals(p[1], p[3])

def p_assignment_exp_equals(p):
    '''assignment : ID BIT_XOR_ASSIGN expression'''
    p[0] = sa.AssignmentXOREquals(p[1], p[3])

def p_assignment_lshift(p):
    '''assignment : ID BIT_LSHIFT_ASSIGN expression'''
    p[0] = sa.AssignmentDeslocationLeft(p[1], p[3])

def p_assignment_rshift(p):
    '''assignment : ID BIT_RSHIFT_ASSIGN expression'''
    p[0] = sa.AssignmentDeslocationRight(p[1], p[3])


def p_error(p):
    print("Syntax error in input!")

def main():
    f = open("teste.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()