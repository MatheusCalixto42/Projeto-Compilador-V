Claro, aqui está um Markdown completo sobre a parte léxica da linguagem de programação V, ideal para um repositório no GitHub.

---

# Léxico da Linguagem de Programação V

Este documento detalha os elementos léxicos da linguagem de programação V. O léxico de uma linguagem define o conjunto de regras que governam como uma sequência de caracteres é dividida em "tokens" ou elementos básicos do código.

---

## **Comentários** 💬

Comentários são anotações no código-fonte que são ignoradas pelo compilador. V suporta dois tipos de comentários.

### **Comentários de Linha Única**

Começam com `//`. Todo o texto desde `//` até o final da linha é considerado um comentário.

```v
// Este é um comentário de linha única.
x := 10 // Isso atribui o valor 10 à variável x.
```

### **Comentários de Múltiplas Linhas**

Começam com `/*` e terminam com `*/`. Eles podem abranger várias linhas.

```v
/*
  Este é um exemplo
  de um comentário
  de múltiplas linhas.
*/
```

---

## **Identificadores**

Identificadores são os nomes dados a entidades como variáveis, constantes, funções, tipos e módulos.

- **Regras de Nomenclatura**:
  - Devem começar com uma letra (`a-z`, `A-Z`) ou um sublinhado (`_`).
  - Após o primeiro caractere, podem conter letras, números (`0-9`) e sublinhados.
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

## **Palavras-chave** 🔑

Palavras-chave são palavras reservadas com significado especial para o compilador e não podem ser usadas como identificadores.

| Palavra-chave | Descrição |
| --- | --- |
| `as` | Usado para conversão de tipo (type casting) e renomeação de importações. |
| `const` | Declara uma constante. |
| `else` | Parte de uma estrutura condicional `if-else`. |
| `enum` | Declara uma enumeração. |
| `fn` | Declara uma função. |
| `for` | Usado para laços de repetição. |
| `go` | Inicia a execução de uma função em uma nova goroutine (concorrência). |
| `if` | Inicia uma estrutura condicional. |
| `import` | Importa um módulo. |
| `in` | Usado em laços `for` para iterar sobre arrays, mapas e ranges. |
| `interface` | Declara uma interface. |
| `is` | Usado em expressões `match` para verificação de tipo. |
| `match` | Inicia uma estrutura de correspondência de padrões, similar ao `switch`. |
| `module` | Declara o nome do módulo do arquivo. |
| `mut` | Marca uma variável como mutável. |
| `pub` | Torna uma declaração (função, struct, etc.) pública e exportável. |
| `return` | Retorna um valor de uma função. |
| `select` | Usado em concorrência para esperar por múltiplas operações de canais. |
| `static` | Usado para declarar métodos associados a um tipo, não a uma instância. |
| `struct` | Declara uma estrutura (um tipo de dado composto). |
| `type` | Usado para criar um alias (apelido) para um tipo existente. |
| `unsafe` | Denota um bloco de código que pode violar as garantias de segurança do V. |

---

## **Operadores** 🧮

Operadores são símbolos especiais que realizam operações em operandos (valores e variáveis).

### **Operadores Aritméticos**
| Operador | Descrição |
| :---: | --- |
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `%` | Módulo (resto da divisão) |

### **Operadores de Atribuição**
| Operador | Descrição |
| :---: | --- |
| `=` | Atribuição simples |
| `:=` | Declaração curta com inferência de tipo e atribuição |
| `+=` | Adição e atribuição |
| `-=` | Subtração e atribuição |
| `*=` | Multiplicação e atribuição |
| `/=` | Divisão e atribuição |
| `%=` | Módulo e atribuição |
| `&=` | E bit a bit e atribuição |
| `|=` | OU bit a bit e atribuição |
| `^=` | XOR bit a bit e atribuição |
| `<<=` | Deslocamento à esquerda e atribuição |
| `>>=` | Deslocamento à direita e atribuição |

### **Operadores de Comparação**
| Operador | Descrição |
| :---: | --- |
| `==` | Igual a |
| `!=` | Diferente de |
| `<` | Menor que |
| `<=` | Menor ou igual a |
| `>` | Maior que |
| `>=` | Maior ou igual a |

### **Operadores Lógicos**
| Operador | Descrição |
| :---: | --- |
| `&&` | E lógico |
| `||` | OU lógico |
| `!` | NÃO lógico |

### **Operadores Bit a Bit (Bitwise)**
| Operador | Descrição |
| :---: | --- |
| `&` | E (AND) |
| `|` | OU (OR) |
| `^` | OU Exclusivo (XOR) |
| `<<` | Deslocamento à esquerda |
| `>>` | Deslocamento à direita |

---

## **Literais**

Literais são as representações de valores fixos no código-fonte.

### **Literais Inteiros**
Representam números inteiros e podem ser especificados em diferentes bases.

- **Decimal**: `123`, `42`, `1000`
- **Hexadecimal** (prefixo `0x`): `0xFF`, `0x1A`
- **Binário** (prefixo `0b`): `0b1010`, `0b1101`
- **Octal** (prefixo `0o`): `0o77`, `0o12`

### **Literais de Ponto Flutuante**
Representam números com casas decimais.

- **Padrão**: `3.14`, `0.5`, `100.0`
- **Notação Científica**: `6.022e23`, `1.5E-10`

### **Literais de Rune**
Representam um único caractere Unicode e são delimitados por aspas simples (`'`).

- **Exemplos**: `'a'`, `'B'`, `'$'`, `'\n'` (caractere de nova linha)

### **Literais de String**
Representam sequências de caracteres. V possui dois tipos.

- **Strings Interpretadas**: Delimitadas por aspas duplas (`"`). Sequências de escape (como `\n`, `\t`, `\"`) são interpretadas.

  ```v
  minha_string := "Olá, mundo!\nIsto está em uma nova linha."
  ```

- **Strings Brutas (Raw Strings)**: Delimitadas por crases (`` ` ``). Todo o conteúdo é lido literalmente, sem interpretar sequências de escape. Útil para caminhos de arquivo ou expressões regulares.

  ```v
  caminho := `C:\Usuarios\MeuUsuario\Documentos`
  ```

### **Literais Booleanos**
Representam os dois valores lógicos.

- `true`
- `false`

---

## **Separadores**

Separadores são caracteres que ajudam a definir a estrutura do código.

- **Parênteses `()`**: Usados em chamadas de função, agrupamento de expressões e definições de tipo de função.
- **Chaves `{}`**: Usadas para delimitar blocos de código (corpo de funções, laços, condicionais) e para a inicialização de literais de struct, array e mapa.
- **Colchetes `[]`**: Usados para acessar elementos de arrays e mapas, e para definir tipos de array.
- **Ponto `.`**: Usado para acessar membros de structs e módulos.
- **Vírgula `,`**: Usada para separar elementos em listas (argumentos de função, elementos de array, etc.).
- **Ponto e vírgula `;`**: Geralmente opcional em V, pois o compilador insere-os automaticamente no final das linhas. Seu uso explícito é raro.
- **Dois pontos `:`**: Usado em conjunto com `=` na declaração curta de variáveis (`:=`).