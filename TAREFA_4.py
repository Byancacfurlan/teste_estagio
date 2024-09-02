#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por 
# estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de 
# representação que cada estado teve dentro do valor total mensal da
# distribuidora.  

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
percentualSp= (sp*100)/total
percentualRj= (rj*100)/total
percentualMg= (mg*100)/total
percentualEs= (es*100)/total
percentualOutros= (outros*100)/total

print(f"O percentual de representação de São Paulo foi de: {percentualSp}%",
      f"\n O percentual de representação do Rio de Janeiro foi de: {percentualRj}%",
      f"\n O percentual de representação de Minas Gerais foi de: {percentualMg}%",
      f"\n O percentual de representação do Espírito Santo foi de: {percentualEs}%",
      f"\n O percentual de representação doss outros estados foi de: {percentualOutros}%")
