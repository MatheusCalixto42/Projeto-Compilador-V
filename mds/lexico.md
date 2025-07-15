# **Linguagem V(Vlang) - Elementos Léxicos**

## **Sobre o documento**
Este documento detalha os elementos léxicos da linguagem de programação V. V é uma linguagem de programação compilada e estaticamente tipada, projetada para a construção de software sustentável.
É semelhante ao Go e seu design também foi influenciado por Oberon, Rust, Swift, Kotlin e Python.

---

## **1. Palavras Reservadas**

V apresenta apenas as seguintes palavras reservas ou palavras-chave:

### **1.1. Literais**

* `true`: Representa o valor booleano verdadeiro.
* `false`: Representa o valor booleano falso.
* `none`: Indica a ausência de valor, semelhante a `null` em outras linguagens.

### **1.2. Controle de Fluxo**

* `if`: Inicia uma estrutura condicional.
* `else`: Define o bloco a ser executado caso a condição do `if` seja falsa.
* `for`: Inicia um loop; V utiliza `for` para todas as estruturas de repetição.
* `match`: Estrutura de controle semelhante ao `switch` em outras linguagens.
* `break`: Interrompe a execução de loops ou estruturas de controle.
* `continue`: Pula para a próxima iteração de um loop.
* `return`: Retorna um valor de uma função.
* `or`: Utilizado para tratamento de erros, especificando um bloco a ser executado em caso de erro.

### **1.3. Definição e Organização**

* `fn`: Declara uma função.
* `import`: Importa módulos externos.
* `const`: Declara constantes.
* `type`: Define um novo tipo.
* `enum`: Declara um conjunto enumerado de constantes.
* `union`: Define uma união de tipos.

### **1.4. Modificadores**

* `mut`: Indica que uma variável ou argumento é mutável.
* `unsafe`: Marca um bloco de código como inseguro, permitindo operações de baixo nível.

### **1.5. Outros**

* `as`: Utilizado para renomear importações ou realizar castings.
* `is`: Verifica se uma variável é de um determinado tipo.
* `in`: Verifica se um valor está contido em uma coleção.
* `isreftype`: Verifica se um tipo é uma referência.
* `sizeof`: Retorna o tamanho em bytes de um tipo ou variável.
* `typeof`: Retorna o tipo de uma variável.
* `__global`: Declara uma variável global; requer a flag `-enable-globals` para uso.
* `assert`: Verifica se uma condição é verdadeira; caso contrário, interrompe a execução.


---

## **2. Operadores**

### **2.1 Operadores Aritméticos**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `+` | Adição | 4 | ➡️ |
| `-` | Subtração | 4 | ➡️ |
| `*` | Multiplicação | 5 | ➡️ |
| `/` | Divisão | 5 | ➡️ |
| `%` | Módulo (resto da divisão) | 5 | ➡️ |

### **2.2. Operadores de Atribuição**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `=` | Atribuição simples | - | - |
| `:=` | Declaração de variáveis com inferência de tipo e atribuição | - | - | 
| `+=` | Adição e atribuição | - | - |
| `-=` | Subtração e atribuição | - | - |
| `*=` | Multiplicação e atribuição | - | - |
| `/=` | Divisão e atribuição | - | - |
| `%=` | Módulo e atribuição | - | - |
| `&=` | E bit a bit e atribuição | - | - |
| `\|=` | OU bit a bit e atribuição | - | - |
| `^=` | XOR bit a bit e atribuição | - | - |
| `<<=` | Deslocamento à esquerda e atribuição | - | - |
| `>>=` | Deslocamento à direita e atribuição | - | - |

### **2.3. Operadores de Comparação**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `==` | Igual a | 3 | ➡️ | 
| `!=` | Diferente de | 3 | ➡️ |
| `<` | Menor que | 3 | ➡️ |
| `<=` | Menor ou igual a | 3 | ➡️ |
| `>` | Maior que | 3 | ➡️ |
| `>=` | Maior ou igual a | 3 | ➡️ |

### **2.4. Operadores Lógicos**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `&&` | E lógico | 2 | ➡️ |
| `\|\|` | OU lógico | 1 | ➡️ |
| `!` | NÃO lógico | 5 | ⬅️ |

### **2.5. Operadores Bit a Bit (Bitwise)**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `&` | E (AND) | 5 | ➡️ |
| `\|` | OU (OR) | 4 | ➡️ |
| `^` | OU Exclusivo (XOR) | 4 | ➡️ |
| `<<` | Deslocamento à esquerda | 5 | ➡️ |
| `>>` | Deslocamento à direita | 5 | ➡️ |

### **2.6. Operadores Unários de Atualização**
| Operador | Descrição | Precedência | Associatividade |
| :---: | --- | --- | --- |
| `++` | Soma 1 ao valor da variável | - | - |
| `--` | Subtrai 1 ao valor da variável | - | - |

---

## **3. Separadores ou Delimitadores**
A linguagem Vlang não possui delimitador para linhas, isto é, não é como em C, por exemplo, que necessita do `';'` para o compilador entender que o comando encerrou. Vlang delimita parâmetros de funções ao utilizar a `','` entre os parâmetros. Vlang também pode separar expressões para dar prioridade com o uso de `()`. Por fim, nessa linguagem, os blocos de comando são delimitados por `\`

- **Parênteses `()`**: Usados em chamadas de função, agrupamento de expressões e definições de tipo de função.
- **Chaves `{}`**: Usadas para delimitar blocos de código (corpo de funções, laços, condicionais) e para a inicialização de literais de struct, array e mapa.
- **Colchetes `[]`**: Usados para acessar elementos de arrays e mapas, e para definir tipos de array.
- **Vírgula `,`**: Usada para separar elementos em listas (argumentos de função, elementos de array, etc.).
- **Ponto e vírgula `;`**: Geralmente opcional em V, pois o compilador insere-os automaticamente no final das linhas. Seu uso explícito é raro.
- **Dois pontos `:`**: Usado em conjunto com `=` na declaração curta de variáveis (`:=`).

---

## **4. Identificadores**
Identificadores são os nomes dados a entidades como variáveis, constantes, funções, tipos e módulos.

- **Regras de Nomenclatura**:
  - Devem começar com uma letra (`a-z`).
  - Identificadores que começam com letra maiúscula são usados para tipos exportados (como Pessoa, Usuario, etc.).
  - Após o primeiro caractere, podem conter letras, números (`0-9`) e sublinhados.
  - Não podem conter espaços nem símbolos como `@`, `#`, `%`, `-`, etc.
  - Palavras-chave (reservadas) não podem ser usadas como identificadores.
  - V é **case-sensitive**, o que significa que `minhaVariavel` e `minhavariavel` são identificadores distintos.

- **Convenções**:
  - **`snake_case`**: Usado para variáveis e funções (`nome_usuario`, `calculartotal`).
  - **`PascalCase`** (ou **`CapitalCase`**): Usado para tipos, como structs, enums e interfaces (`Usuario`, `OpcoesDePagamento`).

- **Exemplos de Identificadores Válidos**:
  - `idade`
  - `soma1`
  - `nomeDeUsuario`
  - `Ponto`

---

## **5. Números**

Vlang dá suporte a números inteiros e a números com ponto flutuantes. Além disso, nessa
linguagem não só os números podem também ser representados nas notações de hexadecimal,
octal ou binária para números inteiros, como também suporta números com _ para separar as
casas, por exemplo o número inteiro mil pode ser escrito da forma 1000 ou 1 _000. Por fim, vale
ressaltar que a linguagem dá suporte à números com sinais e sem sinais (unsigned), sejam eles
inteiros de 8 bits até 64 bits, floats de 32 bits até 64 bits.

### **5.1. Números Inteiros**
Representam números inteiros e podem ser especificados em diferentes bases.

- **Decimal**: `123`, `42`, `1000`
- **Hexadecimal** (prefixo `0x`): `0xFF`, `0x1A`
- **Binário** (prefixo `0b`): `0b1010`, `0b1101`
- **Octal** (prefixo `0o`): `0o77`, `0o12`

### **5.2. Números de Ponto Flutuante**
Representam números com casas decimais.

- **Padrão**: `3.14`, `0.5`, `100.0`
- **Notação Científica**: `6.022e23`, `1.5E-10`

---

## **6. Literais de Rune**
Representam um único caractere Unicode e são delimitados por crase (`` ` ``).

- **Exemplos**: `'a'`, `'B'`, `'$'`, `'\n'` (caractere de nova linha)

---

## **7. String**
Representam sequências de caracteres.

- **Strings Comuns**: Delimitadas por aspas simples (`''`) e por aspas duplas(`""`). Sequências de escape (como `\n`, `\t`, `\"`) são interpretadas.

  ```
  minha_string := 'Olá, mundo!\nIsto está em uma nova linha.'
  ```
  ```
  minha_string := "Olá, mundo!\nIsto está em uma nova linha."
  ```
  
---

 ## **8. Erros**
 Na linguagem V, qualquer sequência de caracteres que não corresponda a um dos elementos léxicos válidos, como identificadores, literais, operadores ou palavras-chave, é considerada um erro léxico. Isso inclui, por exemplo, o uso de símbolos não reconhecidos, identificadores iniciando com números ou o uso de palavras que não pertencem à linguagem.
Durante a análise léxica, espaços em branco, tabulações e quebras de linha são ignorados para fins de reconhecimento de tokens. Eles não afetam a interpretação dos elementos do código, exceto quando são essenciais para separar tokens ou evitar ambiguidade. Por exemplo, a:=10 e a := 10 são equivalentes, mas a ausência completa de espaço entre dois identificadores distintos poderia causar erro.
Embora espaços e quebras de linha não alterem o significado léxico, o compilador da linguagem V utiliza essas quebras de linha para rastrear a posição do código, permitindo que mensagens de erro sejam emitidas com precisão, indicando a linha e a coluna onde ocorreu o problema. Assim, mesmo que ignoradas na análise dos símbolos, essas informações são essenciais para diagnóstico e depuração durante a compilação.

