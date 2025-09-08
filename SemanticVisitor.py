from Visitor import *
import SymbolTable as st

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT32 or type2 == st.FLOAT32):
            return st.FLOAT32
        elif (type1 == st.FLOAT64 or type2 == st.FLOAT64):
            return st.FLOAT64
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        self.n_errors = 0
        self.main_defined = False
        st.beginScope('global')

###################################################################
# Classes to visit the Abstract Syntax of Program
##################################################################

    def visitCompoundImportItems(self,compoundImportItems):
        if(compoundImportItems.program_import != None):          #esses ifs sao necessarios? ja q a gente tem uma classe para caso n ter program_import
            compoundImportItems.program_import.accept(self)
        if(compoundImportItems.program_items != None):
            compoundImportItems.program_items.accept(self)

    def visitProgramItems(self,programItems):
        programItems.program_items.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Import
################################################################## 

    def visitSequenceImports(self,sequenceImports):  #so ignora os imports mesmo?
        bindable = st.getBindable(sequenceImports.id)
        if bindable is None:
            st.addImport(sequenceImports.id)
        elif bindable[st.NAMEIMPORT] != sequenceImports.id:
            st.addImport(sequenceImports.id)
        else:
            self.n_errors += 1
            print('\n\t[Erro]', sequenceImports.id, 'já foi importado')
       
        if(sequenceImports.program_import.accept != None):
           sequenceImports.program_import.accept(self)

    def visitSingleImport(self,singleImport):
        bindable = st.getBindable(singleImport.id)
        if bindable is None:
            st.addImport(singleImport.id)
        elif bindable[st.NAMEIMPORT] != singleImport.id:
            st.addImport(singleImport.id)
        else:
            self.n_errors += 1
            print('\n\t[Erro]', singleImport.id, 'já foi importado')
        
###################################################################
# Classes to visit the Abstract Syntax of Program Items
################################################################## 

    def visitSequenceProgramItems(self,sequenceProgramItems):
        if(sequenceProgramItems.program_item.accept != None):
            sequenceProgramItems.program_item.accept(self)
        if(sequenceProgramItems.program_items.accept != None):
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

        constantDeclarationRule.exp.accept(self.printer)

        bindable = st.getBindable(constantDeclarationRule.id)
        typeConst = constantDeclarationRule.exp.accept(self)
        if bindable is not None:
            self.n_errors += 1
            print(f"\n\t[Erro] Constante '{constantDeclarationRule.id}' já declarada")
            return None
        st.addConstVar(constantDeclarationRule.id, typeConst)
        return typeConst
    

###################################################################
# Classes to visit the Abstract Syntax of Function Definition
##################################################################

    def visitFunctionVoid(self,functionVoid):
        functionVoid.signature.accept(self)
        functionVoid.blockStm.accept(self)
        

    def visitFunctionReturnType(self,functionReturnType):
        nomeFunc = functionReturnType.signature.accept(self)

        typeFunc = functionReturnType.id

        if(typeFunc in st.type):
             st.updateBindableAttr(nomeFunc, st.TYPE, typeFunc)
        else:
            self.n_errors += 1
            print('\n\t[ERROR] Funcao com tipo inválido: ', typeFunc)

        functionReturnType.blockStm.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Signature
##################################################################
    
    def visitSignatureWithParams(self, signatureWithParams):

        params = {}

        bindable = st.getBindable(signatureWithParams.id)
        
        if(signatureWithParams.id == 'main' and not self.main_defined):
            self.main_defined = True
            st.addFunction(signatureWithParams.id, params, st.VOID)
        elif(signatureWithParams.id == 'main' and self.main_defined):
            self.n_errors += 1
            print('\n\t[ERROR] Funcao main já definida')
        elif(bindable != None):
            self.n_errors += 1
            print('\n\t[ERROR] Funcao', bindable[st.NAMEFUNCTION],'já definida')
        else:
            if (signatureWithParams.sigParams != None):
                params = signatureWithParams.sigParams.accept(self)
                st.addFunction(signatureWithParams.id, params, None)
                
            else:
                st.addFunction(signatureWithParams.id, params, st.VOID)
            
        st.beginScope(signatureWithParams.id)
        for k in range(0, len(params), 2):
            st.addMutableVar(params[k], params[k+1])

        bindable = st.getBindable(signatureWithParams.id)
        if(bindable[st.TYPE] == None):
            return signatureWithParams.id

###################################################################
# Classes to visit the Abstract Syntax of Sigparams
##################################################################

    def visitSingleSigParam(self, singleSigParam):

        return [singleSigParam.id, singleSigParam.idType]

    def visitSequenceSigParams(self, sequenceSigParams):
        sequenceSigParams.sigParams.accept(self)
        
        return [sequenceSigParams.id, sequenceSigParams.idType] + sequenceSigParams.sigParams.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Params
##################################################################
    
    def visitSequenceParams(self,sequenceParams):
        return [sequenceParams.exp.accept(self)] + sequenceParams.params.accept(self)

    def visitSingleParams(self, singleParams):
        return [singleParams.exp.accept(self)]


###################################################################
# Classes to visit the Abstract Syntax of BlockStatement
##################################################################     

    def visitBlockStm(self, blockStm):
        if(blockStm.stms != None):
            blockStm.stms.accept(self)
       
       

###################################################################
# Classes to visit the Abstract Syntax of Stms
##################################################################

    def visitSequenceStm(self, sequenceStm):
        sequenceStm.stm.accept(self)
        sequenceStm.stms.accept(self)

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Stm
##################################################################

    def visitVarStm(self,varStm):#var_statemnt
        varStm.var_stm.accept(self)
       
    
    def visitVarAssign(self,varAssign):
        varAssign.var_assign.accept(self)
        
   
    def visitListStm(self, listStm):
        listStm.list_stm.accept(self)
        
        
    def visitListAssign(self, listAssign):
        listAssign.list_assign.accept(self)
       

    def visitFuncCalls(self,funcCalls):
        funcCalls.func_call.accept(self)
       
         
    def visitIfStm(self,ifStm):
        ifStm.if_stm.accept(self)

    def visitForStm(self,forStm):
        forStm.for_stm.accept(self)

    def visitBreakStm(self, breakStm):
        print(blank(), 'break', end=' ')

    def visitReturnStm(self,returnStm):
    
        if(returnStm.exp == None):
            pass

        returnStm.exp.accept(self)

    def visitIncrementStm(self, incrementStm):
        incrementStm.increment_stm.accept(self)
        

    def visitAssignStm(self, assignStm):
        assignStm.assign_stm.accept(self)
      


 ###################################################################
# Classes to visit the Abstract Syntax of Var Statement
##################################################################   

    def visitImutableDeclaration(self,imutableDeclaration):
        idName = imutableDeclaration.id
        bindable = st.getBindable(idName)
        typeVar = imutableDeclaration.exp.accept(self)

        if(bindable != None):
            st.addImutableVar(idName,typeVar)
        else:
            self.n_errors += 1
            print(f"\n\t[Erro] Variável '{idName}' já declarada")
            
    def visitMutableDeclaration(self,mutableDeclaration):
        idName = mutableDeclaration.id
        bindable = st.getBindable(idName)
        typeVar = mutableDeclaration.exp.accept(self)

        if(bindable != None):
            st.addMutableVar(idName,typeVar)
        else:
            self.n_errors += 1
            print(f"\n\t[Erro] Variável '{idName}' já declarada")
    

###################################################################
# Classes to visit the Abstract Syntax of Var Assignment
##################################################################

    def visitVarModification(self,varModification):
       idName = varModification.id
       bindable = st.getBindable(idName)
       typeVar = varModification.exp.accept(self)   
       if(bindable == None):
            self.n_errors += 1
            print('\t\n[Erro] Variável', idName, 'não declarada')
       if(bindable[st.BINDABLE] == st.IMUTABLEVAR):
            self.n_errors += 1
            print('\t\n[Erro] Variável', idName, 'imutável')
       if(bindable[st.TYPE] != typeVar):
            self.n_errors += 1
            print('\t\n[Erro] Atribuição inválida. A variável', idName, 'é do tipo', bindable[st.TYPE], 'enquanto a expressão é do tipo', typeVar)
           

###################################################################
# Classes to visit the Abstract Syntax of List Statement
##################################################################

    def visitDeclarationImutableListRule(self, declarationImutableListRule):
        idName = declarationImutableListRule.id
        bindable = st.getBindable(idName)
        params = {}
        typeArray = None

        if(declarationImutableListRule.params != None):
            params = declarationImutableListRule.params.accept(self)
            typeArray = params[0]
        
        if params:
            for type in params:
                if type != typeArray:
                    self.n_errors += 1
                    print(f"\n\t[Erro] Lista '{declarationImutableListRule.id}' possui elementos de tipos diferentes: '{typeArray}' e '{type}'")
                    break 

        if(bindable != None):
            self.n_errors += 1
            print(f"\n\t[Erro] Lista '{idName}' já declarada")
        
        st.addArrayImutable(idName, len(params), typeArray)

    def visitDeclarationMutableList(self, declarationMutableList):
        idName = declarationMutableList.id
        bindable = st.getBindable(idName)
        params = {}
        typeArray = None

        if(declarationMutableList.params != None):
            params = declarationMutableList.params.accept(self)
            typeArray = params[0]
        
        if params:
            for type in params:
                if type != typeArray:
                    self.n_errors += 1
                    print(f"\n\t[Erro] Lista '{declarationMutableList.id}' possui elementos de tipos diferentes: '{typeArray}' e '{type}'")
                    break 

        if(bindable != None):
            self.n_errors += 1
            if(bindable != None):
                print(f"\n\t[Erro] Lista '{idName}' já declarada")
            if(typeArray == None and len(params) != 0):
                print(f"\n\t[Erro] Lista '{idName}' declarada com elementos inválidos")
    
        st.addArrayMutable(idName, len(params), typeArray)

    def visitDeclarationMutableListLengthDefinition(self, listLengthDefinition):
        idName = listLengthDefinition.id
        number = listLengthDefinition.number
        bindable = st.getBindable(idName)
        typeArray = listLengthDefinition.type

        if(bindable != None):
            self.n_errors += 1
            print(f"\n\t[Erro] Lista '{idName}' já declarada")
            
        if(not (typeArray in st.type)):
            self.n_errors += 1
            print('\n\t[ERROR] Lista com tipo inválido: ', typeArray)
        
        st.addArrayMutable(idName, number, typeArray)
        

###################################################################
# Classes to visit the Abstract Syntax of List Assigment
##################################################################

    def visitListModification(self, listModification):
        idName = listModification.id
        bindable = st.getBindable(idName)
        typeVar = listModification.exp.accept(self)   
        if(bindable == None):
            self.n_errors += 1
            print('\t\n[Erro] Lista', idName, 'não declarada')
        if(bindable[st.BINDABLE] == st.IMUTABLEVAR):
            self.n_errors += 1
            print('\t\n[Erro] Lista', idName, 'imutável')
        if(0 < listModification.number and listModification.number > bindable[st.LENGTH]):
            self.n_errors += 1
            print('\t\n[Erro] Indice fora do tamanho da lista. tamanho da lista: ', bindable[st.LENGTH])
        if(bindable[st.TYPE] != typeVar):
            self.n_errors += 1
            print('\t\n[Erro] Atribuição inválida. A Lista', idName, 'é do tipo', bindable[st.TYPE], 'enquanto a expressão é do tipo', typeVar)
            

###################################################################
# Classes to visit the Abstract Syntax of Func Call List
##################################################################

    def visitCallListAll(self, callListAll):
        bindable = st.getBindable(callListAll.id)
        if(bindable != None):
            self.n_errors += 1
            print('\t\n[Erro] Lista', callListAll.id, 'não declarada')

    def visitCallListRange(self, callRange):
        bindable = st.getBindable(callRange.id)
        
        if(bindable == None):
            self.n_errors += 1
            print('\t\n[Erro] Lista', callRange.id, 'não declarada')
        if(0 < callRange.number and callRange.number2 > bindable[st.LENGTH]):
            self.n_errors += 1
            print('\t\n[Erro] Indice fora do tamanho da lista. tamanho da lista: ', bindable[st.LENGTH])
            

    # def visitFuncCallListSingle(self, funcCallSingle):
    #     print(blank(), funcCallSingle.id, end=' ')
    #     print('[', end=' ')
    #     print(funcCallSingle.number, end=' ')
    #     print(']', end=' ')

###################################################################
# Classes to visit the Abstract Syntax of Func Call
##################################################################

    def visitFuncCallWithParams(self,funcCallWithParams):

        paramsCall = {}

        if(funcCallWithParams.params != None):
            paramsCall = funcCallWithParams.params.accept(self)
        
        paramsFunc = {}

        bindable = st.getBindable(funcCallWithParams.id)

        if(bindable == None):
            self.n_errors += 1
            print('\t\n[Erro] Função', funcCallWithParams.id, 'não declarada')
        else:
            paramsFunc = bindable[st.PARAMS]

            if(len(paramsFunc)//2 != len(paramsCall)):
                self.n_errors += 1
                print('\t\n[Erro] A função', funcCallWithParams.id, 'espera', int(len(paramsFunc)/2), 'parâmetros, mas foram passados', int(len(paramsCall)))
            else:
                for i in range(len(paramsCall)):
                    if paramsFunc[i*2+1] != paramsCall[i]:
                        self.n_errors += 1
                        print('\t\n[Erro] Parâmetro', i+1, 'da função', funcCallWithParams.id, 'espera o tipo', paramsFunc[i*2+1], 'mas foi passado o tipo', paramsCall[i])
        
    

###################################################################
# Classes to visit the Abstract Syntax of If Statement
##################################################################

    def visitOnlyIf(self,onlyIf):

        typeExp = onlyIf.expRels.accept(self)
        
        st.beginScope('if') #Duvida se ta certo
        onlyIf.blockStm.accept(self)
        st.endScope()

    def visitIfAndElse(self,ifAndElse):

        typeExp = ifAndElse.expRels.accept(self)

        st.beginScope('if')
        
        ifAndElse.blockStm.accept(self)
        ifAndElse.elseV.accept(self)


###################################################################
# Classes to visit the Abstract Syntax of Else
##################################################################

    def visitElseIf(self,elseIf):
       
        elseIf.if_stm.accept(self)
        st.endScope() #isso aqui ta certo?

    def visitOnlyElse(self,onlyElse):
       
        onlyElse.blockstm.accept(self)
        st.endScope()

###################################################################
# Classes to visit the Abstract Syntax of For
##################################################################

    def visitForEach(self,forEach):
    
        forEach.exp.accept(self)
        forEach.blockStm.accept(self)
    

    def visitConventionalFor(self,conventionalFor):
      
        conventionalFor.expRels.accept(self)
        
        conventionalFor.increment.accept(self)
        conventionalFor.blockStm.accept(self)

    def visitOnlyexpRelFor(self,onlyexpRelFor):
     
        onlyexpRelFor.expRels.accept(self)
        onlyexpRelFor.blockStm.accept(self)

        
###################################################################
# Classes to visit the Abstract Syntax of Expression
##################################################################

    def visitSequenceExpRels(self, sequenceExpRels):
        sequenceExpRels.expRels.accept(self)
        sequenceExpRels.expRel.accept(self)

    def visitSingleExpRel(self,singleExpRel):
        singleExpRel.expRel.accept(self)

    def visitExpPlus(self,expPlus):
        expPlus.exp.accept(self.printer)
        expPlus.term.accept(self.printer)

        tipo1 = expPlus.exp.accept(self)
        tipo2 = expPlus.term.accept(self)
        tipo = coercion(tipo1, tipo2)

        if(tipo == None):
            expPlus.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            expPlus.exp.accept(self.printer)
            print(' eh do tipo', tipo1, 'enquanto a expressao ', end='')
            expPlus.term.accept(self.printer)
            print(' eh do tipo', tipo2,'\n')
        return tipo


    def visitExpMinus(self,expMinus):
        expMinus.exp.accept(self.printer)
       
        expMinus.term.accept(self.printer)

        tipo1 = expMinus.exp.accept(self)
        tipo2 = expMinus.term.accept(self)
        tipo = coercion(tipo1, tipo2)

        if(tipo == None):
            expMinus.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Subtração invalida. A expressao ', end='')
            expMinus.exp.accept(self.printer)
            print(' eh do tipo', tipo1, 'enquanto a expressao ', end='')
            expMinus.term.accept(self.printer)
            print(' eh do tipo', tipo2,'\n')
        return tipo

    def visitSingleTerm(self,singleTerm):
        return singleTerm.term.accept(self)

    def visitExpIncrement(self, expIncrement):
      
        expIncrement.increment.accept(self)
        

    def visitExpFuncCall(self, expFuncCall):
        expFuncCall.funcCall.accept(self)

    def visitExpCallList(self, expCallList):
        expCallList.calllist.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Relational Expression
##################################################################

    def visitExpRelEqual(self,expRelEqual):
        typeVar1 = expRelEqual.exp1.accept(self)
        typeVar2 = expRelEqual.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL

    def visitExpRelNotEqual(self,expRelNotEqual):
        typeVar1 = expRelNotEqual.exp1.accept(self)
        typeVar2 = expRelNotEqual.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL

    def visitExpRelLessThan(self,expRelLessThan):
        typeVar1 = expRelLessThan.exp1.accept(self)
        typeVar2 = expRelLessThan.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL 

    def visitExpRelGreaterThan(self,expRelGreaterThan):
        typeVar1 = expRelGreaterThan.exp1.accept(self)
        typeVar2 = expRelGreaterThan.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL 
    
    def visitExpRelLessThanOrEqual(self,expRelationalLessThanOrEqual):
        typeVar1 = expRelationalLessThanOrEqual.exp1.accept(self)
        typeVar2 = expRelationalLessThanOrEqual.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional de igualdade deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL

    def visitExpRelGreaterThanOrEqual(self,expRelGreaterThanOrEqual):
        typeVar1 = expRelGreaterThanOrEqual.exp1.accept(self)
        typeVar2 = expRelGreaterThanOrEqual.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL 

    def visitExpRelAnd(self,expressionRelationalAnd):
        typeVar1 = expressionRelationalAnd.exp1.accept(self)
        typeVar2 = expressionRelationalAnd.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL 

    def visitExpRelOr(self,expressionRelationalOr):
        typeVar1 = expressionRelationalOr.exp1.accept(self)
        typeVar2 = expressionRelationalOr.exp2.accept(self)
        if(typeVar1 != typeVar2):
            self.n_errors += 1
            print('\n\t[Erro] A expressão relacional deve ser entre expressões do mesmo tipo, e são do tipo', typeVar1, 'e', typeVar2)
        else:
            return st.BOOL

    def visitExpRelNot(self,expressionRelationalNot):
        return st.BOOL

###################################################################
# Classes to visit the Abstract Syntax of Term
##################################################################

    def visitMultiplication(self,multiplication):
        multiplication.term.accept(self.printer)
        
        multiplication.factor.accept(self.printer)

        tipo1 = multiplication.exp.accept(self)
        tipo2 = multiplication.term.accept(self)
        tipo = coercion(tipo1, tipo2)

        if(tipo == None):
            multiplication.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Multiplicação invalida. A expressao ', end='')
            multiplication.exp.accept(self.printer)
            print(' eh do tipo', tipo1, 'enquanto a expressao ', end='')
            multiplication.term.accept(self.printer)
            print(' eh do tipo', tipo2,'\n')
        return tipo

    def visitDivision(self,division):
        division.term.accept(self.printer)
        
        division.factor.accept(self.printer)

        tipo1 = division.exp.accept(self)
        tipo2 = division.term.accept(self)
        tipo = coercion(tipo1, tipo2)

        if(tipo == None):
            division.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Divisão invalida. A expressao ', end='')
            division.exp.accept(self.printer)
            print(' eh do tipo', tipo1, 'enquanto a expressao ', end='')
            division.term.accept(self.printer)
            print(' eh do tipo', tipo2,'\n')
        return tipo
    
    def visitMod(self,mod):
        mod.term.accept(self.printer)
        
        mod.factor.accept(self.printer)

        tipo1 = mod.exp.accept(self)
        tipo2 = mod.term.accept(self)
        tipo = coercion(tipo1, tipo2)

        if(tipo == None):
            mod.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Módulo invalido. A expressao ', end='')
            mod.exp.accept(self.printer)
            print(' eh do tipo', tipo1, 'enquanto a expressao ', end='')
            mod.term.accept(self.printer)
            print(' eh do tipo', tipo2,'\n')
        return tipo
    
    def visitOnlyFactor(self,onlyFactor):
        return onlyFactor.factor.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Factor
##################################################################
    def visitFactorNumber(self,factorNumber):
        if(isinstance(factorNumber.number, int)):
            return st.INT

    def visitFactorString(self,factorString):
        return st.STRING

    def visitFactorID(self,factorID):
        idName = factorID.id
        bindable = st.getBindable(idName)
        if(bindable != None):
            return bindable[st.TYPE]
        return None

    def visitFactorExp(self,factorExp):
        
        factorExp.exp.accept(self.printer)
        

        return factorExp.exp.accept(self)

    def visitFactorList(self, factorList):
      

        idName = factorList.id
        bindable = st.getBindable(idName)
        if(bindable != None):
            return bindable[st.TYPE]
        return None

    def visitFactorTrue(self,factorTrue):
        return st.BOOL
    
    def visitFactorFalse(self,factorFalse):
        return st.BOOL

    def visitFactorRune(self,factorRune):
        return st.RUNETYPE

    def visitFactorNumberFloat(self, factorNumberFloat):
        if(isinstance(factorNumberFloat.numberfloat, float)):
            return st.FLOAT64
        else:
            return st.FLOAT32

    def visitFactorCientificNotation(self, cientific_notation):
        if(isinstance(cientific_notation.cientificNotation, float)):
            return st.FLOAT64
        else:
            return st.FLOAT32

    def visitFactorBinary(self, binary):
        if(isinstance(binary.factorBinary, float)):
            return st.FLOAT64
        else:
            return st.FLOAT32

    def visitFactorOctal(self, octal):
        if(isinstance(octal.factorOctal, float)):
            return st.FLOAT64
        else:
            return st.FLOAT32

    def visitFactorHex(self, hex):
        if(isinstance(hex.factorHex, float)):
            return st.FLOAT64
        else:
            return st.FLOAT32

    def visitFactorSizeOfExp(self, factorSizeofExp):
        factorSizeofExp.sizeofexp.accept(self)

###################################################################
# Classes to visit the Abstract Syntax of Size of Expression
##################################################################

    def visitSizeOfExp(self, sizeOfExp):

        sizeOfExp.exp.accept(self)


    def visitSizeOfType(self, sizeOfType):
    
        print(sizeOfType.idType, end=' ')
 

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
     
        assignPlusEquals.exp.accept(self)

    def visitAssignMinusEquals(self, assignMinusEquals):
       
        assignMinusEquals.exp.accept(self)

    def visitAssignMultiplicationEquals(self, assignMultiplicationEquals):
       
        assignMultiplicationEquals.exp.accept(self)

    def visitDivideEquals(self, DivideEquals):
       
        DivideEquals.exp.accept(self)

    def visitAssignModEquals(self, assignModEquals):
    
        assignModEquals.exp.accept(self)

    def visitAssignAndEquals(self, assignAndEquals):
       
        assignAndEquals.exp.accept(self)

    def visitAssignOrEquals(self, assignOrEquals):
       
        assignOrEquals.exp.accept(self)

    def visitAssignXOREquals(self, assignXOREquals):
        
        assignXOREquals.exp.accept(self)

    def visitAssignDeslocationLeft(self, assignDeslocationLeft):
        
        assignDeslocationLeft.exp.accept(self)

    def visitAssignDeslocationRight(self, assignDeslocationRight):
        
        assignDeslocationRight.exp.accept(self)


def main():
    f = open("testeSemanticoV.v", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)
    print("#imprime erros semanticos encontrados")
    svisitor = SemanticVisitor()
    result.accept(svisitor)
    print(f"Foram encontrados {svisitor.n_errors} erros")
    #visitorPrettyPrinters = Visitor()
    #result.accept(visitorPrettyPrinters)

if __name__ == "__main__":
    main()