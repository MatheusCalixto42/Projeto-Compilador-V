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
* `goto`: Permite saltar para um rótulo específico no código (uso desencorajado).
* `select`: Utilizado para operações concorrentes, semelhante ao `select` em Go.

### **1.3. Definição e Organização**

* `fn`: Declara uma função.
* `module`: Define o módulo atual do arquivo.
* `import`: Importa módulos externos.
* `const`: Declara constantes.
* `type`: Define um novo tipo.
* `struct`: Define uma estrutura de dados.
* `enum`: Declara um conjunto enumerado de constantes.
* `union`: Define uma união de tipos.
* `interface`: Declara uma interface, especificando métodos que um tipo deve implementar.
* `implements`: Indica que um tipo implementa uma interface.

### **1.4. Modificadores**

* `pub`: Torna funções, métodos ou variáveis públicas, acessíveis fora do módulo.
* `mut`: Indica que uma variável ou argumento é mutável.
* `shared`: Declara uma variável compartilhada entre threads.
* `rlock`: Adquire um bloqueio de leitura em uma variável compartilhada.
* `lock`: Adquire um bloqueio de escrita em uma variável compartilhada.
* `atomic`: Indica que uma operação é atômica, utilizada em contextos concorrentes.
* `unsafe`: Marca um bloco de código como inseguro, permitindo operações de baixo nível.
* `volatile`: Indica que uma variável pode ser modificada fora do controle do programa, como por hardware.

### **1.5. Outros**

* `as`: Utilizado para renomear importações ou realizar castings.
* `is`: Verifica se uma variável é de um determinado tipo.
* `in`: Verifica se um valor está contido em uma coleção.
* `isreftype`: Verifica se um tipo é uma referência.
* `sizeof`: Retorna o tamanho em bytes de um tipo ou variável.
* `typeof`: Retorna o tipo de uma variável.
* `__offsetof`: Retorna o deslocamento de um campo dentro de uma estrutura.
* `__global`: Declara uma variável global; requer a flag `-enable-globals` para uso.
* `spawn`: Inicia uma nova goroutine (thread leve) para execução concorrente.
* `go`: Similar ao `spawn`; inicia uma nova goroutine.
* `defer`: Adia a execução de uma função até o final do escopo atual.
* `static`: Indica que uma variável ou função tem duração estática.
* `assert`: Verifica se uma condição é verdadeira; caso contrário, interrompe a execução.
* `asm`: Permite a inserção de código assembly inline.

---

## **2. Operadores**

### **2.1 Operadores Aritméticos**
| Operador | Descrição |
| :---: | --- |
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `%` | Módulo (resto da divisão) |

### **2.2. Operadores de Atribuição**
| Operador | Descrição |
| :---: | --- |
| `=` | Atribuição simples |
| `:=` | Declaração de variáveis com inferência de tipo e atribuição |  
| `+=` | Adição e atribuição |
| `-=` | Subtração e atribuição |
| `*=` | Multiplicação e atribuição |
| `/=` | Divisão e atribuição |
| `%=` | Módulo e atribuição |
| `&=` | E bit a bit e atribuição |
| `\|=` | OU bit a bit e atribuição |
| `^=` | XOR bit a bit e atribuição |
| `<<=` | Deslocamento à esquerda e atribuição |
| `>>=` | Deslocamento à direita e atribuição |

### **2.3. Operadores de Comparação**
| Operador | Descrição |
| :---: | --- |
| `==` | Igual a |
| `!=` | Diferente de |
| `<` | Menor que |
| `<=` | Menor ou igual a |
| `>` | Maior que |
| `>=` | Maior ou igual a |

### **2.4. Operadores Lógicos**
| Operador | Descrição |
| :---: | --- |
| `&&` | E lógico |
| `\|\|` | OU lógico |
| `!` | NÃO lógico |

### **2.5. Operadores Bit a Bit (Bitwise)**
| Operador | Descrição |
| :---: | --- |
| `&` | E (AND) |
| `\|` | OU (OR) |
| `^` | OU Exclusivo (XOR) |
| `<<` | Deslocamento à esquerda |
| `>>` | Deslocamento à direita |

---

## **3. Separadores ou Delimitadores**
A linguagem Vlang não possui delimitador para linhas, isto é, não é como em C, por exemplo, que necessita do `';'` para o compilador entender que o comando encerrou. Vlang delimita parâmetros de funções ao utilizar a `','` entre os parâmetros. Vlang também pode separar expressões para dar prioridade com o uso de `()`. Por fim, nessa linguagem, os blocos de comando são delimitados por `\`

- **Parênteses `()`**: Usados em chamadas de função, agrupamento de expressões e definições de tipo de função.
- **Chaves `{}`**: Usadas para delimitar blocos de código (corpo de funções, laços, condicionais) e para a inicialização de literais de struct, array e mapa.
- **Colchetes `[]`**: Usados para acessar elementos de arrays e mapas, e para definir tipos de array.
- **Ponto `.`**: Usado para acessar membros de structs e módulos.
- **Vírgula `,`**: Usada para separar elementos em listas (argumentos de função, elementos de array, etc.).
- **Ponto e vírgula `;`**: Geralmente opcional em V, pois o compilador insere-os automaticamente no final das linhas. Seu uso explícito é raro.
- **Dois pontos `:`**: Usado em conjunto com `=` na declaração curta de variáveis (`:=`).

---

## **4. Identificadores**
Identificadores são os nomes dados a entidades como variáveis, constantes, funções, tipos e módulos.

- **Regras de Nomenclatura**:
  - Devem começar com uma letra (`a-z`) ou um sublinhado (`_`).
  - Identificadores que começam com letra maiúscula são usados para tipos exportados (como Pessoa, Usuario, etc.).
  - Após o primeiro caractere, podem conter letras, números (`0-9`) e sublinhados.
  - Não podem conter espaços nem símbolos como `@`, `#`, `%`, `-`, etc.
  - Palavras-chave (reservadas) não podem ser usadas como identificadores.
  - V é **case-sensitive**, o que significa que `minhaVariavel` e `minhavariavel` são identificadores distintos.

- **Convenções**:
  - **`camelCase`**: Usado para variáveis e funções (`nomeUsuario`, `calcularTotal`).
  - **`PascalCase`** (ou **`CapitalCase`**): Usado para tipos, como structs, enums e interfaces (`Usuario`, `OpcoesDePagamento`).

- **Exemplos de Identificadores Válidos**:
  - `idade`
  - `_temp`
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

- **Strings Comuns**: Delimitadas por aspas simples (`''`). Sequências de escape (como `\n`, `\t`, `\"`) são interpretadas.

  ```
  minha_string := 'Olá, mundo!\nIsto está em uma nova linha.'
  ```
  
   ---

 ## **8. Erros**
 Na linguagem V, qualquer sequência de caracteres que não corresponda a um dos elementos léxicos válidos, como identificadores, literais, operadores ou palavras-chave, é considerada um erro léxico. Isso inclui, por exemplo, o uso de símbolos não reconhecidos, identificadores iniciando com números ou o uso de palavras que não pertencem à linguagem.
Durante a análise léxica, espaços em branco, tabulações e quebras de linha são ignorados para fins de reconhecimento de tokens. Eles não afetam a interpretação dos elementos do código, exceto quando são essenciais para separar tokens ou evitar ambiguidade. Por exemplo, a:=10 e a := 10 são equivalentes, mas a ausência completa de espaço entre dois identificadores distintos poderia causar erro.
Embora espaços e quebras de linha não alterem o significado léxico, o compilador da linguagem V utiliza essas quebras de linha para rastrear a posição do código, permitindo que mensagens de erro sejam emitidas com precisão, indicando a linha e a coluna onde ocorreu o problema. Assim, mesmo que ignoradas na análise dos símbolos, essas informações são essenciais para diagnóstico e depuração durante a compilação.

