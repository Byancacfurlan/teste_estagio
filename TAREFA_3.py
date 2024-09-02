#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json

with open('INICIO/teste_estagio/dadosFaturamento.json', 'r') as arquivo:
    json_dados = json.load(arquivo)

faturamentoDiario= json_dados['faturamento']
menorValor = float('inf')
maiorValor=float('-inf')
soma= 0
diasFaturamento = 0
diasAcima = 0
for dia in faturamentoDiario:
    valor = dia['valorDiario']
    if valor >0: 
        if valor<menorValor:
            menorValor = valor
        if valor>maiorValor:
            maiorValor= valor
        soma+=valor
        diasFaturamento+=1

if diasFaturamento>0:
    mediaMensal = soma/diasFaturamento
else:
    mediaMensal=0

for dia in faturamentoDiario:
    valor = dia['valorDiario']
    if valor>mediaMensal:
        diasAcima +=1


print(f"Menor valor de faturamentofoi de: {menorValor}",
      f"\nMaior valor de faturamento foi:{maiorValor}",
      f"\nNúmero de dias com faturamento a cima da média mensal foi de: {diasAcima}")