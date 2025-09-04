const teste1 := 10
fn soma(a int, b int) int {
	mut fnum := [3]int
	return a + b
}
const teste2 := 10
fn teste(a int){
	mut list := [3]int
	list[0] = 1
	list[1] = 2
	list[2] = list[0]
	println(list[..])
	println(list[1])
	println(list[0..1])
}

const teste3 := 10
fn main(){

	println('Hello World!')
	rocket := `b`
	nome := 'Matheus'	// Variável imutável (seria o const do C)
	mut idade := 30		// Variável mutável (igual a uma variável comum no C)
    mut somar := 10
	println('Nome: ${nome}')
	println('Idade: ${idade}')

	idade = 25

	print('Idade atualizada: ${idade}\n')

	println('\n---------------------------------------\n')

	saldo := 100.50	// Padrão f64

	
	esta_ativo := true	// booleano
	letras := ['a', 'b', 'c']	// []rune (array de caracteres)
	listaboolean := [true, false, true] // []bool (array de booleanos)
	mut listateste := [(1+1),2]
	listateste[1] = 3
	println(listateste)
	
	println('Saldo: ${saldo}')
	println('Ativo: ${esta_ativo}')
	println('Primeira letra: ${letras[0]}')

	println('\n---------------------------------------\n')

	if idade < 25 {
		println('Idade menor que 25 anos')
	} else if idade == 25 {
		println('Idade igual a 25 anos')
	} else {
		println('Idade maior que 25 anos')
	}

	println('\n---------------------------------------\n')
    
	for  i :=0 ; i < 5; i++ {
		println('Contador: ${i}')
	}
	
	numeros := [1,2,3,4,5]
	tam := sizeof(numeros)
	mut jfg := 0
	
	for i := 0; i < 20; i++ {
    	jfg += 2
    	if jfg >= 10 {
        	break
    	}
	}

	for i in numeros {
		println('Número: ${i}')

	}
    mut x := 0
    for x < 5{
        println('Contador: ${x}')
        //x++
    }
	x--
	println('\n---------------------------------------\n')
  	somar += soma((2+3), numeros[1]) + 3
	somar ^= 4
	soma(3,5)
	println('Função soma: ${somar}')
  	mut soma2 := 5
	mut soma1 := 5 + 4 * (soma2++)
  	soma1 = (soma2++) + 2
  	println(soma1)
	
	a := 0x7B
	b := 0b01111011
	c := 0o173
	
}
const teste4 := 10

fn soma222(a int, b int) int {
	mut fnum := [3]int
	return a + b
}
const teste5 := 10