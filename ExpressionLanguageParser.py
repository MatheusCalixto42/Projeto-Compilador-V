import ply.yacc as yacc
from LexicoV import *
import SintaxeAbstrate as sa

def p_program1(p):
    '''program : program_import program_items'''
    p[0] = sa.CompoundImportItems(p[1],p[2])

def p_program2(p):
    '''program : program_items'''
    p[0] = sa.ProgramItems(p[1])

def p_program_import1(p):
    '''program_import : IMPORT ID program_import'''
    p[0] = sa.SequenceImports(p[1],p[2],p[3])

def p_program_import2(p):
    '''program_import : IMPORT ID'''
    p[0] = sa.SingleImport(p[1], p[2])

def p_program_sequence_items(p):
    '''program_items : program_item program_items'''
    p[0] = sa.SequenceProgramItems(p[1], p[2])

def p_program_single_item(p):
    '''program_items : program_item'''
    p[0] = sa.SingleProgramItem(p[1])

def p_program_item_const(p):
    '''program_item : const_declaration'''
    p[0] = sa.ConstantDeclaration(p[1])

def p_program_item_function(p):
    '''program_item : function_definition'''
    p[0] = sa.FunctionDeclaration(p[1])

def p_program_const_declaration_rule(p):
    '''const_declaration : CONST ID DECLARE_ASSIGN expression'''
    p[0] = sa.ConstantDeclarationRule(p[2], p[4])

def p_function_definition1(p):
    '''function_definition : signature block_statement'''
    p[0] = sa.FunctionVoid(p[1], p[2])

def p_function_definition2(p):
    '''function_definition : signature ID block_statement  '''
    p[0] = sa.FunctionReturnType(p[1], p[2], p[3])

def p_signature1(p):
    '''signature : FN ID LPAREN sigparams RPAREN   '''
    p[0] = sa.SignatureWithParams(p[2], p[4])

def p_signature2(p):
    '''signature : FN ID LPAREN RPAREN '''
    p[0] = sa.SignatureWithParams(p[2], None)

def p_single_sigparams(p):
    '''sigparams : ID ID'''
    p[0] = sa.SingleSigParam(p[1], p[2])

def p_sequence_sigparams(p):
    '''sigparams : ID ID COMMA sigparams'''
    p[0] = sa.SequenceSigParams(p[1], p[2], p[4])

def p_sequence_params(p):
    '''params : expression COMMA params'''
    p[0] = sa.SequenceParams(p[1], p[3])

def p_single_params(p):
    '''params : expression'''
    p[0] = sa.SingleParams(p[1])

def p_block_statement(p):
    '''block_statement :  LBRACE statements RBRACE'''
    p[0] = sa.BlockStm(p[2])

def p_none_block_statement(p):
    '''block_statement : LBRACE RBRACE'''
    p[0] = sa.BlockStm(None)

def p_sequence_statements(p):
    '''statements : statement statements'''
    p[0] = sa.SequenceStm(p[1], p[2])

def p_single_statement(p):
    '''statements : statement'''
    p[0] = sa.SingleStm(p[1])

def p_statement1(p):
    '''statement :  var_statement '''
    p[0] = sa.VarStm(p[1])

def p_statement2(p):
    '''statement :  var_assignment '''
    p[0] = sa.VarAssign(p[1])

def p_statement3(p):
    '''statement : list_statement '''
    p[0] = sa.ListStm(p[1])

def p_statement4(p):
    '''statement :  list_assignment '''
    p[0] = sa.ListAssign(p[1])

def p_statement5(p):
    '''statement :  func_call '''
    p[0] = sa.FuncCalls(p[1])

def p_statement6(p):
    '''statement :  if_statement '''
    p[0] = sa.IfStm(p[1])

def p_statement7(p):
    '''statement :  for_statement '''
    p[0] = sa.ForStm(p[1])

def p_statement8(p):
    '''statement :  increment_rule '''
    p[0] = sa.IncrementStm(p[1])

def p_statement9(p):
    '''statement : assignment '''
    p[0] = sa.AssignStm(p[1])

def p_statement10(p):
    '''statement : BREAK'''
    p[0] = sa.Break()

def p_statement11(p):
    '''statement :  RETURN expression'''
    p[0] = sa.Return(p[2])

def p_var_declaration1(p):
    '''var_statement : ID DECLARE_ASSIGN expression'''
    p[0] = sa.ImutableDeclaration(p[1], p[3])

def p_var_declaration2(p):
    '''var_statement : MUT ID DECLARE_ASSIGN expression'''
    p[0] = sa.MutableDeclaration(p[1], p[2], p[4])

def p_var_assignment(p):
    '''var_assignment :  ID ASSIGN expression'''
    p[0] = sa.VarModification(p[1], p[3])

def p_list_declaration_imutable(p):
    '''list_statement : ID DECLARE_ASSIGN LBRACKET params RBRACKET'''
    p[0] = sa.DeclarationImutableListRule(p[1],p[4])

def p_list_declaration_mutable(p):
    '''list_statement : MUT ID DECLARE_ASSIGN LBRACKET params RBRACKET'''
    p[0] = sa.DeclarationMutableList(p[1], p[2], p[5])

def p_list_declaration_mutable_list_lenght_definition(p):
    '''list_statement : MUT ID DECLARE_ASSIGN LBRACKET params RBRACKET ID'''
    p[0] = sa.DeclarationMutableListLengthDefinition(p[1], p[2], p[5], p[7])

def p_list_assignment(p):
    '''list_assignment : ID LBRACKET NUMBER RBRACKET ASSIGN expression'''
    p[0] = sa.ListModification(p[1], p[3], p[6])

def p_list_call1(p):
    '''list_call : ID LBRACKET DOTDOT RBRACKET'''
    p[0] = sa.CallListAll(p[1], p[3])

def p_list_call2(p):
    '''list_call : ID LBRACKET NUMBER DOTDOT NUMBER RBRACKET'''
    p[0] = sa.CallListRange(p[1], p[3], p[4], p[5])

# def p_func_call_list_single(p):
#     '''func_call_list : ID LBRACKET NUMBER RBRACKET'''
#     p[0] = sa.FuncCallListSingle(p[1], p[3])

def p_func_call(p):
    '''func_call : ID LPAREN params RPAREN'''
    p[0] = sa.FuncCallWithParams(p[1], p[3])

def p_func_call_empty(p):
    '''func_call : ID LPAREN RPAREN'''
    p[0] = sa.FuncCallWithParams(p[1], None)

def p_if_statement(p):
    '''if_statement : IF expression_relacional block_statement '''
    p[0] = sa.OnlyIf(p[2], p[3])

def p_if_statement_else(p):
    '''if_statement : IF expression_relacional block_statement  elseop'''
    p[0] = sa.IfAndElse(p[2], p[3], p[4])

def p_else(p):
    '''elseop : ELSE if_statement'''
    p[0] = sa.ElseIf(p[2])

def p_else2(p):
    '''elseop : ELSE block_statement '''
    p[0] = sa.OnlyElse(p[2])

def p_for_each_statement(p):
    '''for_statement : FOR ID IN expression block_statement '''
    p[0] = sa.ForEach(p[2], p[4], p[5])

def p_for_statement(p):
    '''for_statement : FOR ID SEMICOLON expression_relacional SEMICOLON increment_rule block_statement '''
    p[0] = sa.ConventionalFor(p[2], p[4], p[6], p[7])

def p_for_statement2(p):
    '''for_statement : FOR expression_relacional block_statement '''
    p[0] = sa.OnlyexpRelFor(p[2], p[3])

def p_expression_plus(p):
    '''expression : expression PLUS term'''
    p[0] = sa.ExpPlus(p[1], p[3])

def p_expression_minus(p):
    '''expression : expression MINUS term'''
    p[0] = sa.ExpMinus(p[1], p[3])

def p_expression_increment(p):
    '''expression :  increment_rule'''
    p[0] = sa.ExpIncrement(p[1])

def p_expression_func_call(p):
    '''expression : func_call'''
    p[0] = sa.ExpFuncCall(p[1])

def p_expression_call_list(p):
    '''expression : list_call'''
    p[0] = sa.ExpCallList(p[1])

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
    p[0] = sa.FactorExp(p[2])

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

def p_factor_size_of_expression_rule(p):
    '''factor : size_of_expression'''
    p[0] = sa.FactorSizeOfExp(p[1])

def p_size_of_expression(p):
    '''size_of_expression : SIZEOF LPAREN expression RPAREN'''
    p[0] = sa.SizeOfExp(p[3])

def p_size_of_type(p):
    '''size_of_expression : SIZEOF LPAREN ID RPAREN'''
    p[0] = sa.SizeOfType(p[3])

def p_increment_plus(p):
    '''increment_rule : ID INCREMENT'''
    p[0] = sa.Inc(p[1])

def p_increment_minus(p):
    '''increment_rule : ID DECREMENT'''
    p[0] = sa.Dec(p[1])

def p_expression_relacional_equals(p):
    '''expression_relacional : expression EQ expression'''
    p[0] = sa.ExpRelEqual(p[1], p[3])

def p_expression_relacional_not_equals(p):
    '''expression_relacional : expression NEQ expression'''
    p[0] = sa.ExpRelNotEqual(p[1], p[3])

def p_expression_relacional_less_than(p):
    '''expression_relacional : expression LT expression'''
    p[0] = sa.ExpRelLessThan(p[1], p[3])

def p_expression_relacional_less_than_or_equal(p):
    '''expression_relacional : expression LE expression'''
    p[0] = sa.ExpRelLessThanOrEqual(p[1], p[3])

def p_expression_relacional_greater_than(p):
    '''expression_relacional : expression GT expression'''
    p[0] = sa.ExpRelGreaterThan(p[1], p[3])

def p_expression_relacional_greater_than_or_equal(p):
    '''expression_relacional : expression GE expression'''
    p[0] = sa.ExpRelGreaterThanOrEqual(p[1], p[3])

def p_expression_relacional_and(p):
    '''expression_relacional : expression AND expression'''
    p[0] = sa.ExpRelAnd(p[1], p[3])

def p_expression_relacional_or(p):
    '''expression_relacional : expression OR expression'''
    p[0] = sa.ExpRelOr(p[1], p[3])    

def p_expression_relacional_not(p):
    '''expression_relacional : NOT expression'''
    p[0] = sa.ExpRelNot(p[2])

def p_assignment_plus_equals(p):
    '''assignment : ID PLUS_ASSIGN expression'''
    p[0] = sa.AssignPlusEquals(p[1], p[3])

def p_assignment_minus_equal(p):
    '''assignment : ID MINUS_ASSIGN expression'''
    p[0] = sa.AssignMinusEquals(p[1], p[3])

def p_assignment_multiply_equals(p):
    '''assignment : ID TIMES_ASSIGN expression'''
    p[0] = sa.AssignMultiplicationEquals(p[1], p[3])

def p_assignment_divide_equals(p):
    '''assignment : ID DIVIDE_ASSIGN expression'''
    p[0] = sa.AssignDivideEquals(p[1], p[3])

def p_assignment_mod_equals(p):
    '''assignment : ID MOD_ASSIGN expression'''
    p[0] = sa.AssignModEquals(p[1], p[3])

def p_assignment_and_equals(p):
    '''assignment : ID BIT_AND_ASSIGN expression'''
    p[0] = sa.AssignAndEquals(p[1], p[3])

def p_assignment_or_equals(p):
    '''assignment : ID BIT_OR_ASSIGN expression'''
    p[0] = sa.AssignOrEquals(p[1], p[3])

def p_assignment_exp_equals(p):
    '''assignment : ID BIT_XOR_ASSIGN expression'''
    p[0] = sa.AssignXOREquals(p[1], p[3])

def p_assignment_lshift(p):
    '''assignment : ID BIT_LSHIFT_ASSIGN expression'''
    p[0] = sa.AssignDeslocationLeft(p[1], p[3])

def p_assignment_rshift(p):
    '''assignment : ID BIT_RSHIFT_ASSIGN expression'''
    p[0] = sa.AssignDeslocationRight(p[1], p[3])


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