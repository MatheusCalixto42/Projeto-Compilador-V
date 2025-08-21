fn soma(a int, b int) int {
	return a + b
}
fn main(){
	println('Hello World!')

	nome := 'Matheus'	// Variável imutável (seria o const do C)
	mut idade := 30		// Variável mutável (igual a uma variável comum no C)
    mut somar := 10
    //const teste1 := 10
	println('Nome: ${nome}')
	println('Idade: ${idade}')

	idade = 25

	print('Idade atualizada: ${idade}\n')

	println('\n---------------------------------------\n')

	//saldo := 100.50	// Padrão f64
	esta_ativo := true	// booleano
	//letras := ['a', 'b', 'c']	// []rune (array de caracteres)

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
	
	//numeros := [1,2,3,4,5]
	for i in numeros {
		println('Número: ${i}')
	}
    mut x := 0
    for x < 5{
        println('Contador: ${x}')
        //x++
    }

	println('\n---------------------------------------\n')
    //somar += soma((2+3), numeros[1]) + 3
	println('Função soma: ${somar}')
    mut soma2 := 5
    //mut soma1 := 5 + 4 * (soma2++)
    //soma1 = (soma2++) + 2
    println(soma1)
	println(teste1)

}
