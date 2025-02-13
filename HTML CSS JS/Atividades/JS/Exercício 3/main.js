let reais = window.prompt("Digite o valor em reais(R$): ")
let cotacao = window.prompt("Digite a cotação atual do dolár: ")
reais = float(reais)
cotacao = float(cotacao)
let resultado = reais / cotacao
resultado = float(resultado)

window.alert(`
 - Valor em Reais: R$${reais}
 - Cotação atual do Dólar: R$${cotacao}
 - Valor em Dólares: $${resultado}
 `)
